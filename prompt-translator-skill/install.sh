#!/bin/sh
# install.sh — Install prompt-translator-skill to detected platforms
#
# Usage:
#   ./install.sh              # Install to all detected platforms
#   ./install.sh --dry-run    # Preview without making changes
#   ./install.sh --uninstall  # Remove all symlinks pointing to this repo
#   ./install.sh --platform cursor  # Install to specific platform
#   ./install.sh --all             # Install to all platforms forcefully
#
# POSIX-compatible (works in bash, dash, zsh, ash).

set -eu

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SKILL_NAME="prompt-translator-skill"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

# ---------------------------------------------------------------------------
# Colors (disabled when stdout is not a terminal)
# ---------------------------------------------------------------------------
if [ -t 1 ]; then
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    RED='\033[0;31m'
    BOLD='\033[1m'
    NC='\033[0m'
else
    GREEN='' YELLOW='' BLUE='' RED='' BOLD='' NC=''
fi

info()    { printf "${BLUE}[INFO]${NC}  %s\n" "$1"; }
success() { printf "${GREEN}[OK]${NC}    %s\n" "$1"; }
warn()    { printf "${YELLOW}[WARN]${NC}  %s\n" "$1"; }
error()   { printf "${RED}[ERROR]${NC} %s\n" "$1" >&2; }

# ---------------------------------------------------------------------------
# Options
# ---------------------------------------------------------------------------
DRY_RUN=false
UNINSTALL=false
TARGET_PLATFORM=""
INSTALL_ALL=false

while [ $# -gt 0 ]; do
    case "$1" in
        --dry-run)   DRY_RUN=true ;;
        --uninstall) UNINSTALL=true ;;
        --all)       INSTALL_ALL=true ;;
        --platform)
            shift
            TARGET_PLATFORM="$1"
            ;;
        -h|--help)
            printf "Usage: %s [options]\n\n" "$0"
            printf "Options:\n"
            printf "  --platform <name>  Install to specific platform (claude, cursor, copilot, gemini, windsurf, cline, codex, kiro, trae, goose, opencode, roo-code, antigravity, universal)\n"
            printf "  --all              Install to all platforms\n"
            printf "  --dry-run          Preview without making changes\n"
            printf "  --uninstall        Remove all symlinks pointing to this repo\n"
            printf "  -h, --help         Show this help message\n"
            exit 0
            ;;
        *)
            error "Unknown option: $1"
            exit 1
            ;;
    esac
    shift
done

# ---------------------------------------------------------------------------
# Platform path definitions (user-level)
# ---------------------------------------------------------------------------
platform_path() {
    case "$1" in
        universal)  echo "$HOME/.agents/skills/$SKILL_NAME" ;;
        claude)     echo "$HOME/.claude/skills/$SKILL_NAME" ;;
        gemini)     echo "$HOME/.gemini/skills/$SKILL_NAME" ;;
        goose)      echo "$HOME/.config/goose/skills/$SKILL_NAME" ;;
        opencode)   echo "$HOME/.config/opencode/skills/$SKILL_NAME" ;;
        copilot)    echo "$HOME/.copilot/skills/$SKILL_NAME" ;;
        cursor)     echo "$HOME/.cursor/rules/$SKILL_NAME" ;;
        windsurf)   echo "$HOME/.windsurf/rules/$SKILL_NAME" ;;
        cline)      echo "$HOME/.clinerules/$SKILL_NAME" ;;
        codex)      echo "$HOME/.agents/skills/$SKILL_NAME" ;;
        kiro)       echo "$HOME/.kiro/skills/$SKILL_NAME" ;;
        trae)       echo "$HOME/.trae/rules/$SKILL_NAME" ;;
        roo-code)   echo "$HOME/.roo/rules/$SKILL_NAME" ;;
        antigravity) echo "$HOME/.agents/skills/$SKILL_NAME" ;;
        *)
            error "Unknown platform: $1"
            return 1
            ;;
    esac
}

platform_detect_dir() {
    case "$1" in
        universal)  echo "$HOME/.agents" ;;
        claude)     echo "$HOME/.claude" ;;
        gemini)     echo "$HOME/.gemini" ;;
        goose)      echo "$HOME/.config/goose" ;;
        opencode)   echo "$HOME/.config/opencode" ;;
        copilot)    echo "$HOME/.copilot" ;;
        cursor)     echo "$HOME/.cursor" ;;
        windsurf)   echo "$HOME/.windsurf" ;;
        cline)      echo "$HOME/.clinerules" ;;
        codex)      echo "$HOME/.agents" ;;
        kiro)       echo "$HOME/.kiro" ;;
        trae)       echo "$HOME/.trae" ;;
        roo-code)   echo "$HOME/.roo" ;;
        antigravity) echo "$HOME/.agents" ;;
        *)
            echo ""
            ;;
    esac
}

# ---------------------------------------------------------------------------
# Create a symlink (with fallback to copy)
# ---------------------------------------------------------------------------
create_symlink() {
    target="$1"
    link_path="$2"

    if [ "$target" = "$link_path" ]; then
        return 0
    fi

    mkdir -p "$(dirname "$link_path")"

    if [ -e "$link_path" ] || [ -L "$link_path" ]; then
        rm -rf "$link_path"
    fi

    if ln -s "$target" "$link_path" 2>/dev/null; then
        return 0
    else
        warn "Symlink failed for $link_path — falling back to copy"
        cp -R "$target" "$link_path"
    fi
}

# ---------------------------------------------------------------------------
# Uninstall
# ---------------------------------------------------------------------------
do_uninstall() {
    printf "\n${BOLD}Uninstalling $SKILL_NAME${NC}\n\n"
    removed=0

    for plat in universal claude gemini goose opencode copilot cursor windsurf cline codex kiro trae roo-code antigravity; do
        dest="$(platform_path "$plat" 2>/dev/null || true)"
        if [ -n "$dest" ] && [ -L "$dest" ]; then
            link_target="$(readlink "$dest" 2>/dev/null || true)"
            if [ "$link_target" = "$REPO_DIR" ]; then
                if [ "$DRY_RUN" = true ]; then
                    info "[dry-run] Would remove: $dest ($plat)"
                else
                    rm "$dest"
                    success "Removed: $dest ($plat)"
                fi
                removed=$((removed + 1))
            fi
        fi
    done

    if [ "$removed" -eq 0 ]; then
        info "No symlinks found."
    fi

    if [ "$DRY_RUN" = true ]; then
        printf "\n${YELLOW}Dry run — no changes made.${NC}\n"
    else
        printf "\nDone.\n"
    fi
}

# ---------------------------------------------------------------------------
# Install
# ---------------------------------------------------------------------------
do_install() {
    printf "\n${BOLD}Prompt Translator Skill — Installer${NC}\n\n"
    info "Source: $REPO_DIR"

    count=0

    if [ -n "$TARGET_PLATFORM" ]; then
        # Install to specific platform only
        dest="$(platform_path "$TARGET_PLATFORM")"
        if [ "$DRY_RUN" = true ]; then
            info "[dry-run] Would install: $dest ← $REPO_DIR ($TARGET_PLATFORM)"
        else
            create_symlink "$REPO_DIR" "$dest"
            success "Installed for $TARGET_PLATFORM → $dest"
        fi
        count=$((count + 1))
    else
        # Auto-detect platforms (or install all)
        for plat in universal claude gemini goose opencode copilot cursor windsurf cline codex kiro trae roo-code antigravity; do
            detect="$(platform_detect_dir "$plat")"
            dest="$(platform_path "$plat")"

            if [ "$INSTALL_ALL" = true ] || [ -d "$detect" ] || [ "$plat" = "universal" ]; then
                if [ "$DRY_RUN" = true ]; then
                    info "[dry-run] Would install: $dest ← $REPO_DIR ($plat)"
                else
                    create_symlink "$REPO_DIR" "$dest"
                    success "Installed for $plat → $dest"
                fi
                count=$((count + 1))
            fi
        done
    fi

    # Summary
    printf "\n${BOLD}Done!${NC} Installed to $count platform(s).\n\n"

    if [ "$DRY_RUN" = true ]; then
        printf "${YELLOW}Dry run — no changes made.${NC}\n\n"
    else
        printf "  Source: ${BOLD}%s${NC}\n" "$REPO_DIR"
        printf "  Run ${BOLD}git pull${NC} from that directory to update.\n\n"
    fi

    printf "${BOLD}How to use:${NC}\n"
    printf "  Open your AI agent and type:\n"
    printf "    /prompt-translator-skill 帮我写一个分析销售数据的提示词\n"
    printf "  Or naturally:\n"
    printf "    我不知道怎么问AI，我的需求是...\n\n"
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if [ "$UNINSTALL" = true ]; then
    do_uninstall
else
    do_install
fi
