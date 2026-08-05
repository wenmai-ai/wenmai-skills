# Wenmai Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-orange)](https://agentskills.io)
[![Skills](https://img.shields.io/badge/skills-189-brightgreen)](#skills-catalog)
[![npm](https://img.shields.io/npm/v/%40wenmai-ai%2Fwenmai-skills.svg)](https://www.npmjs.com/package/@wenmai-ai/wenmai-skills)

**Wenmai Skills** 是面向跨境电商的数据型 AI Skill 集合，提供 189 个 API 驱动的原子能力，覆盖多平台商品与内容采集、Amazon 评论、JIIMORE、Keepa、卖家精灵（SellerSprite）、SIF 和 Sorftime 等数据源。

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

`@wenmai-ai/wenmai-skills` 是包含全部 Skills 的 npm 聚合包：

```bash
npm install @wenmai-ai/wenmai-skills
```

npm 会把完整集合下载到 `node_modules/@wenmai-ai/wenmai-skills`，但不会自动注册到 Agent。可以继续使用 Skills CLI 从本地包中安装指定 Skill：

```bash
npx skills add ./node_modules/@wenmai-ai/wenmai-skills \
  --skill wenmai-sif-asin-keywords \
  -g -a codex -y
```

### Install for Wenmai Agent

安装器要求显式指定目标 Agent；不传 `--agent` 时不会执行安装。

更新最新的版本的Wenmai Agent。

安装全部 Skills：

```bash
npx @wenmai-ai/wenmai-skills install --agent wenmai-agent
```

安装单个 Skill：

```bash
npx @wenmai-ai/wenmai-skills install wenmai-sif-asin-keywords --agent wenmai-agent
```

更新已经安装的 Skills：

```bash
npx @wenmai-ai/wenmai-skills install --agent wenmai-agent --force
```

安装器会自动识别系统并使用以下目录：

- macOS：`~/Library/Application Support/Wenmai Agent/wenmai-cli/skills`
- Windows：`%APPDATA%\wenmaiAgent\wenmai-cli\skills`

### Install for Codex with the npm package

安装全部 Skills：

```bash
npx @wenmai-ai/wenmai-skills install --agent codex
```

安装单个 Skill：

```bash
npx @wenmai-ai/wenmai-skills install wenmai-sif-asin-keywords --agent codex
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

以下按数据源完整列出当前 189 个 Skill。

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
| `wenmai-keepa-product-history` | Amazon 平台：查询价格、BSR、Buy Box、评分与评论等历史走势 |
| `wenmai-keepa-product-search` | Amazon 平台：按关键词搜索 Keepa 商品池 |

### JIIMORE

| Skill | Description |
| --- | --- |
| `wenmai-jiimore-expand-aba-keywords-by-keyword` | Amazon 平台：按种子关键词扩展 Amazon ABA 关键词 |
| `wenmai-jiimore-find-aba-asins-by-keyword` | Amazon 平台：按关键词查询 ABA 关联商品与 ASIN |
| `wenmai-jiimore-find-asins-batch` | Amazon 平台：批量查询 Amazon ASIN 摘要信息 |
| `wenmai-jiimore-find-asins-by-keyword` | Amazon 平台：按关键词搜索 Amazon 商品与 ASIN |
| `wenmai-jiimore-find-niches-by-asin` | Amazon 平台：按 ASIN 查找所属或相关细分市场 |
| `wenmai-jiimore-find-niches-by-keyword` | Amazon 平台：按关键词查找相关细分市场 |
| `wenmai-jiimore-find-same-niche-asins` | Amazon 平台：查询与指定 ASIN 同细分市场的商品 |
| `wenmai-jiimore-find-similar-asins` | Amazon 平台：基于 ABA 关系查询相似 ASIN |
| `wenmai-jiimore-get-asin-details` | Amazon 平台：查询一个或多个 Amazon ASIN 的商品详情 |
| `wenmai-jiimore-get-keyword-rankings` | Amazon 平台：反查 ASIN 的关联关键词与排名 |
| `wenmai-jiimore-get-niche-asins` | Amazon 平台：查询指定细分市场中的商品与 ASIN |
| `wenmai-jiimore-get-niche-details` | Amazon 平台：查询 Amazon 细分市场详情与指标 |
| `wenmai-jiimore-get-niche-keywords` | Amazon 平台：查询指定细分市场的关键词池 |
| `wenmai-jiimore-search-aba-keywords` | Amazon 平台：按 ASIN 查询 ABA 关键词 |
| `wenmai-jiimore-search-keywords-batch` | Amazon 平台：批量查询 Amazon 关键词指标 |
| `wenmai-jiimore-search-keywords-by-asin` | Amazon 平台：按 ASIN 查询关联关键词 |
| `wenmai-jiimore-search-keywords-by-keyword` | Amazon 平台：围绕种子词扩展 Amazon 相关关键词 |

### SellerSprite（卖家精灵）

| Skill | Description |
| --- | --- |
| `wenmai-sellersprite-aba-research-monthly` | Amazon 平台：用于在指定 Amazon 站点和时间点（按月） |
| `wenmai-sellersprite-aba-research-trend` | Amazon 平台：ABA选品-关键词的趋势数据，包含：ABA排名和搜索量 |
| `wenmai-sellersprite-aba-research-weekly` | Amazon 平台：用于在指定 Amazon 站点和时间点（按周） |
| `wenmai-sellersprite-asin-coupon-trend` | Amazon 平台：查询指定 ASIN 在 Amazon 指定市场下的优惠价格信息 |
| `wenmai-sellersprite-asin-detail` | Amazon 平台：ASIN 商品详情接口，用于查询单个商品的标题、品牌、类目、价格、销量、收入、评分、BSR 及接口支持的完整指标 |
| `wenmai-sellersprite-asin-detail-with-coupon-trend` | Amazon 平台：ASIN 商品详情与 Coupon 趋势接口，用于查询指定 Amazon 市场中的商品完整信息及优惠券变化数据 |
| `wenmai-sellersprite-asin-prediction` | Amazon 平台：查询指定 ASIN 在 Amazon 对应市场的商品基础信息及销量与销售额预测数据 |
| `wenmai-sellersprite-bsr-prediction` | Amazon 平台：根据 Amazon 指定市场下的一级类目节点和大类 BSR 排名 |
| `wenmai-sellersprite-competitor` | Amazon 平台：卖家精灵竞品查询接口，用于按 ASIN、品牌、卖家、类目、站点、月份、关键词或变体条件查找 Amazon 竞品及其指标 |
| `wenmai-sellersprite-google-trend` | Amazon 平台：Google Trends 关键词趋势接口，用于查询指定关键词在目标市场和时间范围内的搜索热度变化 |
| `wenmai-sellersprite-keepa-info` | Amazon 平台：获取指定 Amazon ASIN 的完整商品画像及多维度历史趋势数据(不含有销量数据) |
| `wenmai-sellersprite-keyword-miner` | Amazon 平台：高级关键词流量与竞争分析工具（卖家决策级） |
| `wenmai-sellersprite-keyword-order` | Amazon 平台：基于 ASIN 的关键词反查工具，用于分析某个或多个 ASIN |
| `wenmai-sellersprite-keyword-research` | Amazon 平台：专业级 Amazon 关键词市场与选品分析工具 |
| `wenmai-sellersprite-keyword-research-trends` | Amazon 平台：关键词选品-关键词的趋势数据，包含：搜索量，购买量，购买率，同比增长率，环比增长率，三个月增长率 |
| `wenmai-sellersprite-market-brand-concentration` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的品牌集中度情况 |
| `wenmai-sellersprite-market-ebc-distribution` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的A+视频分布 |
| `wenmai-sellersprite-market-listing-date-distribution` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的商品上架时间分布与新品接受度 |
| `wenmai-sellersprite-market-listing-trend-distribution` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的商品上架时间分布与生命周期 |
| `wenmai-sellersprite-market-price-distribution` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的商品价格区间分布与市场定价结构 |
| `wenmai-sellersprite-market-product-concentration` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的商品集中度情况 |
| `wenmai-sellersprite-market-product-demand-trend` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的商品需求趋势情况 |
| `wenmai-sellersprite-market-rating-distribution` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的商品评分值分布与市场成熟度评估 |
| `wenmai-sellersprite-market-ratings-count-distribution` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的商品评分数区间分布与新品进入难度 |
| `wenmai-sellersprite-market-research` | Amazon 平台：类目市场研究接口，用于分析市场规模、商品数量、销量、销售额、均价、评分、BSR、品牌与卖家集中度、新品占比和配送结构 |
| `wenmai-sellersprite-market-seller-concentration` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的卖家集中度情况 |
| `wenmai-sellersprite-market-seller-country-distribution` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的卖家所属地分布情况 |
| `wenmai-sellersprite-market-seller-type-concentration` | Amazon 平台：用于分析指定 Amazon 市场类目节点下的卖家发货类型竞争情况 |
| `wenmai-sellersprite-market-statistics` | Amazon 平台：类目节点统计接口，用于获取指定节点的 Top N 市场汇总、新品指标、平均销量、销售额、价格、评分和 BSR |
| `wenmai-sellersprite-product-node` | Amazon 平台：查询 Amazon 产品类目信息的工具 |
| `wenmai-sellersprite-product-search` | Amazon 平台：商品搜索与商品池筛选接口，可按关键词、类目、销量、销售额、BSR、价格、评分、卖家、品牌、徽章和配送方式等条件筛选商品 |
| `wenmai-sellersprite-review` | Amazon 平台：评论接口，用于按 ASIN 查询评论标题、正文、评分、评论人、评论时间及接口支持的评价数据 |
| `wenmai-sellersprite-traffic-extend` | Amazon 平台：用于在指定 Amazon 站点中，根据 ASIN、时间范围及多维筛选条件 |
| `wenmai-sellersprite-traffic-keyword` | Amazon 平台：ASIN 流量关键词接口，用于查询关键词列表、自然位与广告位、搜索量、购买率、流量占比、关键词类型、转化类型和排名位置 |
| `wenmai-sellersprite-traffic-keyword-stat` | Amazon 平台：ASIN 流量关键词概览统计接口，用于汇总自然词、广告词、流量词和转化词等关键词结构指标 |
| `wenmai-sellersprite-traffic-listing` | Amazon 平台：关联商品接口，用于查询指定 ASIN 在站内关联的 Listing，分析商品间的竞品和流量关联关系 |
| `wenmai-sellersprite-traffic-listing-stat` | Amazon 平台：用于分析 Amazon ASIN 的流量来源结构，包括免费流量、付费流量和关联类型分布 |
| `wenmai-sellersprite-traffic-source` | Amazon 平台：流量来源分析接口，用于从 ASIN 或关键词维度查看流量关键词结构和接口支持的来源指标 |

### SIF 搜索智能

| Skill | Description |
| --- | --- |
| `wenmai-sif-ads-get-ad-group-keyword-breakdown` | Amazon 平台：查询单个广告组在指定周的关键词明细，包含每个关键词的流量占比以及该关键词在哪些 ASIN 上展示 |
| `wenmai-sif-ads-get-ad-group-traffic-trend` | Amazon 平台：查询单个广告组从创建至今的完整历史流量趋势，可附带用户选中窗口的上下文便于对比定位 |
| `wenmai-sif-ads-get-asin-ad-feature-profile` | Amazon 平台：ads_get_asin_ad_window_feature_profile 的兼容别名，执行逻辑完全相同 |
| `wenmai-sif-ads-get-asin-ad-historical-feature-profile` | Amazon 平台：基于 ASIN 的历史全量广告数据，生成长期广告特征画像，描述投放节奏、渠道组合、集中度和增长轨迹 |
| `wenmai-sif-ads-get-asin-ad-structure` | Amazon 平台：查询某 ASIN 的广告结构总览，统计历史全量范围内各广告类型的 campaign 数量 |
| `wenmai-sif-ads-get-asin-ad-traffic-trend` | Amazon 平台：查询某 ASIN 历史全量的广告流量趋势，按 SP/SB/SBV 三个渠道分别输出曝光量时序 |
| `wenmai-sif-ads-get-asin-ad-window-feature-profile` | Amazon 平台：基于 ASIN 广告数据，生成指定时间窗口内的广告特征画像，描述窗口期内的结构、集中度、投放节奏和稳定性 |
| `wenmai-sif-ads-get-asin-campaign-changes` | Amazon 平台：查询某 ASIN 在历史各周内新上线的 campaign 变更事件，即 campaign_created 事件列表 |
| `wenmai-sif-ads-get-asin-campaign-contribution-overview` | Amazon 平台：基于曝光得分，查询某 ASIN 在指定时间窗口内各 campaign 的贡献总览，按贡献从高到低排序 |
| `wenmai-sif-ads-get-campaign-contribution-breakdown` | Amazon 平台：查询某 campaign 在单个自然周内的贡献明细，支持按 keyword 或 ad_group 维度拆解 |
| `wenmai-sif-ads-get-campaign-structure` | Amazon 平台：查询单个 campaign 的历史广告组结构，列出该 campaign 下所有广告组的详情 |
| `wenmai-sif-ads-get-campaign-traffic-trend` | Amazon 平台：查询单个 campaign 从创建至今的全生命周期流量趋势，并附带广告组创建事件作为结构性上下文 |
| `wenmai-sif-analyze-traffic-anomaly` | Amazon 平台：所有流量变化分析的主入口工具 |
| `wenmai-sif-asin-keywords` | Amazon 平台：ASIN 反查关键词接口，用于获取流量关键词、自然排名、广告排名、关键词贡献变化、排名差距以及上升或下降关键词 |
| `wenmai-sif-asin-summary` | Amazon 平台：ASIN 流量概览接口，用于汇总 Listing 的自然与广告流量占比、SP／SB／SBV 渠道结构、推荐流量来源和整体流量健康度 |
| `wenmai-sif-keyword-overview` | Amazon 平台：关键词需求概览接口，用于查询搜索量历史、ABA 排名历史、Top 3 点击或转化集中度、市场需求规模和关键词趋势 |
| `wenmai-sif-keyword-traffic` | Amazon 平台：关键词流量与竞争分析接口，用于查看头部 ASIN 的流量份额、自然／SP／SB／SBV 占比、集中度、竞争位置和关键词机会 |
| `wenmai-sif-market-get-keyword-demand` | Amazon 平台：需求判断层——回答'这个词的需求处于什么生命周期阶段，是在增长、在萎缩还是只是季节性低谷，以及现在是进场、加速、收割还是收缩的时机' |
| `wenmai-sif-market-get-keyword-root-trend` | Amazon 平台：需求边界层——回答'这个词背后的整个市场有多大，买家需求是集中在精确词上，还是分散在大量长尾变体词里' |
| `wenmai-sif-ops-get-asin-sales-list` | Amazon 平台：以列表视图查询一个或多个 ASIN 的销量数据，返回各变体的销量、价格、属性及月度趋势迷你图 |
| `wenmai-sif-ops-get-asin-sales-trend` | Amazon 平台：查看 ASIN Listing 下各变体的月度销量历史趋势，用于分析销量走势和季节性规律 |
| `wenmai-sif-ops-get-asin-traffic-trend` | Amazon 平台：查看 ASIN 的流量趋势时间序列，按周期返回总流量分数及自然/广告渠道拆解 |
| `wenmai-sif-ops-get-asin-traffic-trend-detail` | Amazon 平台：查看 ASIN 在指定时间窗口内的关键词级流量明细，按关键词分页返回各渠道排名与分数拆解 |
| `wenmai-sif-ops-get-listing-keyword-distribution` | Amazon 平台：查看各变体的关键词数量分布，返回每个变体在自然流量、SP、SB、SBV 各渠道中覆盖的流量词数量 |
| `wenmai-sif-ops-get-listing-traffic-structure` | Amazon 平台：查看 Listing 内各变体的流量结构拆解，返回每个变体在自然流量、SP、SB、SBV 渠道中各自的分数与占比 |
| `wenmai-sif-sif-catalog` | Amazon 平台：返回 SIF 可用接口的分类目录 |

### Sorftime

| Skill | Description |
| --- | --- |
| `wenmai-sorftime-ali1688-product-request` | 1688 平台产品详情查询 |
| `wenmai-sorftime-ali1688-product-search` | 1688 平台产品多维度搜索 |
| `wenmai-sorftime-ali1688-product-search-from-image` | 1688 平台以图搜产品 |
| `wenmai-sorftime-ali1688-product-variations` | 1688 平台产品SKU数据查询 |
| `wenmai-sorftime-ali1688-similar-product` | 1688 平台查询货源 |
| `wenmai-sorftime-category-keywords` | Amazon 平台：类目核心关键词 |
| `wenmai-sorftime-category-name-search` | Amazon 平台：类目名称搜索 |
| `wenmai-sorftime-category-report` | Amazon 平台：类目实时市场报告 |
| `wenmai-sorftime-category-report-from-history` | Amazon 平台：类目历史市场报告 |
| `wenmai-sorftime-category-search-from-product-name` | Amazon 平台：按产品名称搜类目 |
| `wenmai-sorftime-category-search-from-top-node` | Amazon 平台：查大类下的细分类目市场 |
| `wenmai-sorftime-category-tree` | Amazon 平台：类目树查询 |
| `wenmai-sorftime-category-trend` | Amazon 平台：类目市场趋势 |
| `wenmai-sorftime-change-favorite-keyword` | Amazon 平台：移动收藏关键词 |
| `wenmai-sorftime-competitor-product-keywords` | Amazon 平台：竞品关键词分析 |
| `wenmai-sorftime-del-favorite-keyword` | Amazon 平台：删除收藏关键词 |
| `wenmai-sorftime-favorite-keyword` | Amazon 平台：收藏关键词 |
| `wenmai-sorftime-get-favorite-keyword` | Amazon 平台：查询收藏关键词 |
| `wenmai-sorftime-get-favorite-keyword-dict` | Amazon 平台：查询收藏夹列表 |
| `wenmai-sorftime-keyword-detail` | Amazon 平台：关键词详情 |
| `wenmai-sorftime-keyword-extends` | Amazon 平台：查延伸关键词 |
| `wenmai-sorftime-keyword-list` | Amazon 平台：实时热搜关键词榜 |
| `wenmai-sorftime-keyword-list-from-history` | Amazon 平台：历史热搜关键词榜 |
| `wenmai-sorftime-keyword-search-results` | Amazon 平台：关键词搜索结果 |
| `wenmai-sorftime-keyword-trend` | Amazon 平台：关键词历史趋势 |
| `wenmai-sorftime-potential-product` | Amazon 平台：潜力产品搜索 |
| `wenmai-sorftime-product-customers-say` | Amazon 平台：总结产品评论 |
| `wenmai-sorftime-product-detail` | Amazon 平台：产品详情 |
| `wenmai-sorftime-product-ranking-trend-by-keyword` | Amazon 平台：产品关键词排名趋势 |
| `wenmai-sorftime-product-report` | Amazon 平台：产品分析报告 |
| `wenmai-sorftime-product-reviews` | Amazon 平台：产品评论 |
| `wenmai-sorftime-product-search` | Amazon 平台：选产品（实时） |
| `wenmai-sorftime-product-search-from-history` | Amazon 平台：选产品（历史） |
| `wenmai-sorftime-product-traffic-terms` | Amazon 平台：产品流量词反查 |
| `wenmai-sorftime-product-trend` | Amazon 平台：产品历史趋势 |
| `wenmai-sorftime-product-variations` | Amazon 平台：产品变体查询 |
| `wenmai-sorftime-search-categories-broadly` | Amazon 平台：细分类目（品类）市场 |
| `wenmai-sorftime-shopee-category-request` | Shopee 平台：类目Best Seller查询 |
| `wenmai-sorftime-shopee-category-search-from-name` | Shopee 平台：类目名称搜索 |
| `wenmai-sorftime-shopee-category-trend` | Shopee 平台：类目市场趋势 |
| `wenmai-sorftime-shopee-change-favorite-keyword` | Shopee 平台：移动收藏关键词 |
| `wenmai-sorftime-shopee-del-favorite-keyword` | Shopee 平台：删除收藏关键词 |
| `wenmai-sorftime-shopee-favorite-keyword` | Shopee 平台：收藏关键词 |
| `wenmai-sorftime-shopee-get-favorite-keyword` | Shopee 平台：查询收藏关键词 |
| `wenmai-sorftime-shopee-get-favorite-keyword-dict` | Shopee 平台：查询收藏夹列表 |
| `wenmai-sorftime-shopee-keyword-relation-results` | Shopee 平台：关键词关联产品 |
| `wenmai-sorftime-shopee-keyword-search` | Shopee 平台：热搜关键词榜单 |
| `wenmai-sorftime-shopee-product-request` | Shopee 平台：产品详情 |
| `wenmai-sorftime-shopee-product-search` | Shopee 平台：选产品 |
| `wenmai-sorftime-shopee-product-search-from-name` | Shopee 平台：按名称搜产品 |
| `wenmai-sorftime-shopee-product-trend` | Shopee 平台：产品历史趋势 |
| `wenmai-sorftime-shopee-shop-request` | Shopee 平台：店铺详情 |
| `wenmai-sorftime-similar-product-feature` | Amazon 平台：相似产品特征 |
| `wenmai-sorftime-temu-category-request` | Temu 平台：类目Best Seller查询 |
| `wenmai-sorftime-temu-category-search` | Temu 平台：选类目 |
| `wenmai-sorftime-temu-category-search-from-name` | Temu 平台：按产品名称搜类目 |
| `wenmai-sorftime-temu-product-request` | Temu 平台：产品详情 |
| `wenmai-sorftime-temu-product-search` | Temu 平台：选产品 |
| `wenmai-sorftime-temu-product-search-from-name` | Temu 平台：按名称搜产品 |
| `wenmai-sorftime-temu-product-trend` | Temu 平台：产品历史趋势 |
| `wenmai-sorftime-temu-shop-request` | Temu 平台：店铺详情 |
| `wenmai-sorftime-tiktok-author` | TikTok 平台：达人搜索 |
| `wenmai-sorftime-tiktok-category-name-search` | TikTok 平台：按产品名称搜类目 |
| `wenmai-sorftime-tiktok-category-report` | TikTok 平台：类目数据报告 |
| `wenmai-sorftime-tiktok-category-search-from-name` | TikTok 平台：按名称搜索 TikTok 类目 |
| `wenmai-sorftime-tiktok-product-detail` | TikTok 平台：产品详情 |
| `wenmai-sorftime-tiktok-product-trend` | TikTok 平台：产品历史趋势 |
| `wenmai-sorftime-tiktok-product-video` | TikTok 平台：产品带货视频 |
| `wenmai-sorftime-tiktok-product-video-author` | TikTok 平台：产品带货达人 |
| `wenmai-sorftime-tiktok-similar-product` | TikTok 平台：相似产品查询 |
| `wenmai-sorftime-walmart-category-report-by-node-id` | Walmart 平台：类目实时销量报告 |
| `wenmai-sorftime-walmart-change-favorite-keyword` | Walmart 平台：移动收藏关键词 |
| `wenmai-sorftime-walmart-del-favorite-keyword` | Walmart 平台：删除收藏关键词 |
| `wenmai-sorftime-walmart-favorite-keyword` | Walmart 平台：收藏关键词 |
| `wenmai-sorftime-walmart-get-favorite-keyword` | Walmart 平台：查询收藏关键词 |
| `wenmai-sorftime-walmart-get-favorite-keyword-dict` | Walmart 平台：查询收藏夹列表 |
| `wenmai-sorftime-walmart-keyword-detail` | Walmart 平台：关键词详情 |
| `wenmai-sorftime-walmart-keyword-extends` | Walmart 平台：关键词延伸 |
| `wenmai-sorftime-walmart-keyword-list` | Walmart 平台：实时热搜关键词列表 |
| `wenmai-sorftime-walmart-keyword-search-from-name` | Walmart 平台：按名称查询 Walmart 热搜关键词 |
| `wenmai-sorftime-walmart-keyword-search-results` | Walmart 平台：关键词搜索结果 |
| `wenmai-sorftime-walmart-product-detail-by-product-id` | Walmart 平台：产品详情 |
| `wenmai-sorftime-walmart-product-traffic-terms` | Walmart 平台：产品流量词反查 |
| `wenmai-sorftime-walmart-product-trend-by-product-id` | Walmart 平台：产品历史趋势 |
| `wenmai-sorftime-walmart-product-variation-sales-by-product-id` | Walmart 平台：产品变体查询 |

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
