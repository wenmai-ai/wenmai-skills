# Wenmai Sorftime 查延伸关键词

固定调用一个 Wenmai standard API 端点，执行 `keyword_extends`。

- Operation: `keyword_extends`
- Endpoint: `POST /wmapi/v1/sorftime/keyword-extends`
- Script: `scripts/keyword_extends.py`
- Authentication: `WENMAI_API_KEY`（兼容 `WENMAI_SECRET_KEY`）作为 `secret-key`
- Inputs: JSON 对象；必填字段为 keyword, keyword_support_site
- Output: 原样 JSON 响应，可按响应字段生成可追溯摘要
- Limitations: 不接受动态端点；不补造缺失数据；不绕过上游额度、参数或站点限制
- API key / 充值: https://agent.wenmai-ai.com/
