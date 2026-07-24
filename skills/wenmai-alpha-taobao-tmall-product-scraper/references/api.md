# Wenmai Alpha Taobao Tmall Product Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/taobao-tmall-product-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_taobao_tmall_product_scraper`
- **接口说明**：Taobao & Tmall Product Scraper
- **脚本入口**：`scripts/alpha_taobao_tmall_product_scraper.py`，脚本参数即标准 API POST Body JSON

### 运行时覆盖

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `WENMAI_API_ORIGIN` | Wenmai API 地址 | `https://all-api.wenmai-ai.com` |
| `WENMAI_API_BASE_PATH` | 标准 API Base Path | `/wmapi/v1` |
| `WENMAI_API_TIMEOUT` | HTTP 超时时间，单位秒 | `120` |

## 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `sort` | string | 否 | 排序方式。 |
| `itemId` | string | 否 | ID 标识。 |
| `shopId` | string | 否 | 店铺信息。 |
| `userId` | string | 否 | ID 标识。 |
| `keyword` | string | 否 | 搜索关键词。 |
| `endPrice` | integer | 否 | 价格。 |
| `maxPages` | integer | 否 | 最大采集或返回数量。 |
| `operation` | string | 否 | 采集操作。可选值：keywordSearch、productDetail、shopCatalog、productReviews、productQuestions。`keywordSearch` 为基础搜索；其余操作会按所选能力单独计费。 |
| `orderType` | string | 否 | 排序方式。 |
| `tmallOnly` | boolean | 否 | tmallOnly 字段。 |
| `startPrice` | integer | 否 | 价格。 |
| `detailVersion` | string | 否 | 商品详情版本。使用 `v4` 会启用单独计费的最终价/优惠价高级详情能力；不要自动选择。 |
| `catalogVersion` | string | 否 | catalogVersion 字段。 |

### 额外计费提醒

不要自动把 `operation` 从 `keywordSearch` 切换为 `productDetail`、`shopCatalog`、`productReviews` 或 `productQuestions`，也不要自动选择 `detailVersion: "v4"`。只有用户明确要求相应数据时才启用，并在请求前提醒用户该能力需要单独计费。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "sort": "_sale",
  "itemId": "744983869996",
  "shopId": "67095450",
  "userId": "713464357",
  "keyword": "iphone 15",
  "endPrice": 5000,
  "maxPages": 3,
  "operation": "keywordSearch",
  "orderType": "feedbackdate",
  "tmallOnly": false,
  "startPrice": 100,
  "detailVersion": "v9",
  "catalogVersion": "v1"
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `discntPriceYuan` | number | 价格。 |
| `discntRate` | boolean | discntRate 字段。 |
| `extraMap` | string | extraMap 字段。 |
| `fahuoDsr` | string | fahuoDsr 字段。 |
| `frontStock` | number | 库存信息。 |
| `fuwuDsr` | string | fuwuDsr 字段。 |
| `hasTongkuan` | boolean | 是否启用该选项。 |
| `hasXiangsi` | boolean | 是否启用该选项。 |
| `itemGradeAvg` | string | itemGradeAvg 字段。 |
| `itemId` | number | ID 标识。 |
| `itemLoc` | string | itemLoc 字段。 |
| `itemName` | string | itemName 字段。 |
| `itemType` | string | itemType 字段。 |
| `miaoshuDsr` | string | miaoshuDsr 字段。 |
| `options` | string | options 字段。 |
| `orderPayUV` | string | 排序方式。 |
| `picUrl` | string | 链接地址。 |
| `picUrlFull` | string | 链接地址。 |
| `picUrlList` | boolean | 链接地址。 |
| `priceFen` | number | 价格。 |
| `priceYuanDouble` | number | 价格。 |
| `priceZKFen` | number | 价格。 |
| `priceZKYuanDouble` | number | 价格。 |
| `prodId` | number | ID 标识。 |
| `sellerGoodrat` | string | 卖家信息。 |
| `sellerLevel` | string | 卖家信息。 |
| `serviceList` | boolean | serviceList 字段。 |
| `shopId` | number | 店铺信息。 |
| `shopName` | string | 店铺信息。 |
| `spuId` | number | ID 标识。 |
| `tagList` | boolean | tagList 字段。 |
| `tmcTagList` | boolean | tmcTagList 字段。 |
| `userTag` | string | 作者信息。 |
| `userType` | string | 作者信息。 |
| `recordTime` | string | 时间或日期。 |
| `_operation` | string | _operation 字段。 |
| `_fetchedAt` | string | _fetchedAt 字段。 |
| `_page` | string | _page 字段。 |
| `_sourceKeyword` | string | _sourceKeyword 字段。 |
| `_totalItems` | number | 数量。 |
| `_totalPages` | number | 数量。 |

## 使用要点

- 本接口适合：淘宝/天猫商品。
- 优先使用用户给定的 URL、关键词、商品 ID、站点、国家、语言、排序、分页和数量限制。
- 采集类接口的字段会随目标平台页面结构变化；输出分析时保留原始字段名和 URL，避免把缺失字段补写成事实。
- 当用户需要多平台对比时，分别调用对应 Alpha 原子 Skill，再在上层分析中合并结果。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按上方请求参数表修正枚举值、日期格式、分页范围、URL/关键词数组、数量范围或必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/taobao-tmall-product-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sort": "_sale", "itemId": "744983869996", "shopId": "67095450", "userId": "713464357", "keyword": "iphone 15", "endPrice": 5000, "maxPages": 3, "operation": "keywordSearch", "orderType": "feedbackdate", "tmallOnly": false, "startPrice": 100, "detailVersion": "v9", "catalogVersion": "v1"}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。
