# Wenmai Sorftime 亚马逊总结产品评论

固定调用一个 Wenmai standard API 端点，执行 `product_customers_say`。

- Operation: `product_customers_say`
- Endpoint: `POST /wmapi/v1/sorftime/product-customers-say`
- Script: `scripts/product_customers_say.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段为 asin, site
- Output: 原样 JSON 响应，可按响应字段生成可追溯摘要
- Limitations: 不接受动态端点；不补造缺失数据；不绕过上游额度、参数或站点限制
- API key / 充值: https://agent.wenmai-ai.com/
