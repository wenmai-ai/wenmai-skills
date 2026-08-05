# Wenmai SellerSprite `keyword_miner` API 参考

Amazon 高级关键词流量与竞争分析工具（卖家决策级）。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keyword-miner`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`keyword_miner`
- **脚本入口**：`scripts/keyword_miner.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `request.historyDate` | string | 否 | 历史日期，yyyyMM格式，最近30天不传或传空字符串；示例：202201。 |
| `request.keyword` | string | 是 | 查询关键词文本。 |
| `request.keywordList` | array | 否 | 批量查询关键词；示例：["phone stand"]。 |
| `request.minSearch` | integer | 否 | 最小搜索量；示例：543。 |
| `request.maxSearch` | integer | 否 | 最大搜索量；示例：23453。 |
| `request.minPurchases` | integer | 否 | 最小购买量；示例：6。 |
| `request.maxPurchases` | integer | 否 | 最大购买量；示例：34。 |
| `request.minPurchasesRate` | number | 否 | 最小购买率；示例：3。 |
| `request.maxPurchasesRate` | number | 否 | 最大购买率；示例：43。 |
| `request.minSPR` | integer | 否 | 最小SPR；2 |
| `request.maxSPR` | integer | 否 | 最大SPR；16 |
| `request.minTitleDensity` | integer | 否 | 最小标题密度；示例：2。 |
| `request.maxTitleDensity` | integer | 否 | 最大标题密度；示例：23。 |
| `request.minRelevancy` | number | 否 | 最小相关度；23，最小0。 |
| `request.maxRelevancy` | number | 否 | 最大相关度；90，最大100。 |
| `request.minSearchRank` | integer | 否 | 最小搜索排名；示例：33。 |
| `request.maxSearchRank` | integer | 否 | 最大搜索排名；示例：3223。 |
| `request.minProducts` | integer | 否 | 最小商品数；示例：54。 |
| `request.maxProducts` | integer | 否 | 最大商品数；示例：324。 |
| `request.minSupplyDemandRatio` | number | 否 | 最小供需比；示例：11.2。 |
| `request.maxSupplyDemandRatio` | number | 否 | 最大供需比；示例：45.2。 |
| `request.minAdProducts` | integer | 否 | 最小广告竞品数；示例：123。 |
| `request.maxAdProducts` | integer | 否 | 最大广告竞品数；示例：345。 |
| `request.minWordCount` | integer | 否 | 最小单词个数；示例：2。 |
| `request.maxWordCount` | integer | 否 | 最大单词个数；示例：4。 |
| `request.minMonopolyClickRate` | number | 否 | 最小点击集中度；示例：23.4。 |
| `request.maxMonopolyClickRate` | number | 否 | 最大点击集中度；示例：53.1。 |
| `request.minBid` | number | 否 | 最小ppc竞价；示例：10.2。 |
| `request.maxBid` | number | 否 | 最大ppc竞价；示例：23.1。 |
| `request.minPrice` | number | 否 | 最小均价；示例：43.3。 |
| `request.maxPrice` | number | 否 | 最大均价；示例：234.2。 |
| `request.minRatings` | integer | 否 | 最小评分数；示例：100。 |
| `request.maxRatings` | integer | 否 | 最大评分数；示例：399。 |
| `request.minRating` | number | 否 | 最小评分值；示例：3。 |
| `request.maxRating` | number | 否 | 最大评分值；示例：4.9。 |
| `request.amazonChoice` | boolean | 否 | 亚马逊推荐词；示例：true。 |
| `request.filterRootWord` | integer | 否 | 过滤词根 0包含所有 1只包含词根；示例：0。 |
| `request.matchType` | integer；可选值：2、3 | 否 | 2: 广泛匹配, 3: 词组匹配；示例：2。 |
| `request.includeKeywords` | array | 否 | 包含的词；示例：["phone stand"]。 |
| `request.excludeKeywords` | array | 否 | 排除的词；示例：["phone stand"]。 |
| `request.page` | integer | 否 | 页码，从 1 开始；默认：1。 |
| `request.size` | integer | 否 | 每页条数；默认：50，最大：100。 |
| `request.order` | object | 否 | 排序配置对象。 |
| `request.order.field` | string | 否 | 排序字段，加入筛序条件之后，不能以相关度排序 |
| `request.order.desc` | boolean | 否 | true为降序 false为升序；默认降序。 |

## 请求示例

```json
{
  "request": {
    "keyword": "wireless earbuds",
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
| `items[].marketplace` | string | 市场；官方示例值：US。 |
| `items[].keyword` | string | 关键词文本；官方示例值：phone stand for recording。 |
| `items[].keywordCn` | string | 关键词中文翻译；官方示例值：用于录音的电话支架。 |
| `items[].keywordJp` | string | 关键词英文翻译；官方示例值：録音用電話スタンド。 |
| `items[].departments[]` | array | Amazon 类目。 |
| `items[].departments[].code` | string | 类目代码；官方示例值：electronics。 |
| `items[].departments[].label` | string | 类目名称；官方示例值：Electronics。 |
| `items[].month` | string | 搜索月份；官方示例值：2022.01。 |
| `items[].supplement` | string | 是否属于补充关键词（无当前月搜索量）；官方示例值：N。 |
| `items[].searches` | integer | 搜索量；官方示例值：21582。 |
| `items[].purchases` | integer | 月购买量；官方示例值：1996。 |
| `items[].purchaseRate` | number | 月购买率；官方示例值：0.0925。 |
| `items[].monopolyClickRate` | number | 点击集中度（官方称“点击垄断率”）；0.3。 |
| `items[].products` | integer | 商品数；官方示例值：1645。 |
| `items[].adProducts` | integer | 广告竞品数；官方示例值：34。 |
| `items[].supplyDemandRatio` | number | 供需比；官方示例值：13.12。 |
| `items[].avgPrice` | number | 平均价格；官方示例值：36.14。 |
| `items[].avgRatings` | integer | 平均评分数；官方示例值：12223。 |
| `items[].avgRating` | number | 平均评分值；官方示例值：4.5。 |
| `items[].bidMin` | number | 最小PPC价格；官方示例值：1.34。 |
| `items[].bidMax` | number | 最大PPC价格；官方示例值：3.21。 |
| `items[].bid` | number | PPC价格；官方示例值：1.6。 |
| `items[].cvsShareRate` | number | 转化共享率；官方示例值：0.3084。 |
| `items[].wordCount` | integer | 单词个数；官方示例值：4。 |
| `items[].titleDensity` | string | 标题密度。 |
| `items[].spr` | string | 8 天单量。 |
| `items[].relevancy` | number | 相关度；官方示例值：28.6。 |
| `items[].amazonChoice` | boolean | 亚马逊推荐词 true是的 false不是；官方示例值：false。 |
| `items[].searchRank` | integer | 搜索排名；官方示例值：17910。 |
| `items[].trends` | string | trends。 |
| `items[].clicks` | integer | 点击量；官方示例值：10。 |
| `items[].impressions` | integer | 展示量；官方示例值：20。 |
| `terminal` | string | 终端类型。 |
| `hasNextPage` | integer | 是否还有下一页。 |
| `guestVisited` | boolean | 访客是否访问过。 |

## 使用要点

- 必填字段：`request`, `request.marketplace`, `request.keyword`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keyword-miner" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request":{"keyword":"wireless earbuds","marketplace":"US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
