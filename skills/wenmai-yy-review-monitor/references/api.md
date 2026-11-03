# Wenmai 数据Amazon 评论抓取 API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/yy/{接口路径}`，4 个固定接口见下表
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 在 https://agent.wenmai-ai.com/app/account 的个人中心获取，充值也在同一入口完成。
- **脚本入口**：每个接口一个脚本，脚本参数即标准 API POST Body JSON；`scripts/crawl_reviews.py` 串联提交、轮询和取评论。

| 接口 | 接口编码 | 路径 | 脚本 |
|------|----------|------|------|
| 添加评论监控 ASIN | `yy_add_review_monitor_asins` | `POST /wmapi/v1/yy/add-review-monitor-asins` | `scripts/add_review_monitor_asins.py` |
| 查询评论监控任务 | `yy_get_review_monitor_tasks` | `POST /wmapi/v1/yy/get-review-monitor-tasks` | `scripts/get_review_monitor_tasks.py` |
| 获取评论监控数据 | `yy_get_monitor_asin_reviews` | `POST /wmapi/v1/yy/get-monitor-asin-reviews` | `scripts/get_monitor_asin_reviews.py` |
| 查询评论任务抓取次数 | `yy_get_review_crawl_count` | `POST /wmapi/v1/yy/get-review-crawl-count` | `scripts/get_review_crawl_count.py` |

### 运行时覆盖

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `WENMAI_API_ORIGIN` | Wenmai API 地址 | `https://all-api.wenmai-ai.com` |
| `WENMAI_API_BASE_PATH` | 标准 API Base Path | `/wmapi/v1` |
| `WENMAI_API_TIMEOUT` | 单次 HTTP 超时时间，单位秒 | `120` |
| `WENMAI_REVIEW_POLL_SECONDS` | `crawl_reviews.py` 查询任务状态的间隔，单位秒 | `30` |
| `WENMAI_REVIEW_WAIT_SECONDS` | `crawl_reviews.py` 等待抓取完成的最长时间，单位秒 | `600` |

## 调用流程

评论抓取是异步任务：
1. 调用「添加评论监控 ASIN」提交 1 个 ASIN，返回评论任务 ID（`aid`）。
2. 调用「查询评论监控任务」轮询该 `aid`，直到 `has_rel=2`（抓取完成）。`has_rel`：0 未抓取，1 抓取中，2 抓取完成。
3. 调用「获取评论监控数据」按 `aid` 取评论，可按评论日期、星级筛选。
4. 需要核对抓取情况时，调用「查询评论任务抓取次数」。

实测参考（2026-10-30）：
- `review_end_num` 传 N 即抓 N 页，每页 10 条，按评论时间从新到旧；1 页返回 10 条，3 页返回 30 条（第 1～3 页）。评论不足时最后一页可能少于 10 条。
- `format_restrict=0`（默认）返回所传 ASIN 所属 listing 全部变体的评论，每条评论的 `review_asin`、`format_text` 标明所属变体；`format_restrict=1` 只返回所传 ASIN 这个变体本身的评论。个别评论在 Amazon 上没有规格信息，这两个字段为空字符串。
- 任务从提交到 `has_rel=2` 通常 1.5～2.5 分钟；不同优先级、页数差异不明显。建议每 30 秒查询一次，超过 10 分钟未完成再提示用户稍后查询。
- 提交按申请页数计费（`review_end_num`，未传按 1 页）；查询类接口按次计费，避免过于频繁地轮询。

## 添加评论监控 ASIN（`/wmapi/v1/yy/add-review-monitor-asins`）

提交 1 个需要抓取评论的 Amazon ASIN，返回评论任务 ID（aid）。抓取为异步任务：用「查询评论监控任务」轮询到 has_rel=2 后，再用「获取评论监控数据」取评论。按 review_end_num 抓取页数（每页 10 条，从新到旧，默认 1 页，最多 10 页），按页计费。

### 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `station` | string | 是 | 站点名：1 美国站；2 意大利站；3 日本站；4 德国站；5 英国站；6 法国站；7 西班牙站；8 加拿大站；9 墨西哥站；10 荷兰站；11 波兰站；12 瑞典站；13 澳大利亚站；14 沙特；15 阿联酋；16 新加坡；17巴西；18土耳其；19比利时；20印度；一次调用最多一个站点 |
| `asins` | array<string> | 是 | Amazon ASIN，单次只能提交 1 个（按该 ASIN 申请的页数计费）；最多 1 个 |
| `craw_all_review` | integer | 否 | 是否抓取全部评论：1 全部；0 增量（默认）。抓取页数仍受 review_end_num 限制；可选值：0、1 |
| `review_date_start` | string | 否 | 评论起始日期(string型 格式:年-月-日)；(不填，默认不限时间) |
| `collect_source` | string | 否 | 抓取方式(string型 默认:pc)；可选值：pc、mobile |
| `language` | string | 否 | 若为空则默认语言；en 英文；(目前只支持默认和en)；可选值：en |
| `site_restrict` | integer | 否 | 站点限制；0不限制；1限制只抓取当前站点评论；可选值：0、1 |
| `format_restrict` | integer | 否 | 变体范围：0（默认）返回所传 ASIN 所属 listing 全部变体的评论，每条评论通过 review_asin、format_text 标明所属变体；1 只返回所传 ASIN 这个变体本身的评论；可选值：0、1 |
| `priority` | integer | 否 | 优先级 (不填,默认为0)；普通任务 0， 快抓取任务1-100；取值 0~100 |
| `review_end_num` | integer | 否 | 抓取页数，每页 10 条，按评论时间从新到旧抓取（例如传 10 最多返回 100 条）；不传默认 1 页，小于 1 按 1、大于 10 按 10 处理；按页计费；取值 1~10 |

### 请求示例

```json
{
  "station": "1",
  "asins": [
    "B085DTZQNZ"
  ],
  "review_end_num": 2,
  "format_restrict": 0
}
```

### 响应字段

公共响应字段：`code`、`message`、`requestId`、`costCredit`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `status` | string | 接口状态：success 成功；error 失败（失败时标准 API 直接返回错误，不会出现在 data 中） |
| `code` | integer | YY状态码，200 表示成功 |
| `size` | integer | 本次返回的结果数量 |
| `total_size` | integer | 符合条件的结果总数 |
| `no_more_data` | boolean | 是否没有更多数据；false 表示还有下一页 |
| `result[]` | array<object> | 结果集 |
| `result[].aid` | integer | 唯一标识aid |
| `result[].asin` | string | 商品id |
| `result[].station` | integer | 站点；1 美国站 2 意大利站；3 日本站 4 德国站；5 英国站 6 法国站；7 西班牙站 8 加拿大站；9 墨西哥站 10 荷兰站；11 波兰站 12 瑞典站；13 澳大利亚站 14 沙特；15 阿联酋 16 新加坡 |
| `result[].status` | string | 添加状态(true或false) |
| `result[].collect_source` | string | 抓取方式；pc 或者mobile |
| `result[].language` | string | 指定抓取语言，为空则平台默认语言 |
| `result[].format_restrict` | string | 0 无限制抓取任务asin所属listing全部格式的全部评论(默认)；1 限制只抓取任务asin对应格式的asin |

## 查询评论监控任务（`/wmapi/v1/yy/get-review-monitor-tasks`）

按评论任务 ID（aid）查询抓取状态：has_rel=0 未抓取、1 抓取中、2 抓取完成；抓取完成后返回评分、评分数、评论数等汇总信息。

### 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `aids` | array<integer> | 是 | 监控唯一id(单次最多100个)；最多 100 个 |

### 请求示例

```json
{
  "aids": [
    67041432
  ]
}
```

### 响应字段

公共响应字段：`code`、`message`、`requestId`、`costCredit`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `status` | string | 接口状态：success 成功；error 失败（失败时标准 API 直接返回错误，不会出现在 data 中） |
| `code` | integer | YY状态码，200 表示成功 |
| `size` | integer | 本次返回的结果数量 |
| `total_size` | integer | 符合条件的结果总数 |
| `no_more_data` | boolean | 是否没有更多数据；false 表示还有下一页 |
| `result[]` | array<object> | 结果集 |
| `result[].id` | integer | 监控唯一id |
| `result[].station` | string | 站点；1 美国站 2 意大利站；3 日本站 4 德国站；5 英国站 6 法国站；7 西班牙 8 加拿大；9 墨西哥 10 荷兰；11 波兰 12 瑞典；13 澳大利亚 14沙特；15阿联酋 16新加坡 |
| `result[].asin` | string | 产品asin |
| `result[].filter_by` | string | 查询结果中固定返回 null（官方已标注取消）；以 request_param 为准 |
| `result[].review_end_date` | string | 评论截止日期(默认空 表示无截止日期) |
| `result[].site_restrict` | string | 查询结果中固定返回 null（官方已标注取消）；以 request_param 为准 |
| `result[].format_restrict` | string | 查询结果中固定返回 null（官方已标注取消）；任务实际的变体范围以 request_param 中的 format_restrict 为准 |
| `result[].created_at` | string | 任务创建时间 |
| `result[].last_upd_date` | string | 任务结束时间 |
| `result[].has_rel` | integer | 爬取状态；0：未抓取；1：正在抓取；2：抓取完成 |
| `result[].score` | string | 星级评分 |
| `result[].rating_cnt` | integer | 整个 listing 的评分总数；format_restrict=1 时为 0；未抓取时为 null |
| `result[].review_info` | string | review分布信息 |
| `result[].rev_cnt` | integer | Amazon 页面展示的评论数：listing 评论超过 1 万时为 10000；format_restrict=1 时为该变体的匹配评论数；未抓取时为 null |
| `result[].task_status` | string | 任务状态 |
| `result[].request_param` | string | 请求参数 |
| `result[].rating_str` | string | Amazon 页面上的评论数文字，例如「More than 10,000 customer reviews」「1,560 matching customer reviews」 |
| `result[].title` | string | 商品标题（官方标注已取消，通常为 null） |
| `result[].img_url` | string | 商品图片链接（官方标注已取消，通常为 null） |
| `result[].page_num` | integer | 本任务实际抓取的页数（每页 10 条）；未抓取时为 0 |
| `result[].collect_source` | string | 抓取方式；pc 或者mobile |
| `result[].not_exist` | integer | asin状态；0 上架 1下架 |
| `result[].language` | string | 指定抓取语言，为空则平台默认语言 |

## 获取评论监控数据（`/wmapi/v1/yy/get-monitor-asin-reviews`）

按评论任务 ID（aid）获取已抓取的评论，可按评论日期和星级筛选。需在任务 has_rel=2 后调用，否则 reviews 为空。

### 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `aids` | array<integer> | 是 | 监控唯一id(单次最多100个)；最多 100 个 |
| `review_date_start` | string | 否 | 评论日期起始值(string型 格式:年-月-日) |
| `review_date_end` | string | 否 | 评论日期结束值(string型 格式:年-月-日) |
| `star_start` | number | 否 | 评论打分起始值；取值 1~5 |
| `star_end` | number | 否 | 评论打分结束值；取值 1~5 |

### 请求示例

```json
{
  "aids": [
    67041432
  ],
  "review_date_start": "2026-01-01",
  "review_date_end": "2026-10-29",
  "star_start": 1,
  "star_end": 5
}
```

### 响应字段

公共响应字段：`code`、`message`、`requestId`、`costCredit`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `status` | string | 接口状态：success 成功；error 失败（失败时标准 API 直接返回错误，不会出现在 data 中） |
| `code` | integer | YY状态码，200 表示成功 |
| `size` | integer | 本次返回的结果数量 |
| `total_size` | integer | 符合条件的结果总数 |
| `no_more_data` | boolean | 是否没有更多数据；false 表示还有下一页 |
| `result[]` | array<object> | 结果集 |
| `result[].aid` | integer | 唯一标识id |
| `result[].score` | string | 星级评分 |
| `result[].rating_cnt` | integer | 整个 listing 的评分总数；format_restrict=1 时为 0 |
| `result[].review_info` | string | review分布信息 |
| `result[].rev_cnt` | integer | Amazon 页面展示的评论数：listing 评论超过 1 万时为 10000；format_restrict=1 时为该变体的匹配评论数 |
| `result[].rating_str` | string | Amazon 页面上的评论数文字，例如「More than 10,000 customer reviews」「1,560 matching customer reviews」 |
| `result[].title` | string | 商品标题（官方标注已取消，通常为 null） |
| `result[].img_url` | string | 商品图片链接（官方标注已取消，通常为 null） |
| `result[].page_num` | integer | 本任务实际抓取的页数（每页 10 条） |
| `result[].collect_source` | string | 抓取方式；pc 或者mobile |
| `result[].not_exist` | integer | asin状态；0 上架 1下架 |
| `result[].language` | string | 指定抓取语言，为空则平台默认语言 |
| `result[].reviews[]` | array<object> | 商品评论数据（评论任务抓取完成（has_rel=2）后返回） |
| `result[].reviews[].asin` | string | 商品asin |
| `result[].reviews[].station` | integer | 商品站点；1 美国站 2 意大利站；3 日本站 4 德国站；5 英国站 6 法国站；7 西班牙站 8 加拿大站；9 墨西哥站 10 荷兰站；11 波兰站 12 瑞典站；13 澳大利亚站 14 沙特；15 阿联酋 16 新加坡 |
| `result[].reviews[].reviews_id` | string | 评论id |
| `result[].reviews[].reviews_title` | string | 评论标题 |
| `result[].reviews[].reviews` | string | 商品评论数据 |
| `result[].reviews[].review_img` | string | 评论图片地址 |
| `result[].reviews[].star` | number | 评论打分 |
| `result[].reviews[].star_level` | string | 评论打分文本 |
| `result[].reviews[].write_by` | string | 评论用户名 |
| `result[].reviews[].author_id` | string | 评论用户id |
| `result[].reviews[].customer_url` | string | 评论用户主页地址 |
| `result[].reviews[].review_date` | string | 评论日期 |
| `result[].reviews[].v_purchase` | integer | 是否是Verified Purchase；0:否 1:是 |
| `result[].reviews[].helpful_vote` | integer | 是否 helpful_vote；0否 1是 |
| `result[].reviews[].review_asin` | string | 评论对应的子体 ASIN。format_restrict=0 时可能是同一 listing 的其他变体，可据此区分变体；个别评论为空字符串（无法归属变体）：抓取时 Amazon 页面上这条评论还没显示规格（如新上架的子体），之后 Amazon 补上规格也不会回填 |
| `result[].reviews[].format_text` | string | 评论对应子体的规格文字，例如「Color: Black Cherry \| Size: 32 Ounces」；与 review_asin 同时为空时无法归属变体 |
| `result[].reviews[].helpful_vote_cnt` | integer | helpful_vote people 数 |
| `result[].reviews[].badges` | string | 标签 |
| `result[].reviews[].vine_badge` | integer | 是否Vine标；0否 1是 |
| `result[].reviews[].hall_badge` | integer | 是否HALL OF FAME；0否 1是 |
| `result[].reviews[].top_badge` | integer | 是否TOP X REVIEWER；0否 1是 |
| `result[].reviews[].page_url` | string | 评论抓取时候所属页面连接 |
| `result[].reviews[].video_url` | string | 视频评论链接 |
| `result[].reviews[].review_country` | string | 评论国家 |

## 查询评论任务抓取次数（`/wmapi/v1/yy/get-review-crawl-count`）

查询评论任务（aid）被抓取的次数，可再按站点、ASIN、任务创建时间缩小范围。

### 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `aids` | array<integer> | 是 | 监控唯一id(单次最多100个)；最多 100 个 |
| `station` | string | 否 | 站点名：1 美国站；2 意大利站；3 日本站；4 德国站；5 英国站；6 法国站；7 西班牙站；8 加拿大站；9 墨西哥站；10 荷兰站；11 波兰站；12 瑞典站；13 澳大利亚站；14 沙特；15 阿联酋；16 新加坡；一次调用最多一个站点 |
| `asins` | array<string> | 否 | 商品id |
| `created_at_start` | string | 否 | 任务创建时间起始值(string型 格式:年-月-日 时:分:秒) |
| `created_at_end` | string | 否 | 任务创建时间结束值(string型 格式:年-月-日 时:分:秒) |

### 请求示例

```json
{
  "aids": [
    67041432
  ]
}
```

### 响应字段

公共响应字段：`code`、`message`、`requestId`、`costCredit`、`supplier`、`apiCode`、`data`。业务字段位于 `data`。

| 字段 | 类型 | 说明 |
|------|------|------|
| `status` | string | 接口状态：success 成功；error 失败（失败时标准 API 直接返回错误，不会出现在 data 中） |
| `code` | integer | YY状态码，200 表示成功 |
| `size` | integer | 本次返回的结果数量 |
| `total_size` | integer | 符合条件的结果总数 |
| `no_more_data` | boolean | 是否没有更多数据；false 表示还有下一页 |
| `result` | integer | 结果集 |

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 到 https://agent.wenmai-ai.com/app/account 的个人中心充值后重试。 |
| 参数错误（如 `REQ_001`） | 按请求参数表修正：提交一次只能 1 个 ASIN；`station` 为站点编号字符串；`aids` 最多 100 个；`review_end_num` 取值 1～10。 |
| 任务长时间 `has_rel=0` | 抓取在供应商侧排队；保留 `aid`，稍后用「查询评论监控任务」继续查询，不要重复提交同一 ASIN。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/yy/add-review-monitor-asins" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"station": "1", "asins": ["B085DTZQNZ"], "review_end_num": 2, "format_restrict": 0}'
```

---
来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（2026-11-03 生成，字段来自 2026-10-30 真实调用）。
