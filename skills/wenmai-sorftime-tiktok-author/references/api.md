# Wenmai Sorftime `tiktok_author` API 参考

达人搜索。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/tiktok-author`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`tiktok_author`
- **脚本入口**：`scripts/tiktok_author.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `author_id` | String | 是 | 要查询的达人 ID（实际接受达人昵称，例如 `xmw_us`）。 |

## 请求示例

```json
{
  "author_id": "xmw_us"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.author_category` | String | 达人所属类目（如 购物与零售 / Shopping & Retail）。 |
| `data.author_id` | String | TikTok 达人唯一数字 ID。 |
| `data.author_name` | String | 达人昵称。 |
| `data.avatar` | String | 达人头像 URL。 |
| `data.fans_count` | Integer | 达人当前粉丝数。 |
| `data.is_blue_verified` | Boolean | 达人是否为蓝 V 认证。 |
| `data.is_mcn` | Boolean | 达人是否隶属 MCN。 |
| `data.is_relation_shop` | Boolean | 达人是否绑定关联店铺（带货与店铺绑定）。 |
| `data.like_count` | Integer | 达人累计获赞数。 |
| `data.max_category` | Object | 达人最擅长类目（主类目）。 |
| `data.max_category.name` | String | 类目名称。 |
| `data.max_category.node_id` | String | 类目节点 ID（字符串）。 |
| `data.promo_product_count` | Integer | 达人累计推广的不同商品数。 |
| `data.promo_video_count` | Integer | 达人累计推广视频数。 |
| `data.recent_15_avg_review_count` | Number | 最近 15 条视频的平均评论数（float）。 |
| `data.recent_15_like_interaction_rate` | Number | 最近 15 条视频的点赞互动率（百分比值，0.37 = 0.37%）。 |
| `data.recent_15_review_interaction_rate` | Number | 最近 15 条视频的评论互动率（百分比值，0.01 = 0.01%）。 |
| `data.recent_15_video_avg_likes` | Number | 最近 15 条视频的平均点赞数（float）。 |
| `data.recent_15_video_avg_views` | Number | 最近 15 条视频的平均播放数（float）。 |
| `data.recent_30_day_fans_growth` | Integer | 近 30 天净增粉丝数（可为负）。 |
| `data.recent_30_day_like_count` | Integer | 近 30 天获得的点赞数。 |
| `data.recent_30_day_new_promo_count` | Integer | 近 30 天新推广的不同商品数。 |
| `data.recent_30_day_video_count` | Integer | 近 30 天发布的视频数。 |
| `data.second_category` | Object | 达人第二擅长类目，无数据时 name/node_id 为空字符串。 |
| `data.second_category.name` | String | 类目名称。 |
| `data.second_category.node_id` | String | 类目节点 ID。 |
| `data.third_category` | Object | 达人第三擅长类目，无数据时 name/node_id 为空字符串。 |
| `data.third_category.name` | String | 类目名称。 |
| `data.third_category.node_id` | String | 类目节点 ID。 |
| `data.video_count` | Integer | 达人累计发布视频数。 |

## 使用要点

- 必填字段：`author_id`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/tiktok-author" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id":"xmw_us"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。
