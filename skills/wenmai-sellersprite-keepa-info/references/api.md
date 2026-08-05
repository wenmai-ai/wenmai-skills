# Wenmai SellerSprite `keepa_info` API 参考

获取指定 Amazon ASIN 的完整商品画像及多维度历史趋势数据(不含有销量数据)。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keepa-info`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`keepa_info`
- **脚本入口**：`scripts/keepa_info.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN、MX、BR、AU、AE | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `asin` | string | 是 | Amazon ASIN；示例：B08GHW4TBS。 |
| `startTimestamp` | integer | 否 | 趋势数据起始时间戳。 |
| `endTimestamp` | integer | 否 | 趋势数据结束时间戳。 |
| `dailyLatest` | boolean | 否 | 是否仅获取每日最新趋势数据。 |

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
| `marketplace` | string | Amazon 市场站点编码。 |
| `asin` | string | Amazon ASIN；官方示例值：B07V34QQ3C。 |
| `dataAsin` | string | 实际返回Keepa数据的ASIN；官方示例值：B07V34QQ3C。 |
| `parentAsin` | string | 父体ASIN；官方示例值：B0CWW9N7QW。 |
| `variationAsins` | array | 变体ASIN列表；官方示例值：["B0CN2PBVNS","B0BT4PMNY4","B0C6FYKC3D","B0CSLMG2TF","B0CGGPC6G3","B0BXG8L46Y","B0CRSZGN9L","B07V34QQ3C"]。 |
| `rootCategory` | string | BSR大类节点ID；官方示例值：172282。 |
| `rootCategoryLabel` | string | 跟类目；官方示例值：Electronics。 |
| `salesRankReference` | string | 排名节点ID；官方示例值：541966。 |
| `salesRankReferenceHistory[]` | array | 排名节点变动历史；PairStrDto 趋势字符串数据结构。 |
| `salesRankReferenceHistory[].timePoint` | string | 时间点。 |
| `salesRankReferenceHistory[].value` | string | 数值。 |
| `nodeIdPath` | string | 上架类目全路径；官方示例值：172282:541966:13896617011:565098:13896597011。 |
| `nodeLabelPath` | string | 上架类目名称全路径；官方示例值：Electronics:Computers & Accessories:Computers & Tablets:Desktops:Towers。 |
| `productStatus` | string | 商品状态；STANDARD:everything accessibleDOWNLOADABLE:no marketplace/3rd party price dataEBOOK:no price data and sales rank accessibleINACCESSIBLE:no data accessibleINVALID:invalid or deprecated asinVARIATION_PARENT:product is a parent ASINUNKNOWN:null of status。 |
| `availabilityAmazon` | string | 亚马逊跟卖转态；官方示例值：-1。 |
| `title` | string | 商品标题；iBUYPOWER Gaming PC Computer Desktop Element 9260 (Intel Core i7-9700F 3.0Ghz, NVIDIA GeForce GTX 1660 Ti 6GB, 16GB DDR4, 240GB SSD, 1TB HDD, Wi-Fi & Windows 10 Home) Black。 |
| `brand` | string | 品牌名称；官方示例值：iBUYPOWER。 |
| `asinUrl` | string | ASIN链接；官方示例值：https://www.amazon.com/dp/B07V34QQ3C。 |
| `brandUrl` | string | 品牌链接；官方示例值：https://www.amazon.com/s?k=iBUYPOWER。 |
| `salesRankUrl` | string | 销售排名链接；官方示例值：https://www.amazon.com/b/?node=541966。 |
| `imageUrl` | string | 商品缩略图200*200；官方示例值：https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US200_.jpg。 |
| `zoomImageUrl` | string | 商品大图600*600；官方示例值：https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US600_.jpg。 |
| `imageUrls[]` | array | 商品图片列表；["https://images-na.ssl-images-amazon.com/images/I/711nEj5l5SL._AC_US200_.jpg","https://images-na.ssl-images-amazon.com/images/I/61bpfnvHjqL._AC_US200_.jpg",......]。 |
| `dimensions` | string | 净尺寸；官方示例值：97。 |
| `dimensionsSize[]` | array | 尺寸分布列表。 |
| `weight` | string | 净重量；官方示例值：1063280。 |
| `weightGram` | integer | 净重数值 单位统一为：克(g)；官方示例值：1055398:1063252:1063280。 |
| `pkgDimensions` | string | 打包尺寸；官方示例值：22 x 19.9 x 12.4 inches。 |
| `pkgDimensionsSize[]` | array | 打包尺寸 长/宽/高 单位统一为：厘米(cm)；官方示例值：[558,506,316]。 |
| `pkgWeight` | string | 打包重量；官方示例值：0.11 pounds。 |
| `pkgWeightGram` | integer | 打包重量数值 单位统一为：克(g)；官方示例值：13660。 |
| `fbaFees` | number | FBA总费用；官方示例值：26.11。 |
| `fbaItems` | string | FBA费用项明细JSON串，包含：仓储费，仓储费税，运送打包费，运送打包费税；官方示例值："{\"pickAndPackFeeTax\":0,\"storageFee\":0,\"storageFeeTax\":0,\"pickAndPackFee\":26.11}"。 |
| `numberOfPages` | integer | 在第几页；官方示例值：-1。 |
| `numberOfItems` | integer | 在第几个；官方示例值：1。 |
| `price[]` | array | 价格趋势。 |
| `price[].timePoint` | number | 时间点。 |
| `price[].value` | number | 数值。 |
| `dealPrice[]` | array | 成交价趋势。 |
| `dealPrice[].timePoint` | number | 时间点。 |
| `dealPrice[].value` | number | 数值。 |
| `buyBox[]` | array | 黄金购物车价格趋势。 |
| `buyBox[].timePoint` | string | 时间点。 |
| `buyBox[].value` | string | 数值。 |
| `priceList[]` | array | 划线价格。 |
| `priceList[].timePoint` | number | 时间点。 |
| `priceList[].value` | number | 数值。 |
| `buyBoxSellerIdHistory[]` | array | 黄金购物车卖家Id历史趋势；PairStrDto 趋势字符串数据结构。 |
| `buyBoxSellerIdHistory[].timePoint` | string | 时间点。 |
| `buyBoxSellerIdHistory[].value` | string | 数值。 |
| `bsr[]` | array | 大类BSR排名历史趋势。 |
| `bsr[].timePoint` | string | 时间点。 |
| `bsr[].value` | string | 数值。 |
| `subSalesRank[]` | array | 小类排名趋势数据。 |
| `subSalesRank[].nodeId` | string | 类目节点 ID。 |
| `subSalesRank[].node` | string | 类目节点。 |
| `subSalesRank[].ranks[]` | array | 自然排名关键词数量列表。 |
| `subSalesRank[].ranks[].timePoint` | string | 时间点。 |
| `subSalesRank[].ranks[].value` | string | 数值。 |
| `reviews[]` | array | 评分数趋势数据。 |
| `reviews[].timePoint` | string | 时间点。 |
| `reviews[].value` | string | 数值。 |
| `rating[]` | array | 评分值趋势数据。 |
| `rating[].timePoint` | string | 时间点。 |
| `rating[].value` | string | 数值。 |
| `sellers[]` | array | 卖家数趋势数据。 |
| `sellers[].timePoint` | string | 时间点。 |
| `sellers[].value` | string | 数值。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keepa-info" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin":"B08GHW4TBS","marketplace":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
