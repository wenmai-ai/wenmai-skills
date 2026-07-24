# Wenmai SellerSprite traffic listing API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-listing`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`traffic_listing`
- **脚本入口**：`scripts/traffic_listing.py`，脚本参数即标准 API POST Body JSON

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
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string | 是 | 站点编码，例如 US |
| `request.asinList` | array | 是 | asin列表；["B07Z82895W"] |
| `request.relations` | array | 是 | 关联类型，例如 ["vav"] |
| `request.variations` | boolean | 否 | 是否查询变体；false |
| `request.page` | integer | 否 | 页码，从 1 开始；默认：1 |
| `request.size` | integer | 否 | 每页条数；默认：50 |
| `request.order` | object | 否 | 排序 |
| `request.order.field` | string | 否 | 排序字段 |
| `request.order.desc` | boolean | 否 | true为降序 false为升序；默认降序 |

## 请求示例

```json
{
  "request": {
    "asinList": [
      "B08GHW4TBS"
    ],
    "marketplace": "US",
    "relations": [
        "vav"
      ]
  }
}
```


## 响应结构

公共响应字段：`code`、`message`、`requestId`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `guestId` | string | 访客 ID。 |
| `pages` | integer | 总页数。 |
| `page` | integer | 当前页码。 |
| `size` | integer | 每页数量。 |
| `total` | integer | 总数量。 |
| `took` | integer | 请求耗时。 |
| `url` | string | 链接地址。 |
| `order` | object | 排序对象。 |
| `order.field` | string | 排序字段。 |
| `order.desc` | boolean | 是否降序。 |
| `items[]` | array | 列表数据。 |
| `items[].asin` | string | ASIN。 |
| `items[].brand` | string | 品牌。 |
| `items[].brandUrl` | string | 品牌链接。 |
| `items[].imageUrl` | string | 图片 URL。 |
| `items[].title` | string | 标题。 |
| `items[].parent` | string | 父 ASIN。 |
| `items[].nodeLabelPath` | string | 类目名称路径。 |
| `items[].nodeIdPath` | string | 类目节点路径。 |
| `items[].nodeId` | string | 类目节点 ID。 |
| `items[].bsrId` | string | BSR 类目 ID。 |
| `items[].bsr` | string | BSR 排名。 |
| `items[].bsrCv` | string | BSR 变异系数。 |
| `items[].bsrCr` | number | BSR 变化率。 |
| `items[].amzUnit` | string | Amazon 自营销量。 |
| `items[].amzUnitDate` | string | Amazon 自营销量日期。 |
| `items[].amzSales` | string | Amazon 自营销量。 |
| `items[].units` | integer | 销量。 |
| `items[].unitsGr` | string | 销量增长率。 |
| `items[].revenue` | string | 销售额。 |
| `items[].price` | number | 价格。 |
| `items[].averagePrice` | number | 平均价格。 |
| `items[].primePrice` | number | Prime 价格。 |
| `items[].profit` | string | 利润。 |
| `items[].fba` | string | FBA 费用。 |
| `items[].ratings` | integer | 评论数。 |
| `items[].ratingsRate` | number | 评论率。 |
| `items[].rating` | string | 评分。 |
| `items[].ratingsCv` | string | 评论数变异系数。 |
| `items[].ratingDelta` | string | 评分变化值。 |
| `items[].availableDate` | string | 可售日期。 |
| `items[].fulfillment` | string | 配送方式。 |
| `items[].variations` | integer | 变体数量。 |
| `items[].sellers` | integer | 卖家数量。 |
| `items[].sellerName` | string | 卖家名称。 |
| `items[].sellerId` | string | 卖家 ID。 |
| `items[].sellerNation` | string | 卖家国家或地区。 |
| `items[].lqs` | string | Listing 质量分。 |
| `items[].weight` | string | 重量。 |
| `items[].dimension` | string | 商品尺寸。 |
| `items[].pkgDimensions` | string | 包装尺寸。 |
| `items[].pkgDimensionType` | string | 包装尺寸类型。 |
| `items[].pkgWeight` | string | 包装重量。 |
| `items[].sku` | string | SKU。 |
| `items[].dimensionsType` | string | 尺寸类型。 |
| `items[].deliveryPrice` | number | 配送价格。 |
| `items[].badge` | string | 商品标签。 |
| `items[].badge.bestSeller` | string | Best Seller 标签。 |
| `items[].badge.amazonChoice` | string | Amazon Choice 标签。 |
| `items[].badge.newRelease` | string | New Release 标签。 |
| `items[].badge.ebc` | string | 是否有 A+ 页面。 |
| `items[].badge.video` | string | 是否有视频。 |
| `items[].subcategories[]` | array | 子类目列表。 |
| `items[].subcategories[].code` | string | code。 |
| `items[].subcategories[].rank` | integer | 排名。 |
| `items[].subcategories[].label` | string | 分组标签。 |
| `items[].symbol` | string | 币种符号。 |
| `terminal` | string | 终端类型。 |
| `hasNextPage` | integer | 是否还有下一页。 |
| `guestVisited` | boolean | 访客是否访问过。 |

## 使用要点

- 本 Skill 直接调用 Wenmai 标准 API `/sellersprite/traffic-listing`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-listing" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request": {"asinList": ["B08GHW4TBS"], "marketplace": "US", "relations": ["vav"]}}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs。
