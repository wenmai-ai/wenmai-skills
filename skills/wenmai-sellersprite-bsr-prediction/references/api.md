# Wenmai SellerSprite `bsr_prediction` API 参考

根据 Amazon 指定市场下的一级类目节点和大类 BSR 排名，。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/bsr-prediction`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`bsr_prediction`
- **脚本入口**：`scripts/bsr_prediction.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN、MX、BR、AU、AE | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `bsr` | integer | 是 | 大类 BSR 排名；示例：1024。 |
| `categoryId` | string | 是 | 一级类目节点，查产品类目返回；示例：11260432011。 |

## 请求示例

```json
{
  "bsr": 1,
  "categoryId": "11260432011",
  "marketplace": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `marketplace` | string | Amazon 市场站点编码；官方示例值：US。 |
| `bsr` | integer | BSR 排名。 |
| `categoryLabel` | string | 类目名称；官方示例值：2685。 |
| `estDailySales` | integer | 预测日销量；官方示例值：99。 |
| `estMonthSales` | integer | 预测30天销量；官方示例值：2965。 |
| `categoryId` | string | 类目 ID。 |
| `itemList[]` | array | BSR 预测明细列表。 |
| `itemList[].bsr` | integer | 预测明细的 BSR 排名；官方示例值：1。 |
| `itemList[].estDailySales` | integer | 预测日销量；官方示例值：99。 |
| `itemList[].estMonthSales` | integer | 预测30天销量；官方示例值：2965。 |

## 使用要点

- 必填字段：`marketplace`, `bsr`, `categoryId`。
- 保留源文档字段名、类型和层级；数组字段以 `[]` 标识。
- 结果摘要必须保留到原始响应字段的映射，不推断缺失值。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 设置 `WENMAI_API_KEY` 或兼容的 `WENMAI_SECRET_KEY`，不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/ 充值。 |
| 参数错误 | 按请求表检查必填字段、字段类型、站点、日期和分页范围。 |
| HTTP、网络或超时错误 | 保留状态码和脱敏错误摘要，检查网关地址、网络和超时配置。 |
| 响应不是 JSON | 停止解析并报告响应格式错误，不把异常正文当作业务数据。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/bsr-prediction" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bsr":1,"categoryId":"11260432011","marketplace":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
