# Wenmai Alpha JD Com Product Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/jd-com-product-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_jd_com_product_scraper`
- **接口说明**：JD.com Product Scraper — Search, Detail, Reviews
- **脚本入口**：`scripts/alpha_jd_com_product_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `itemId` | string | 否 | ID 标识。 |
| `shopId` | string | 否 | 店铺信息。 |
| `keyword` | string | 否 | 搜索关键词。 |
| `maxPages` | integer | 否 | 最大采集或返回数量。 |
| `operation` | string | 否 | 采集操作。可选值：productSearch、productDetail、productComments、shopCatalog、productPrice。`productSearch` 为基础搜索；其余四种操作会按所选能力单独计费，仅在用户明确要求相应数据时使用。 |

### 额外计费提醒

不要自动把 `operation` 从基础的 `productSearch` 切换为 `productDetail`、`productComments`、`shopCatalog` 或 `productPrice`。使用这些操作前应提醒用户所选能力需要单独计费。不要展示或解释上游价格、套餐、阶梯或计费公式。

## 请求示例

脚本入参示例：

```json
{
  "itemId": "100256400499",
  "shopId": "1000004259",
  "keyword": "华为手机",
  "maxPages": 3,
  "operation": "productSearch"
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | number | ID 标识。 |
| `title` | string | 标题。 |
| `imageUrl` | string | 链接地址。 |
| `tagUrl` | string | 链接地址。 |
| `click` | string | click 字段。 |
| `exp` | string | exp 字段。 |
| `cid1` | number | cid1 字段。 |
| `cid2` | number | cid2 字段。 |
| `cid3` | number | cid3 字段。 |
| `shopId` | number | 店铺信息。 |
| `shopName` | string | 店铺信息。 |
| `venderId` | number | ID 标识。 |
| `bId` | number | ID 标识。 |
| `pCode` | string | pCode 字段。 |
| `global` | string | global 字段。 |
| `price` | number | 价格。 |
| `cc` | string | cc 字段。 |
| `gcp` | string | gcp 字段。 |
| `foi` | string | foi 字段。 |
| `sales` | string | sales 字段。 |
| `monthSales` | string | monthSales 字段。 |
| `landUrl` | string | 链接地址。 |
| `followed` | string | followed 字段。 |
| `presell` | string | presell 字段。 |
| `adSkuType` | string | ID 标识。 |
| `zy` | string | zy 字段。 |
| `xp` | string | xp 字段。 |
| `cjxp` | string | cjxp 字段。 |
| `live` | string | live 字段。 |
| `themeId` | number | ID 标识。 |
| `lowestPrice` | number | 价格。 |
| `isJdMarket` | boolean | 是否启用该选项。 |
| `fxDy` | string | fxDy 字段。 |
| `gcw` | string | gcw 字段。 |
| `sid` | number | ID 标识。 |
| `adType` | string | adType 字段。 |
| `promoTag` | string | promoTag 字段。 |
| `isType` | boolean | 是否启用该选项。 |
| `reqId` | number | ID 标识。 |
| `coupons` | string | coupons 字段。 |
| `discounts` | number | 数量。 |
| `gifts` | string | gifts 字段。 |
| `images` | array | 图片列表。 |
| `jxzy` | string | jxzy 字段。 |
| `gzy` | string | gzy 字段。 |
| `onShelvesTime` | string | 时间或日期。 |
| `gct` | string | gct 字段。 |
| `freight` | string | freight 字段。 |
| `posId` | number | ID 标识。 |
| `isBybt` | boolean | 是否启用该选项。 |
| `bybtTraffic` | string | bybtTraffic 字段。 |
| `offset` | string | offset 字段。 |
| `us` | string | us 字段。 |
| `skuReplaceType` | string | ID 标识。 |
| `fs` | string | fs 字段。 |
| `lac` | string | lac 字段。 |
| `frae` | string | frae 字段。 |
| `esi` | string | esi 字段。 |
| `lsi` | string | lsi 字段。 |
| `element` | string | element 字段。 |
| `element.foi` | string | foi 字段。 |
| `element.gcw` | string | gcw 字段。 |
| `eleinfos` | string | eleinfos 字段。 |
| `eleinfos.bitField0_` | string | bitField0_ 字段。 |
| `eleinfos.eleType_` | string | eleType_ 字段。 |
| `eleinfos.score_` | number | 评分。 |
| `eleinfos.eleStatus_` | string | 状态。 |
| `eleinfos.isExposure_` | boolean | 是否启用该选项。 |
| `eleinfos.impCount_` | number | 数量。 |
| `eleinfos.clickCount_` | number | 数量。 |
| `eleinfos.context_` | string | context_ 字段。 |
| `eleinfos.memoizedIsInitialized` | boolean | memoizedIsInitialized 字段。 |
| `eleinfos.unknownFields` | string | unknownFields 字段。 |
| `eleinfos.unknownFields.fields` | string | fields 字段。 |
| `eleinfos.unknownFields.fieldsDescending` | string | fieldsDescending 字段。 |
| `eleinfos.memoizedSize` | string | memoizedSize 字段。 |
| `eleinfos.memoizedHashCode` | boolean | memoizedHashCode 字段。 |
| `interaction` | string | interaction 字段。 |
| `imageType` | string | imageType 字段。 |
| `showType` | string | showType 字段。 |
| `itemId` | number | ID 标识。 |
| `productTitle` | string | productTitle 字段。 |
| `coverUrl` | string | 链接地址。 |
| `currency` | string | 币种。 |
| `sellerType` | string | 卖家信息。 |
| `categoryIds` | number | 分类。 |
| `salesText` | string | salesText 字段。 |
| `monthSalesText` | string | monthSalesText 字段。 |
| `reviewCountText` | string | 评论列表。 |
| `goodRate` | string | goodRate 字段。 |
| `itemUrl` | string | 链接地址。 |
| `shopUrl` | string | 链接地址。 |
| `isJdSelf` | boolean | 是否启用该选项。 |
| `_operation` | string | _operation 字段。 |
| `_fetchedAt` | string | _fetchedAt 字段。 |
| `_page` | string | _page 字段。 |
| `_sourceKeyword` | string | _sourceKeyword 字段。 |
| `_totalCount` | number | 数量。 |
| `_totalPages` | number | 数量。 |

## 使用要点

- 本接口适合：京东商品搜索和详情。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/jd-com-product-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "100256400499", "shopId": "1000004259", "keyword": "华为手机", "maxPages": 3, "operation": "productSearch"}'
```

---

来源：Wenmai WMAPI 文档；额外计费参数提醒依据《新数据中心供应商价格表》（核对日期：2026-07-24）。
