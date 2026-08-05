# Wenmai SellerSprite `keyword_research` API 参考

专业级 Amazon 关键词市场与选品分析工具。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keyword-research`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`keyword_research`
- **脚本入口**：`scripts/keyword_research.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `request.month` | string | 否 | 筛选日期,yyyyMM格式，支持近24个月的；示例：202203。 |
| `request.departments` | array | 否 | 查询类目，见关键词选品类目接口，传递code；示例：["automotive","baby-products"]。 |
| `request.keywords` | string | 否 | 关键词文本；示例：N95。 |
| `request.excludeKeywords` | string | 否 | 排除的关键字；示例：portable。 |
| `request.minSearches` | integer | 否 | 最小月搜索量；示例：100。 |
| `request.maxSearches` | integer | 否 | 最大月搜索量；示例：300。 |
| `request.minSearchesCr` | number | 否 | 最小月搜索量增长率；示例：10。 |
| `request.maxSearchesCr` | number | 否 | 最大月搜索量增长率；示例：50.8。 |
| `request.minProducts` | integer | 否 | 最小商品数；示例：10。 |
| `request.maxProducts` | integer | 否 | 最大商品数；示例：90。 |
| `request.minPurchases` | integer | 否 | 最小购买量；示例：100。 |
| `request.maxPurchases` | integer | 否 | 最大购买量；示例：500。 |
| `request.minPurchaseRate` | number | 否 | 最小购买率；示例：3.2。 |
| `request.maxPurchaseRate` | number | 否 | 最大购买率；示例：10.5。 |
| `request.withYearlyGrowth` | boolean | 否 | 新细分市场；示例：false。 |
| `request.minSearchMonthCv` | integer | 否 | 最小月搜索量同比增长值；示例：1000。 |
| `request.maxSearchMonthCv` | integer | 否 | 最大月搜索量同比增长值；示例：3000。 |
| `request.minSearchMonthCr` | number | 否 | 最小月搜索量同比增长率；示例：5.3。 |
| `request.maxSearchMonthCr` | number | 否 | 最大月搜索量同比增长率；示例：30.1。 |
| `request.minSearchNearlyCv` | integer | 否 | 最小月搜索量近3个月增长值；示例：6000。 |
| `request.maxSearchNearlyCv` | integer | 否 | 最大月搜索量近3个月增长值；示例：20000。 |
| `request.minSearchNearlyCr` | number | 否 | 最小月搜索量近3个月增长率；示例：10.3。 |
| `request.maxSearchNearlyCr` | number | 否 | 最大月搜索量近3个月增长率；示例：20.4。 |
| `request.marketPeriod` | string | 否 | 市场周期 |
| `request.minAvgPrice` | number | 否 | 最小均价；示例：20。 |
| `request.maxAvgPrice` | number | 否 | 最大均价；示例：30.3。 |
| `request.minRatings` | integer | 否 | 最小评分数；示例：2000。 |
| `request.maxRatings` | integer | 否 | 最大评分数；示例：3000。 |
| `request.minRating` | number | 否 | 最小评分值；示例：3.2。 |
| `request.maxRating` | number | 否 | 最大评分值；示例：4.1。 |
| `request.minBid` | number | 否 | 最小PPC竞价；示例：6.2。 |
| `request.maxBid` | number | 否 | 最大PPC竞价；示例：10.6。 |
| `request.minAraClickRate` | number | 否 | 最小点击集中度；示例：20.1。 |
| `request.maxAraClickRate` | number | 否 | 最大点击集中度；示例：56.4。 |
| `request.minGoodsValue` | number | 否 | 最小货流值；示例：10.1。 |
| `request.maxGoodsValue` | number | 否 | 最大货流值；示例：41.1。 |
| `request.minSupplyDemandRatio` | number | 否 | 最小供需比；示例：5.6。 |
| `request.maxSupplyDemandRatio` | number | 否 | 最大供需比；示例：10.4。 |
| `request.minWordCount` | integer | 否 | 最小单词个数；示例：1。 |
| `request.maxWordCount` | integer | 否 | 最大单词个数；示例：3。 |
| `request.page` | integer | 否 | 页码，从 1 开始；默认：1。 |
| `request.size` | integer | 否 | 每页条数，默认15；最大：15。 |
| `request.order` | object | 否 | 排序配置对象。 |
| `request.order.field` | string | 否 | 请求指定的排序字段；允许值由具体接口的供应商契约决定。 |
| `request.order.desc` | boolean | 否 | true为降序 false为升序；默认降序。 |

## 请求示例

```json
{
  "request": {
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
| `total` | integer | 类目总计；官方示例值：141356。 |
| `took` | integer | 请求耗时。 |
| `url` | string | 用于打开当前页面、媒体或资源的链接。 |
| `order` | object | 排序对象。 |
| `order.field` | string | 分页结果实际采用的排序字段。 |
| `order.desc` | boolean | 是否降序。 |
| `items[]` | array | 列表数据。 |
| `items[].marketplace` | string | Amazon 市场站点编码；官方示例值：US。 |
| `items[].keywords` | string | 关键词文本；官方示例值：polaroid cameras。 |
| `items[].searches` | integer | 搜索量；官方示例值：141356。 |
| `items[].purchases` | integer | 月购买量；官方示例值：4029。 |
| `items[].growth` | number | 增长率；官方示例值：-25.482092。 |
| `items[].purchaseRate` | number | 月购买率；官方示例值：0.0285。 |
| `items[].products` | integer | 产品数；官方示例值：173。 |
| `items[].supplyDemandRatio` | number | 供需比；官方示例值：817.09。 |
| `items[].searchDepartments[]` | array | Amazon 类目。 |
| `items[].searchDepartments[].code` | string | 类目代码；官方示例值：electronics。 |
| `items[].searchDepartments[].label` | string | 类目名称；官方示例值：Electronics。 |
| `items[].searchDepartments[].total` | integer | 搜索类目对应的商品总数；官方示例值：141356。 |
| `items[].searchDepartments[].ratio` | number | 类目占比；官方示例值：1。 |
| `items[].month` | string | 查询月份；官方示例值：2022.01。 |
| `items[].supplement` | string | 是否属于补充关键词；官方示例值：N。 |
| `items[].searchMonthlyCv` | integer | 关键词同比增长值；官方示例值：139749。 |
| `items[].searchMonthlyCr` | number | 关键词同比增长率；官方示例值：8696.27。 |
| `items[].searchNearlyCv` | integer | 关键词近3个月增长值；官方示例值：-48338。 |
| `items[].searchNearlyCr` | number | 关键词近3个月增长率；官方示例值：-25.48。 |
| `items[].currency` | string | 货币；官方示例值：$。 |
| `items[].avgPrice` | number | 平均价格；官方示例值：116.24。 |
| `items[].avgRatings` | integer | 平均评分数；官方示例值：2584。 |
| `items[].avgRating` | number | 平均评论数；官方示例值：4.5。 |
| `items[].relationAsinList[]` | array | 关键词关联asin；官方示例值：4.8。 |
| `items[].relationAsinList[].asin` | string | Amazon ASIN；官方示例值：B099VDRGG1。 |
| `items[].relationAsinList[].imageUrl` | string | 图片；官方示例值：https://m.media-amazon.com/images/I/51aZiZaicYL._AC_US200_.jpg。 |
| `items[].relationAsinList[].price` | number | 商品价格；官方示例值：59.95。 |
| `items[].relationAsinList[].ratings` | integer | 评分数；官方示例值：20115。 |
| `items[].relationAsinList[].rating` | number | 评分；官方示例值：4.7。 |
| `items[].bidMin` | number | bid最小价格；官方示例值：0.987。 |
| `items[].bidMax` | number | bid最大价格；官方示例值：2.54。 |
| `items[].bid` | number | bid价格；官方示例值：1.26。 |
| `items[].araAsinList[]` | array | 点击前三ASIN。 |
| `items[].araAsinList[].asin` | string | 点击前三 ASIN 记录的 Amazon ASIN；官方示例值：B099VDRGG1。 |
| `items[].araAsinList[].title` | string | 点击前三 ASIN 记录的商品标题；官方示例值：Fujifilm Instax Mini 9。 |
| `items[].araAsinList[].imageUrl` | string | 点击前三 ASIN 记录的商品图片链接；官方示例值：https://m.media-amazon.com/images/I/51aZiZaicYL._AC_US200_.jpg。 |
| `items[].araAsinList[].clickRate` | number | 点击率；官方示例值：0.116。 |
| `items[].araAsinList[].conversionShareRate` | number | 转化率；官方示例值：0.1217。 |
| `items[].araClickRate` | number | 点击集中度（官方称“点击垄断率”）；0.2633。 |
| `items[].araShareRate` | number | 共享转化率；官方示例值：0.2633。 |
| `items[].goodsValue` | number | 货流值；官方示例值：0.0108。 |
| `items[].marketPeriod` | string | 市场周期；官方示例值：S11,S12。 |
| `items[].brand` | string | 品牌名称；官方示例值：Fujifilm。 |
| `items[].hasBrandWord` | boolean | 是否存在品牌词；官方示例值：false。 |
| `items[].keywordCn` | string | 中文翻译；官方示例值：宝丽来相机。 |
| `items[].brands[]` | array | TOP3 品牌；官方示例值：["LEGO","Jorumo","Nifeliz"]。 |
| `items[].categories[]` | array | TOP3 类目；官方示例值：["Toys","Home","Mobile_Apps"]。 |
| `items[].titleDensityExact` | string | titleDensityExact。 |
| `items[].clicks` | integer | 点击量；在某个关键词搜索结果页中被点击的总次数非单个ASIN在关键词下的点击量。 |
| `items[].impressions` | integer | 展示量；在某个关键词搜索结果页中所有ASIN的总展示次数非单个ASIN在关键词下的曝光量。 |
| `terminal` | string | 终端类型。 |
| `hasNextPage` | integer | 是否还有下一页。 |
| `guestVisited` | boolean | 访客是否访问过。 |

## 使用要点

- 必填字段：`request`, `request.marketplace`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keyword-research" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request":{"marketplace":"US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
