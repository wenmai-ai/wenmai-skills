# Wenmai SellerSprite asin detail API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/asin-detail`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`asin_detail`
- **脚本入口**：`scripts/asin_detail.py`，脚本参数即标准 API POST Body JSON

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
| `marketplace` | string | 是 | 站点编码，例如 US |
| `asin` | string | 是 | asin；B08GHW4TBS |

## 请求示例

```json
{
  "marketplace": "US",
  "asin": "B08GHW4TBS"
}
```


## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `asin` | string | ASIN。 |
| `asinUrl` | string | ASIN 商品链接。 |
| `availableDate` | string | 可售日期。 |
| `brand` | string | 品牌。 |
| `brandUrl` | string | 品牌链接。 |
| `bsrId` | string | BSR 类目 ID。 |
| `bsrLabel` | string | BSR 类目名称。 |
| `bsrRank` | integer | BSR 排名。 |
| `subcategories[]` | array | 子类目列表。 |
| `subcategories[].rank` | integer | 排名。 |
| `subcategories[].code` | string | code。 |
| `subcategories[].label` | string | 分组标签。 |
| `createdTime` | string | 创建时间。 |
| `dimensions` | string | 商品尺寸。 |
| `firstRatingDate` | string | 首次留评日期。 |
| `imageUrl` | string | 图片 URL。 |
| `lqs` | string | Listing 质量分。 |
| `nodeId` | string | 类目节点 ID。 |
| `nodeIdPath` | string | 类目节点路径。 |
| `nodeLabelPath` | string | 类目名称路径。 |
| `nodeLabelPathLocale` | string | 本地化类目名称路径。 |
| `parent` | string | 父 ASIN。 |
| `price` | number | 价格。 |
| `primePrice` | number | Prime 价格。 |
| `deliveryPrice` | number | 配送价格。 |
| `coupon` | string | 优惠券信息。 |
| `questions` | string | 问答数量。 |
| `rating` | string | 评分。 |
| `ratings` | integer | 评论数。 |
| `reviews` | integer | 评论数量。 |
| `variantRatings` | integer | 变体评论数。 |
| `variantReviews` | integer | 变体评论数量。 |
| `sellerId` | string | 卖家 ID。 |
| `sellerName` | string | 卖家名称。 |
| `fulfillment` | string | 配送方式。 |
| `sellers` | integer | 卖家数量。 |
| `marketplace` | string | Amazon 站点。 |
| `title` | string | 标题。 |
| `updatedTime` | string | 更新时间。 |
| `variations` | integer | 变体数量。 |
| `weight` | string | 重量。 |
| `zoomImageUrl` | string | 高清图片 URL。 |
| `skuList[]` | array | SKU 列表。 |
| `variationList[]` | array | 变体列表。 |
| `variationList[].asin` | string | ASIN。 |
| `variationList[].attribute` | string | 变体属性。 |
| `features[]` | array | 特征列表。 |
| `overviews` | string | 商品概览。 |
| `badge` | string | 商品标签。 |
| `badge.bestSeller` | string | Best Seller 标签。 |
| `badge.amazonChoice` | string | Amazon Choice 标签。 |
| `badge.newRelease` | string | New Release 标签。 |
| `badge.ebc` | string | 是否有 A+ 页面。 |
| `badge.video` | string | 是否有视频。 |
| `variationList[].amazonChoice` | String | Amazon Choice 标签。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/sellersprite/asin-detail`。
- 成功响应位于 `data`；失败时优先读取 `code`、`message`、`requestId` 和 HTTP 状态。
- 保留用户给出的筛选、分页、排序、日期和站点参数，不要擅自扩大查询范围。
- 长数组结果先汇总关键行，再按用户需要继续展开。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按请求参数表修正必填字段、枚举值、日期格式、分页范围。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/asin-detail" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"marketplace": "US", "asin": "B08GHW4TBS"}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。
