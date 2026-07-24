# Wenmai Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-orange)](https://agentskills.io)
[![Skills](https://img.shields.io/badge/skills-82-brightgreen)](#skills-catalog)

**Wenmai Skills** 是面向跨境电商的数据型 AI Skill 集合，提供 82 个 API 驱动的原子能力，覆盖多平台商品与内容采集、Amazon 评论、Keepa、卖家精灵（SellerSprite）、Sorftime、SIF 和西柚洞察（XYDC）等数据源。

本仓库遵循 [Agent Skills](https://agentskills.io) 开放标准，可用于稳卖Agent、 Codex、Claude Code、Cursor、GitHub Copilot 等支持 Agent Skills 的 AI 编程与智能体平台。

---

## Installation

请先安装 [Node.js](https://nodejs.org/)（用于运行 `npx`）。

### 安装全部 Skills

```bash
npx skills add wenmai-ai/wenmai-skills
```

### 安装指定 Skills

```bash
npx skills add wenmai-ai/wenmai-skills --skill wenmai-amazon-reviews wenmai-sif-asin-keywords
```

### 查看可用 Skills

```bash
npx skills add wenmai-ai/wenmai-skills --list
```

### 安装到指定 Agent

```bash
npx skills add wenmai-ai/wenmai-skills --agent codex
npx skills add wenmai-ai/wenmai-skills --agent claude-code
npx skills add wenmai-ai/wenmai-skills --agent cursor
```

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
| `wenmai-alpha-1688-wholesale-scraper` | 采集 1688 批发商品、供应商、MOQ、价格与销量 |
| `wenmai-alpha-alibaba-products-scraper` | 采集 Alibaba 国际站商品与供应商信息 |
| `wenmai-alpha-aliexpress-product-scraper` | 采集 AliExpress 商品、价格与跨境竞品信息 |
| `wenmai-alpha-amazon-product-details-scraper` | 采集 Amazon 商品详情与 Listing 信息 |
| `wenmai-alpha-amazon-reviews-extractor` | 采集 Amazon 商品评论 |
| `wenmai-alpha-bestbuy-scraper` | 采集 Best Buy 商品信息 |
| `wenmai-alpha-bol-com-scraper` | 采集 Bol.com 商品信息 |
| `wenmai-alpha-coupang-listings-scraper` | 采集 Coupang 商品 Listing |
| `wenmai-alpha-dealwatch-scraper` | 采集 DealWatch 零售促销与商品监控数据 |
| `wenmai-alpha-douyin-product-search-scraper` | 搜索并采集抖音商品 |
| `wenmai-alpha-etsy-scraper` | 采集 Etsy 手作与小众商品 |
| `wenmai-alpha-facebook-ads-scraper` | 采集 Facebook / Meta 广告库素材 |
| `wenmai-alpha-free-amazon-product-scraper` | 快速采集公开 Amazon 商品数据 |
| `wenmai-alpha-google-search-results-serp-scraper` | 采集 Google SERP 搜索结果 |
| `wenmai-alpha-google-search-scraper` | 采集 Google 搜索结果 |
| `wenmai-alpha-google-trends-scraper` | 采集 Google Trends 趋势数据 |
| `wenmai-alpha-instagram-scraper` | 采集 Instagram 账号、话题与内容 |
| `wenmai-alpha-jd-com-product-scraper` | 采集京东商品搜索与详情数据 |
| `wenmai-alpha-jumia-product-search-scraper` | 搜索并采集 Jumia 商品 |
| `wenmai-alpha-kaufland-fast-product-scraper` | 快速采集 Kaufland 商品与类目数据 |
| `wenmai-alpha-lazada-scraper` | 采集 Lazada 商品数据 |
| `wenmai-alpha-lowes-product-lookup` | 查询 Lowe's 商品信息 |
| `wenmai-alpha-mercadolibre-scraper` | 采集 Mercado Libre 商品、卖家、评论与问答 |
| `wenmai-alpha-newegg-product-scraper` | 采集 Newegg 商品信息 |
| `wenmai-alpha-noon-com-scraper` | 采集 Noon 中东电商商品 |
| `wenmai-alpha-ozon-scraper-pro` | 采集 Ozon 商品池数据 |
| `wenmai-alpha-rakuten-japan-scraper` | 采集日本乐天商品信息 |
| `wenmai-alpha-reddit-scraper-search-fast` | 快速搜索 Reddit 帖子、评论与舆情 |
| `wenmai-alpha-shein-scraper` | 采集 SHEIN 商品信息 |
| `wenmai-alpha-shopee-scraper` | 采集 Shopee 商品与店铺信息 |
| `wenmai-alpha-shopify-product-scraper` | 采集 Shopify 品牌站商品 |
| `wenmai-alpha-taobao-tmall-product-scraper` | 采集淘宝与天猫商品信息 |
| `wenmai-alpha-target-scraper` | 采集 Target 商品搜索结果 |
| `wenmai-alpha-temu-products-scraper` | 采集 Temu 商品池数据 |
| `wenmai-alpha-tiktok-scraper` | 采集 TikTok 视频、账号、话题与趋势 |
| `wenmai-alpha-trendyol-scraper` | 采集 Trendyol 商品信息 |
| `wenmai-alpha-tweet-scraper` | 采集 X / Twitter 推文、账号与列表 |
| `wenmai-alpha-walmart-fast-product-scraper` | 快速采集 Walmart 商品信息 |
| `wenmai-alpha-walmart-reviews-scraper` | 采集 Walmart 商品评论 |
| `wenmai-alpha-wayfair-listings-scraper` | 采集 Wayfair 家居商品 Listing |
| `wenmai-alpha-wildberries-products-search-scraper` | 搜索并采集 Wildberries 商品 |
| `wenmai-alpha-xiaohongshu-pro-scraper` | 采集小红书笔记、关键词与内容趋势 |
| `wenmai-alpha-youtube-comments-scraper` | 采集 YouTube 视频评论 |
| `wenmai-alpha-youtube-scraper` | 采集 YouTube 视频、频道与搜索结果 |
| `wenmai-alpha-zalando-scraper` | 采集 Zalando 时尚商品 |

### Amazon 评论与 Keepa

| Skill | Description |
| --- | --- |
| `wenmai-amazon-reviews` | 按 ASIN 获取 Amazon 买家评论，用于 VOC 与竞品研究 |
| `wenmai-keepa-product-detail` | 按销量排名、商品类型等条件筛选 Amazon ASIN 商品池 |
| `wenmai-keepa-product-history` | 查询价格、BSR、Buy Box、评分与评论等历史走势 |
| `wenmai-keepa-product-search` | 按关键词搜索 Keepa 商品池 |

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

### XYDC（西柚洞察）

| Skill | Description |
| --- | --- |
| `wenmai-xydc-asin-ad-change-trends` | 查询 ASIN 广告信息变动日趋势 |
| `wenmai-xydc-asin-bsr-trends` | 查询 ASIN BSR 排名日趋势 |
| `wenmai-xydc-asin-info` | 查询 ASIN 商品信息 |
| `wenmai-xydc-asin-info-trends` | 查询 ASIN 商品信息日趋势 |
| `wenmai-xydc-asin-keyword-rank-hourly` | 查询 ASIN 关键词小时排名趋势 |
| `wenmai-xydc-asin-keyword-rank-trends` | 查询 ASIN 关键词日排名趋势 |
| `wenmai-xydc-asin-keyword-traffic-trends` | 查询 ASIN 关键词流量日趋势 |
| `wenmai-xydc-asin-keywords` | 反查 ASIN 最近天数的关键词列表 |
| `wenmai-xydc-asin-keywords-monthly` | 反查 ASIN 月度关键词列表 |
| `wenmai-xydc-asin-order-trends` | 查询 ASIN 月度订单量趋势 |
| `wenmai-xydc-asin-traffic` | 查询 ASIN 流量得分 |
| `wenmai-xydc-asin-traffic-trends` | 查询 ASIN 流量得分日趋势 |
| `wenmai-xydc-asin-variations` | 查询 ASIN 变体关系 |
| `wenmai-xydc-keyword-aba-trends` | 查询关键词 ABA 周趋势 |
| `wenmai-xydc-keyword-analysis-monthly` | 查询关键词月度 ASIN 分析列表 |
| `wenmai-xydc-keyword-asin-analysis` | 查询关键词最近天数的 ASIN 分析列表 |
| `wenmai-xydc-keyword-info` | 查询关键词最近一周的基础信息 |

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

## License

[MIT](LICENSE)
