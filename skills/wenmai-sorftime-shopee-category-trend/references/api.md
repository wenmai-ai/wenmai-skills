# Wenmai Sorftime `shopee_category_trend` API 参考

类目市场趋势。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-category-trend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`shopee_category_trend`
- **脚本入口**：`scripts/shopee_category_trend.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `node_id` | String | 否 | 要查询的类目节点 ID。 |
| `trend_index` | String；可选值："MonthlySalesVolume"、"MonthlySalesAmount"、"AveragePrice"、"AverageReviewCount"、"AverageStarRating"、"SellerCount"、"AverageVariantCount"、"BrandCount"、"FlagshipStoreCount"、"FlagshipStoreRatio"、"FlagshipStoreMonthlySales"、"FlagshipStoreMonthlySalesRatio"、"PreferredStoreCount"、"PreferredStoreRatio"、"PreferredStoreMonthlySales"、"PreferredStoreMonthlySalesRatio"、"OrdinaryStoreCount"、"OrdinaryStoreRatio"、"OrdinaryStoreMonthlySales"、"OrdinaryStoreMonthlySalesRatio"、"Listed1MonthProductCount"、"Listed1MonthProductCountRatio"、"Listed1MonthSalesVolume"、"Listed1MonthSalesVolumeRatio"、"Listed1MonthSalesAmount"、"Listed1MonthSalesAmountRatio"、"Listed1MonthAvgStarRating"、"Listed1MonthAvgReviewCount"、"Listed1MonthAvgPrice"、"Listed3MonthProductCount"、"Listed3MonthProductCountRatio"、"Listed3MonthSalesVolume"、"Listed3MonthSalesVolumeRatio"、"Listed3MonthSalesAmount"、"Listed3MonthSalesAmountRatio"、"Listed3MonthAvgStarRating"、"Listed3MonthAvgReviewCount"、"Listed3MonthAvgPrice"、"Listed6MonthProductCount"、"Listed6MonthProductCountRatio"、"Listed6MonthSalesVolume"、"Listed6MonthSalesVolumeRatio"、"Listed6MonthSalesAmount"、"Listed6MonthSalesAmountRatio"、"Listed6MonthAvgStarRating"、"Listed6MonthAvgReviewCount"、"Listed6MonthAvgPrice"、"Listed12MonthProductCount"、"Listed12MonthProductCountRatio"、"Listed12MonthSalesVolume"、"Listed12MonthSalesVolumeRatio"、"Listed12MonthSalesAmount"、"Listed12MonthSalesAmountRatio"、"Listed12MonthAvgStarRating"、"Listed12MonthAvgReviewCount"、"Listed12MonthAvgPrice"、"Listed24MonthProductCount"、"Listed24MonthProductCountRatio"、"Listed24MonthSalesVolume"、"Listed24MonthSalesVolumeRatio"、"Listed24MonthSalesAmount"、"Listed24MonthSalesAmountRatio"、"Listed24MonthAvgStarRating"、"Listed24MonthAvgReviewCount"、"Listed24MonthAvgPrice"、"Top3ProductSalesVolumeRatio"、"Top3ProductSalesAmountRatio"、"Top3SellerSalesVolumeRatio"、"Top3SellerSalesAmountRatio"、"Top5ProductSalesVolumeRatio"、"Top5ProductSalesAmountRatio"、"Top5SellerSalesVolumeRatio"、"Top5SellerSalesAmountRatio"、"Top10ProductSalesVolumeRatio"、"Top10ProductSalesAmountRatio"、"Top10SellerSalesVolumeRatio"、"Top10SellerSalesAmountRatio" | 否 | 历史趋势类型。允许值：MonthlySalesVolume、MonthlySalesAmount、AveragePrice、AverageReviewCount、AverageStarRating、SellerCount、AverageVariantCount。 |
| `site` | String；允许值："VN"、"ID"、"SG"、"TH"、"MY"、"TW"、"PH"、"BR" | 是 | Shopee 站点，支持：201:VN、202:ID、203:SG、204:TH、205:MY、206:TW、207:PH、208:BR。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "site": "TH"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.AveragePrice` | Number | 平均价格 |
| `data.AverageReviewCount` | Number | 平均评论数 |
| `data.AverageStarRating` | Number | 平均星级 |
| `data.AverageVariantCount` | Number | 平均变体数 |
| `data.MonthlySalesAmount` | Number | 30 天销售额 |
| `data.MonthlySalesVolume` | Integer | 30 天滚动销量 |
| `data.SellerCount` | Number | 卖家数 |

## 使用要点

- 必填字段：`site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/shopee-category-trend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"site":"TH"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。
