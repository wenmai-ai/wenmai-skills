# YY数据Amazon 评论抓取

YY数据Amazon 评论抓取接口：按 1 个 ASIN 提交异步抓取任务，抓取最新评论（每页 10 条，1～10 页），可选整个 listing 全部变体或只抓所传 ASIN 这个变体；每条评论用 `review_asin`、`format_text` 标明所属变体。

固定调用 Wenmai YY数据评论监控 standard API 的 4 个端点，不接受动态端点或其他操作。

- Provider: YY数据
- Platform: Amazon（亚马逊）
- Operations: `yy_add_review_monitor_asins`、`yy_get_review_monitor_tasks`、`yy_get_monitor_asin_reviews`、`yy_get_review_crawl_count`
- Endpoints: `POST /wmapi/v1/yy/add-review-monitor-asins`、`/get-review-monitor-tasks`、`/get-monitor-asin-reviews`、`/get-review-crawl-count`
- Scripts: `scripts/crawl_reviews.py`（提交 → 轮询 → 取评论），以及每个端点一个单步脚本
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段、默认值和限制以 API 契约为准；一次只提交 1 个 ASIN
- Output: 原始 JSON 响应；摘要必须可追溯并映射到响应字段，同时保留 `requestId`、`aid`、`page_num`
- Limitations: 异步任务通常 1.5～2.5 分钟完成；按申请页数计费；不接受动态端点；不静默截断或补造数据
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API key / 充值: https://agent.wenmai-ai.com/
