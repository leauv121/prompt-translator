# Prompt Translator — Web App

> 🔮 你说需求，AI 帮你转化为最佳提示词。无需学习提示词工程。

## 两种使用方式

### 方式一：在线使用（推荐）

部署到免费托管服务，发网址给别人就能用：

**GitHub Pages（免费）：**
```bash
# 1. 在 GitHub 创建新仓库 prompt-translator
# 2. 推送代码
git init
git add index.html README.md
git commit -m "feat: Prompt Translator web app"
git remote add origin https://github.com/YOUR_USER/prompt-translator.git
git push -u origin main

# 3. 在仓库 Settings > Pages > Source 选择 main 分支，保存
# 4. 等待1分钟，访问 https://YOUR_USER.github.io/prompt-translator/
```

**Vercel（免费，国内访问更快）：**
```bash
npx vercel --prod
```

**Netlify（免费，拖拽部署）：**
直接拖 `index.html` 到 https://app.netlify.com/drop

### 方式二：离线使用

1. 下载 `index.html`
2. 双击打开（浏览器中运行）
3. 填入你的 API Key
4. 所有数据存本地，不上传服务器

## 功能

| 功能 | 说明 |
|------|------|
| 🤖 AI 智能模式 | 你说需求，AI 追问关键信息后生成最佳 prompt |
| 📝 手动引导模式 | 按 SPACES 框架填表，自动拼装成 prompt |
| 🔌 多模型支持 | DeepSeek / Claude / ChatGPT / Gemini / 自定义 |
| 📋 一键复制 | 生成后点复制，直接粘贴到任何 AI 工具 |
| 📜 历史记录 | 自动保存到浏览器，随时回溯 |
| 🌙 暗色模式 | 晚上用不刺眼 |
| 📱 响应式 | 手机、平板、电脑都能用 |
| 🔒 隐私安全 | API Key 只存在你浏览器里，不上传任何服务器 |

## 支持的模型

| 提供商 | 可用模型 | 获取 API Key |
|--------|---------|-------------|
| **DeepSeek** | deepseek-chat, deepseek-reasoner | https://platform.deepseek.com |
| **Claude** | claude-sonnet-4-6, claude-opus-4-8 | https://console.anthropic.com |
| **ChatGPT** | gpt-4o, gpt-4o-mini | https://platform.openai.com |
| **Gemini** | gemini-2.5-flash, gemini-2.5-pro | https://aistudio.google.com |
| **自定义** | 任何 OpenAI 兼容接口 | 你自己的服务 |

## 本地开发

无需安装任何依赖。直接打开 `index.html` 即可。

```bash
# 或者用任何静态服务器
python3 -m http.server 8080
# 访问 http://localhost:8080
```

## 开源协议

MIT License
