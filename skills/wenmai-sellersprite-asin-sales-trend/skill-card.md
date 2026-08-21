# SellerSprite ASIN 销量趋势

查询指定 Amazon 站点和 ASIN 的商品信息，以及父体、子体的月度销量、销售额和价格趋势。

- Provider: SellerSprite（卖家精灵）
- Platform: Amazon
- Operation: `asin_sales_trend`
- Endpoint: `POST /wmapi/v1/sellersprite/asin-sales-trend`
- Script: `scripts/asin_sales_trend.py`
- Authentication: `WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`，作为 `secret-key`
- Inputs: `marketplace`、`asin`
- Output: 原始标准 API JSON；业务数据位于 `data.asin` 和 `data.salesTrendPoints`
- API contract: [`references/api.md`](references/api.md)
- 使用指南: https://skill.wenmai-ai.com/wenmaiskills/use_guide.html
- API Key / 充值: https://agent.wenmai-ai.com/

本 Skill 只调用上述固定 Wenmai standard API，不接受动态端点，不补造缺失趋势值。
