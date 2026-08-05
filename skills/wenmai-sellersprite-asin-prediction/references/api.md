# Wenmai SellerSprite `asin_prediction` API 参考

查询指定 ASIN 在 Amazon 对应市场的商品基础信息及销量与销售额预测数据。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/asin-prediction`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`asin_prediction`
- **脚本入口**：`scripts/asin_prediction.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN、MX、BR、AU、AE | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `asin` | string | 是 | Amazon ASIN；示例：B07Z82895W。 |

## 请求示例

```json
{
  "asin": "B08GHW4TBS",
  "marketplace": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `asinDetail` | object | asin明细。 |
| `asinDetail.asin` | string | Amazon ASIN；官方示例值：B00CFM8DI2。 |
| `asinDetail.title` | string | 商品标题；官方示例值：Boot Bananas Original Shoe Deodorizer。 |
| `asinDetail.brand` | string | 平台；官方示例值：Boot Bananas。 |
| `asinDetail.availableDate` | integer | 上架时间；官方示例值：1397001600000。 |
| `asinDetail.category` | string | 类目名称；官方示例值：Clothing, Shoes & Jewelry。 |
| `asinDetail.categoryId` | string | 类目id；官方示例值：7141123011。 |
| `asinDetail.imageUrl` | string | 图片URL；官方示例值：https://images-na.ssl-images-amazon.com/images/I/41AGxmiW-vL._AC_US600_.jpg。 |
| `asinDetail.rating` | number | 评分值；官方示例值：4.6。 |
| `asinDetail.ratings` | integer | 评分数；官方示例值：32004。 |
| `asinDetail.trends` | string | trends。 |
| `asinDetail.nodeIdPath` | string | 类目节点路径。 |
| `asinDetail.nodeLabelPath` | string | 类目名称路径。 |
| `asinDetail.subcategories[]` | array | 子类目列表。 |
| `asinDetail.subcategories[].rank` | integer | 排名。 |
| `asinDetail.subcategories[].code` | string | code。 |
| `asinDetail.subcategories[].label` | string | 分组标签。 |
| `dailyItemList[]` | array | 日销量预测明细。 |
| `dailyItemList[].date` | string | 日期；官方示例值：2026-01-01。 |
| `dailyItemList[].bsr` | integer | 每日预测明细的 BSR 排名；官方示例值：48614。 |
| `dailyItemList[].sales` | integer | 销量；官方示例值：14。 |
| `dailyItemList[].amount` | number | 销售额；官方示例值：200。 |
| `dailyItemList[].price` | number | 单价；官方示例值：20。 |
| `monthItemList[]` | array | 月销量预测明细。 |
| `monthItemList[].date` | string | 日期；官方示例值：2026-01。 |
| `monthItemList[].sales` | integer | 销量；官方示例值：14。 |
| `monthItemList[].amount` | number | 销售额；官方示例值：200。 |
| `monthItemList[].price` | number | 单价；官方示例值：20。 |

## 使用要点

- 必填字段：`marketplace`, `asin`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/asin-prediction" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","marketplace":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
