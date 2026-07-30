# Wenmai Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-orange)](https://agentskills.io)
[![Skills](https://img.shields.io/badge/skills-69-brightgreen)](#skills-catalog)
[![npm](https://img.shields.io/npm/v/%40wenmai-ai%2Fskills.svg)](https://www.npmjs.com/package/@wenmai-ai/skills)

**Wenmai Skills** 是面向跨境电商的数据型 AI Skill 集合，提供 69 个 API 驱动的原子能力，覆盖多平台商品与内容采集、Amazon 评论、JIIMORE、Keepa、卖家精灵（SellerSprite）、SIF 和 Sorftime 等数据源。

本仓库遵循 [Agent Skills](https://agentskills.io) 开放标准，可用于稳卖 Agent、Codex、Claude Code、Cursor、GitHub Copilot 等支持 Agent Skills 的 AI 编程与智能体平台。

---

## Installation

请先安装 [Node.js](https://nodejs.org/)，Node.js 会同时提供 `npx`。

### Install all skills

使用交互式安装器选择目标 Agent 和安装方式：

```bash
npx skills add wenmai-ai/wenmai-skills
```

### Install specific skills

```bash
npx skills add wenmai-ai/wenmai-skills --skill wenmai-sif-asin-keywords wenmai-amazon-reviews
```

### List available skills

```bash
npx skills add wenmai-ai/wenmai-skills --list
```

### Install for a specific agent

```bash
npx skills add wenmai-ai/wenmai-skills --agent wenmai-agent
npx skills add wenmai-ai/wenmai-skills --agent codex
npx skills add wenmai-ai/wenmai-skills --agent claude-code
npx skills add wenmai-ai/wenmai-skills --agent cursor
```

### Install the npm package

`@wenmai-ai/skills` 是包含全部 Skills 的 npm 聚合包：

```bash
npm install @wenmai-ai/skills
```

npm 会把完整集合下载到 `node_modules/@wenmai-ai/skills`，但不会自动注册到 Agent。可以继续使用 Skills CLI 从本地包中安装指定 Skill：

```bash
npx skills add ./node_modules/@wenmai-ai/skills \
  --skill wenmai-sif-asin-keywords \
  -g -a codex -y
```

### Install for Wenmai Agent

安装器要求显式指定目标 Agent；不传 `--agent` 时不会执行安装。

更新最新的版本的Wenmai Agent。

安装全部 Skills：

```bash
npx @wenmai-ai/skills install --agent wenmai-agent
```

安装单个 Skill：

```bash
npx @wenmai-ai/skills install wenmai-sif-asin-keywords --agent wenmai-agent
```

更新已经安装的 Skills：

```bash
npx @wenmai-ai/skills install --agent wenmai-agent --force
```

安装器会自动识别系统并使用以下目录：

- macOS：`~/Library/Application Support/Wenmai Agent/wenmai-cli/skills`
- Windows：`%APPDATA%\wenmaiAgent\wenmai-cli\skills`

### Install for Codex with the npm package

安装全部 Skills：

```bash
npx @wenmai-ai/skills install --agent codex
```

安装单个 Skill：

```bash
npx @wenmai-ai/skills install wenmai-sif-asin-keywords --agent codex
```

默认安装目录为 `${CODEX_HOME:-~/.codex}/skills`。

## Setup

所有 Skills 通过稳卖标准 API 获取数据。使用前请配置 API Key：

1. 参考[稳卖 Skills 使用指南](https://skill.wenmai-ai.com/wenmaiskills/use_guide.html)获取 `secret-key`。
2. 设置环境变量：

   ```bash
   export WENMAI_API_KEY=sk-...
   ```

也可使用兼容变量 `WENMAI_SECRET_KEY`。每个 Skill 的完整参数、响应字段和调用示例见其 `references/api.md`。

## Skills Catalog

### Alpha 多平台采集

| Skill | Description |
| --- | --- |
| `wenmai-alpha-amazon-reviews-extractor` | 采集 Amazon 商品评论 |
| `wenmai-alpha-douyin-product-search-scraper` | 搜索并采集抖音商品 |
| `wenmai-alpha-etsy-scraper` | 采集 Etsy 手作与小众商品 |
| `wenmai-alpha-facebook-ads-scraper` | 采集 Facebook / Meta 广告库素材 |
| `wenmai-alpha-google-search-scraper` | 采集 Google 搜索结果 |
| `wenmai-alpha-google-trends-scraper` | 采集 Google Trends 趋势数据 |
| `wenmai-alpha-instagram-scraper` | 采集 Instagram 账号、话题与内容 |
| `wenmai-alpha-lazada-scraper` | 采集 Lazada 商品数据 |
| `wenmai-alpha-ozon-scraper-pro` | 采集 Ozon 商品池数据 |
| `wenmai-alpha-reddit-scraper-search-fast` | 快速搜索 Reddit 帖子、评论与舆情 |
| `wenmai-alpha-shein-scraper` | 采集 SHEIN 商品信息 |
| `wenmai-alpha-shopee-scraper` | 采集 Shopee 商品与店铺信息 |
| `wenmai-alpha-temu-products-scraper` | 采集 Temu 商品池数据 |
| `wenmai-alpha-tiktok-scraper` | 采集 TikTok 视频、账号、话题与趋势 |
| `wenmai-alpha-walmart-fast-product-scraper` | 快速采集 Walmart 商品信息 |
| `wenmai-alpha-walmart-reviews-scraper` | 采集 Walmart 商品评论 |
| `wenmai-alpha-wildberries-products-search-scraper` | 搜索并采集 Wildberries 商品 |
| `wenmai-alpha-xiaohongshu-pro-scraper` | 采集小红书笔记、关键词与内容趋势 |
| `wenmai-alpha-youtube-comments-scraper` | 采集 YouTube 视频评论 |
| `wenmai-alpha-youtube-scraper` | 采集 YouTube 视频、频道与搜索结果 |

### Amazon 评论与 Keepa

| Skill | Description |
| --- | --- |
| `wenmai-amazon-reviews` | 按 ASIN 获取 Amazon 买家评论，用于 VOC 与竞品研究 |
| `wenmai-keepa-product-history` | 查询价格、BSR、Buy Box、评分与评论等历史走势 |
| `wenmai-keepa-product-search` | 按关键词搜索 Keepa 商品池 |

### JIIMORE

| Skill | Description |
| --- | --- |
| `wenmai-jiimore-expand-aba-keywords-by-keyword` | 按种子关键词扩展 Amazon ABA 关键词 |
| `wenmai-jiimore-find-aba-asins-by-keyword` | 按关键词查询 ABA 关联商品与 ASIN |
| `wenmai-jiimore-find-asins-batch` | 批量查询 Amazon ASIN 摘要信息 |
| `wenmai-jiimore-find-asins-by-keyword` | 按关键词搜索 Amazon 商品与 ASIN |
| `wenmai-jiimore-find-niches-by-asin` | 按 ASIN 查找所属或相关细分市场 |
| `wenmai-jiimore-find-niches-by-keyword` | 按关键词查找相关细分市场 |
| `wenmai-jiimore-find-same-niche-asins` | 查询与指定 ASIN 同细分市场的商品 |
| `wenmai-jiimore-find-similar-asins` | 基于 ABA 关系查询相似 ASIN |
| `wenmai-jiimore-get-asin-details` | 查询一个或多个 Amazon ASIN 的商品详情 |
| `wenmai-jiimore-get-keyword-rankings` | 反查 ASIN 的关联关键词与排名 |
| `wenmai-jiimore-get-niche-asins` | 查询指定细分市场中的商品与 ASIN |
| `wenmai-jiimore-get-niche-details` | 查询 Amazon 细分市场详情与指标 |
| `wenmai-jiimore-get-niche-keywords` | 查询指定细分市场的关键词池 |
| `wenmai-jiimore-search-aba-keywords` | 按 ASIN 查询 ABA 关键词 |
| `wenmai-jiimore-search-keywords-batch` | 批量查询 Amazon 关键词指标 |
| `wenmai-jiimore-search-keywords-by-asin` | 按 ASIN 查询关联关键词 |
| `wenmai-jiimore-search-keywords-by-keyword` | 围绕种子词扩展 Amazon 相关关键词 |

### SellerSprite（卖家精灵）

| Skill | Description |
| --- | --- |
| `wenmai-sellersprite-asin-detail` | 查询单个 Amazon ASIN 的完整商品详情 |
| `wenmai-sellersprite-asin-detail-with-coupon-trend` | 查询 ASIN 商品详情及 Coupon 趋势 |
| `wenmai-sellersprite-competitor` | 按 ASIN、品牌、卖家或类目查询竞品 |
| `wenmai-sellersprite-google-trend` | 查询关键词在指定市场的 Google Trends 趋势 |
| `wenmai-sellersprite-market-research` | 查询类目市场规模、集中度与机会指标 |
| `wenmai-sellersprite-market-statistics` | 查询 Amazon 类目节点统计 |
| `wenmai-sellersprite-product-search` | 按销量、收入、价格、评分等条件筛选 Amazon 商品池 |
| `wenmai-sellersprite-review` | 查询 Amazon ASIN 的评论列表与评分信息 |
| `wenmai-sellersprite-traffic-keyword` | 查询 ASIN 流量关键词、自然位与广告位 |
| `wenmai-sellersprite-traffic-keyword-stat` | 分析 ASIN 流量关键词结构概览 |
| `wenmai-sellersprite-traffic-listing` | 查询 ASIN 关联商品与竞品关系 |
| `wenmai-sellersprite-traffic-source` | 分析 ASIN / 关键词维度的流量来源结构 |

### SIF 搜索智能

| Skill | Description |
| --- | --- |
| `wenmai-sif-asin-keywords` | 反查 ASIN 流量关键词、自然排名与广告排名 |
| `wenmai-sif-asin-summary` | 分析 ASIN 自然流量与广告流量结构 |
| `wenmai-sif-keyword-overview` | 查询关键词搜索量、ABA 排名与点击集中度 |
| `wenmai-sif-keyword-traffic` | 分析关键词竞争格局与 ASIN 流量份额 |

### Sorftime

| Skill | Description |
| --- | --- |
| `wenmai-sorftime-ali1688-product-search` | 多维度搜索 1688 货源商品 |
| `wenmai-sorftime-ali1688-product-search-from-image` | 根据图片搜索 1688 相同或相似商品 |
| `wenmai-sorftime-keyword-extends` | 围绕种子词扩展 Amazon 相关关键词 |
| `wenmai-sorftime-product-customers-say` | 汇总 Amazon 商品评论与买家反馈 |
| `wenmai-sorftime-product-detail` | 查询 Amazon 商品详情 |
| `wenmai-sorftime-product-ranking-trend-by-keyword` | 查询商品关键词排名趋势 |
| `wenmai-sorftime-product-report` | 获取 Amazon 产品分析报告 |
| `wenmai-sorftime-product-reviews` | 查询 Amazon 商品评论 |
| `wenmai-sorftime-product-search` | 实时搜索和筛选 Amazon 商品 |
| `wenmai-sorftime-product-search-from-history` | 按历史月份搜索和筛选 Amazon 商品 |
| `wenmai-sorftime-product-traffic-terms` | 反查 Amazon 商品流量关键词 |
| `wenmai-sorftime-product-trend` | 查询 Amazon 商品历史趋势 |
| `wenmai-sorftime-product-variations` | 查询 Amazon 商品父子变体 |

## Skill Structure

每个 Skill 都是独立、可安装的目录：

```text
skills/<skill-name>/
├── SKILL.md
├── skill-card.md
├── agents/
│   └── openai.yaml
├── references/
│   └── api.md
└── scripts/
    ├── _wenmai_api.py
    └── <endpoint>.py
```

`SKILL.md` 描述触发条件与工作流，`skill-card.md` 提供简要能力卡片，`references/api.md` 保存接口契约，`scripts/` 提供可直接执行的 Python 客户端。

## Requirements

- **Node.js** — 用于运行 `npx skills` 安装器。
- **Python 3.9+** — 所有 Skill 脚本仅使用 Python 标准库，无需安装第三方依赖。
- **环境变量** — 使用前必须设置 `WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`。

## Compatible Platforms

本项目遵循 [Agent Skills](https://agentskills.io) 开放标准：

| Platform | Status |
| --- | --- |
| 稳卖 Agent | Supported |
| Codex | Supported |
| Claude Code | Supported |
| Cursor | Supported |
| GitHub Copilot | Supported |
| OpenClaw | Supported |
| Gemini CLI | Supported |

## License

本项目基于 [MIT License](LICENSE) 开源。
