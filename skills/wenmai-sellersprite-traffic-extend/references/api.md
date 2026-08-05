# Wenmai SellerSprite `traffic_extend` API 参考

用于在指定 Amazon 站点中，根据 ASIN、时间范围及多维筛选条件，。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-extend`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`traffic_extend`
- **脚本入口**：`scripts/traffic_extend.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `request.historyDate` | string | 否 | 历史日期，yyyyMM格式，最近30天不传或传空字符串；示例：202201。 |
| `request.asinList` | array | 是 | asin列表(最多20)；示例：["B07Z82895W"]。 |
| `request.queryType` | integer；可选值：0、1、2 | 否 | 查询方式 0 所有变体 1畅销变体 2当前变体，默认2；示例：2。 |
| `request.minSearches` | integer | 否 | 最小月搜索量；示例：100。 |
| `request.maxSearches` | integer | 否 | 最大月搜索量；示例：300。 |
| `request.minSearchRank` | integer | 否 | 最小搜索排名；示例：33。 |
| `request.maxSearchRank` | integer | 否 | 最大搜索排名；示例：3223。 |
| `request.minPurchases` | integer | 否 | 最小购买量；示例：6。 |
| `request.maxPurchases` | integer | 否 | 最大购买量；示例：34。 |
| `request.minPurchaseRate` | number | 否 | 最小购买率；示例：3。 |
| `request.maxPurchaseRate` | number | 否 | 最大购买率；示例：43。 |
| `request.minProducts` | integer | 否 | 最小商品数；示例：10。 |
| `request.maxProducts` | integer | 否 | 最大商品数；示例：90。 |
| `request.minSupplyDemandRatio` | number | 否 | 最小供需比；示例：11.2。 |
| `request.maxSupplyDemandRatio` | number | 否 | 最大供需比；示例：45.2。 |
| `request.minBid` | number | 否 | 最小ppc竞价；示例：10.2。 |
| `request.maxBid` | number | 否 | 最大ppc竞价；示例：23.1。 |
| `request.minAdProducts` | integer | 否 | 最小广告竞品数；示例：123。 |
| `request.maxAdProducts` | integer | 否 | 最大广告竞品数；示例：345。 |
| `request.minAvgPrice` | number | 否 | 最小均价；示例：20。 |
| `request.maxAvgPrice` | number | 否 | 最大均价；示例：30.3。 |
| `request.minWordCount` | integer | 否 | 最小单词个数；示例：2。 |
| `request.maxWordCount` | integer | 否 | 最大单词个数；示例：4。 |
| `request.includeKeywords` | array | 否 | 包含的词；示例：["phone stand"]。 |
| `request.excludeKeywords` | array | 否 | 排除的词；示例：["phone stand"]。 |
| `request.minSPR` | integer | 否 | 最小SPR；2 |
| `request.maxSPR` | integer | 否 | 最大SPR；16 |
| `request.minTitleDensity` | integer | 否 | 最小标题密度；示例：2。 |
| `request.maxTitleDensity` | integer | 否 | 最大标题密度；示例：23。 |
| `request.minMonopolyClickRate` | number | 否 | 最小点击集中度；示例：23.4。 |
| `request.maxMonopolyClickRate` | number | 否 | 最大点击集中度；示例：53.1。 |
| `request.minTrafficPercentage` | number | 否 | 最小流量占比；示例：45。 |
| `request.maxTrafficPercentage` | number | 否 | 最大流量占比；示例：23。 |
| `request.minConversionRate` | number | 否 | 最小转化率；示例：0.23。 |
| `request.maxConversionRate` | number | 否 | 最大转化率；示例：1.4。 |
| `request.minCompetitors` | integer | 否 | 最小asin数；示例：4。 |
| `request.maxCompetitors` | integer | 否 | 最大asin数；示例：23。 |
| `request.amazonChoice` | boolean | 否 | 亚马逊推荐词；示例：TRUE。 |
| `request.page` | integer | 否 | 页码，从 1 开始；默认：1。 |
| `request.size` | integer | 否 | 每页条数，最大50；默认：50。 |
| `request.order` | object | 否 | 排序配置对象。 |
| `request.order.field` | string | 否 | 请求指定的排序字段；允许值由具体接口的供应商契约决定。 |
| `request.order.desc` | boolean | 否 | true为降序 false为升序；默认降序。 |

## 请求示例

```json
{
  "request": {
    "asinList": [
      "B08GHW4TBS"
    ],
    "queryType": 1,
    "marketplace": "US"
  }
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `guestId` | string | 访客 ID。 |
| `pages` | integer | 分页结果的总页数。 |
| `page` | integer | 当前页码。 |
| `size` | integer | 本次分页结果每页返回的记录数。 |
| `total` | integer | 总数量。 |
| `took` | integer | 请求耗时。 |
| `url` | string | 用于打开当前页面、媒体或资源的链接。 |
| `order` | object | 排序对象。 |
| `order.field` | string | 分页结果实际采用的排序字段。 |
| `order.desc` | boolean | 是否降序。 |
| `items[]` | array | 列表数据。 |
| `items[].keyword` | string | 关键字；官方示例值：N95。 |
| `items[].keywordCn` | string | 关键词中文翻译；官方示例值：用于录音的电话支架。 |
| `items[].searches` | integer | 搜索量；官方示例值：21582。 |
| `items[].products` | integer | 商品数；官方示例值：1645。 |
| `items[].purchases` | integer | 月购买量；官方示例值：1996。 |
| `items[].purchaseRate` | number | 月购买率；官方示例值：0.0925。 |
| `items[].bid` | number | PPC价格；官方示例值：1.6。 |
| `items[].bidMax` | number | 最大PPC价格；官方示例值：3.21。 |
| `items[].bidMin` | number | 最小PPC价格；官方示例值：1.34。 |
| `items[].badges[]` | array | 流量词类型。 |
| `items[].rankPosition` | object | 排名位置。 |
| `items[].adPosition` | object | 广告位置。 |
| `items[].updatedTime` | integer | 更新时间。 |
| `items[].searchesRank` | integer | 周搜索量排名；官方示例值：25。 |
| `items[].searchesRankTimeFrom` | integer | 周搜索量排名时间范围。 |
| `items[].searchesRankTimeTo` | string | 搜索量排名统计结束时间。 |
| `items[].latest1daysAds` | integer | 最近1天广告竞品数；官方示例值：70。 |
| `items[].latest7daysAds` | integer | 最近7天广告竞品数；官方示例值：100。 |
| `items[].latest30daysAds` | integer | 最近30天广告竞品数；官方示例值：280。 |
| `items[].supplyDemandRatio` | number | 供需比；官方示例值：3.8。 |
| `items[].trafficPercentage` | number | 流量占比；官方示例值：0.015。 |
| `items[].calculatedWeeklySearches` | number | 预估周搜索量；官方示例值：40。 |
| `items[].avgPrice` | number | 平均价格；官方示例值：36.14。 |
| `items[].avgReviews` | integer | 平均评论数。 |
| `items[].avgRating` | number | 平均评分值；官方示例值：4.5。 |
| `items[].titleDensity` | string | 标题密度。 |
| `items[].spr` | string | 8 天单量。 |
| `items[].monopolyClickRate` | number | 点击集中度（官方称“点击垄断率”）；0.3。 |
| `items[].top3ClickingRate` | number | Top3 点击占比；官方示例值：0.0813。 |
| `items[].top3ConversionRate` | number | Top3 转化占比；官方示例值：0.2011。 |
| `items[].relationVariationsItems[]` | array | 来自于哪些变体。 |
| `items[].relationVariationsItems[].marketplace` | string | 站点；官方示例值：3。 |
| `items[].relationVariationsItems[].asin` | string | Amazon ASIN；官方示例值：B08P6SC34B。 |
| `items[].relationVariationsItems[].imageUrl` | string | 图片链接；官方示例值：10。 |
| `items[].relationVariationsItems[].trafficPercentage` | number | 流量占比；官方示例值：54.6。 |
| `items[].relationVariationsItems[].title` | string | 关联变体的商品标题。 |
| `items[].relationVariationsItems[].price` | number | 商品价格；官方示例值：60。 |
| `items[].relationVariationsItems[].reviews` | number | 评论数；官方示例值：10。 |
| `items[].relationVariationsItems[].rating` | number | 评分；官方示例值：4.5。 |
| `terminal` | string | 终端类型。 |
| `hasNextPage` | integer | 是否还有下一页。 |
| `guestVisited` | boolean | 访客是否访问过。 |

## 使用要点

- 必填字段：`request`, `request.marketplace`, `request.asinList`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/traffic-extend" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request":{"asinList":["B08GHW4TBS"],"queryType":1,"marketplace":"US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
