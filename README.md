# Wenmai Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-orange)](https://agentskills.io)
[![Skills](https://img.shields.io/badge/skills-56-brightgreen)](#skills-catalog)

**Wenmai Skills** 是面向跨境电商的数据型 AI Skill 集合，提供 56 个 API 驱动的原子能力，覆盖多平台商品与内容采集、Amazon 评论、JIIMORE、Keepa、卖家精灵（SellerSprite）和 SIF 等数据源。

本仓库遵循 [Agent Skills](https://agentskills.io) 开放标准，可用于稳卖 Agent、Codex、Claude Code、Cursor、GitHub Copilot 等支持 Agent Skills 的 AI 编程与智能体平台。

---

## Installation

当前仓库暂不支持通过 `npx skills add` 安装。请下载仓库，并把需要的完整 Skill 目录复制到 Agent 的 Skills 目录。Skill 脚本需要 Python 3.9 或更高版本，且仅依赖 Python 标准库，无需额外安装第三方包。

### 1. 下载仓库

```bash
git clone https://github.com/wenmai-ai/wenmai-skills.git
cd wenmai-skills
```

也可以在 GitHub 仓库页面选择 **Code → Download ZIP**，解压后进入仓库目录。

### 2. 让 Agent 代为安装（可选）

如果当前 Agent 支持联网、GitHub 下载和本地文件操作，也可以直接把安装任务交给 Agent。以下提示词可以直接复制使用。

安装单个 Skill：

```text
请从 GitHub 仓库 https://github.com/wenmai-ai/wenmai-skills 安装
skills/wenmai-sif-asin-keywords 到当前 Agent 的标准用户级 Skills 目录。
请安装完整目录，保留 SKILL.md、skill-card.md、agents、references 和 scripts。
如果目标目录已存在同名 Skill，请不要直接覆盖，先告诉我当前状态并询问是否替换。
安装后请验证 SKILL.md 和配套文件均存在，并告诉我该 Skill 何时可以使用。
```

安装全部 Skills：

```text
请从 GitHub 仓库 https://github.com/wenmai-ai/wenmai-skills 读取 skills/ 目录，
列出所有 wenmai-* Skill 及当前安装状态，然后把尚未安装的 Skill
完整安装到当前 Agent 的标准用户级 Skills 目录。
不要只复制 SKILL.md；必须同时保留 skill-card.md、agents、references 和 scripts。
遇到已存在的同名 Skill 时不要直接覆盖，请先汇总冲突并询问我如何处理。
安装后请验证已安装数量和目录完整性，并告诉我这些 Skill 何时可以使用。
```

如果 Agent 支持显式调用安装 Skill，也可以在提示词开头加上“使用 `$skill-installer`”。Agent 通常会把 Skill 安装到自己的标准目录；以 Codex 为例，目标为 `$CODEX_HOME/skills`，未设置时为 `~/.codex/skills`。新安装的 Skill 通常从下一轮任务开始可用。

### 3. 确认安装目录

Codex 默认从以下目录加载用户级 Skills：

```text
${CODEX_HOME:-$HOME/.codex}/skills
```

未设置 `CODEX_HOME` 时，实际目录为 `~/.codex/skills`。其他 Agent 的安装目录可能不同，请将下方命令中的目标目录替换为对应 Agent 文档指定的 Skills 目录。

### 4. 手动安装单个 Skill

下面以安装 `wenmai-sif-asin-keywords` 到 Codex 为例：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/wenmai-sif-asin-keywords "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装时必须复制完整 Skill 目录，不能只复制 `SKILL.md`。完整目录还包含接口参考、执行脚本和 Agent 元数据：

```text
wenmai-sif-asin-keywords/
├── SKILL.md
├── skill-card.md
├── agents/
├── references/
└── scripts/
```

### 5. 手动安装全部 Skills

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/wenmai-* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

如果目标目录中已存在同名 Skill，请先备份旧目录，再用新目录完整替换，避免新旧脚本或参考文件混用。

### 6. 验证安装

确认 `SKILL.md` 和配套文件已复制成功：

```bash
test -f "${CODEX_HOME:-$HOME/.codex}/skills/wenmai-sif-asin-keywords/SKILL.md" \
  && echo "Skill installed"
```

安装后新建一次 Agent 任务或重新启动 Agent，使新 Skill 被加载。按照 `SKILL.md` 的触发描述提出需求；也可以在支持显式调用的 Agent 中直接指定 Skill 名称。

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
