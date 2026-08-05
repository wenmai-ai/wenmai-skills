# Wenmai SellerSprite `keyword_order` API 参考

基于 ASIN 的关键词反查工具，用于分析某个或多个 ASIN。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keyword-order`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`keyword_order`
- **脚本入口**：`scripts/keyword_order.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `request.asins` | array | 是 | asin列表，最大20；示例：B07Z82895W。 |
| `request.reverseType` | string | 是 | 反查模式 W-周 M-月；示例：W。 |
| `request.date` | string | 否 | 查询日期，按周查，格式为yyyMMdd该周最后一天，按月查询yyyyMM；示例：周：20241109月：202411。 |
| `request.conversionType` | array<string>；元素可选值：E、S、L、I | 否 | 转化类型：E：转化优质词，S：转化平稳词，L：转化流失词，I：无效曝光词；示例：E。 |
| `request.variation` | array<string>；元素可选值：Y、N | 否 | 是否查询变体asin：Y:否 N:是；示例：Y。 |
| `request.page` | integer | 否 | 当前页；默认1。 |
| `request.size` | integer | 否 | 每页显示多少条；示例：固定50。 |
| `request.order` | object | 否 | 排序配置对象。 |
| `request.order.field` | string | 否 | 请求指定的排序字段；允许值由具体接口的供应商契约决定。 |
| `request.order.desc` | boolean | 否 | 是否倒序；示例：false。 |

## 请求示例

```json
{
  "request": {
    "date": "2026-03-29",
    "asins": [
      "B08GHW4TBS"
    ],
    "marketplace": "US",
    "reverseType": "W"
  }
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `marketplace` | string | 市场；官方示例值：US。 |
| `keyword` | string | 关键词文本；官方示例值：phone stand for recording。 |
| `keywordCn` | string | 关键词中文翻译；官方示例值：用于录音的电话支架。 |
| `keywordJp` | string | 关键词英文翻译；官方示例值：録音用電話スタンド。 |
| `asin` | string | 所属asin；官方示例值：B0D1FZW65X。 |
| `searches` | integer | 搜索量；官方示例值：21582。 |
| `monopolyClickRate` | number | 点击集中度（官方称“点击垄断率”）；0.3。 |
| `cvsShareRate` | number | 转化共享率；官方示例值：0.3084。 |
| `searchRank` | integer | 搜索排名；官方示例值：17910。 |
| `searchRankGv` | integer | 月变化量；官方示例值：5343。 |
| `searchRankGr` | number | 月变化率；官方示例值：0.3。 |
| `top3ClickingRate` | number | Top3 点击占比；官方示例值：0.0813。 |
| `top3ConversionRate` | number | Top3 转化占比；官方示例值：0.2011。 |
| `conversionType` | string；可选值：E、S、L、I | 转化类型：E：转化优质词，S：转化平稳词，L：转化流失词，I：无效曝光词；官方示例值：E。 |

## 使用要点

- 必填字段：`request`, `request.marketplace`, `request.asins`, `request.reverseType`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/keyword-order" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request":{"date":"2026-03-29","asins":["B08GHW4TBS"],"marketplace":"US","reverseType":"W"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
