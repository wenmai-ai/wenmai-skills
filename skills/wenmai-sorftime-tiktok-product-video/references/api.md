# Wenmai Sorftime `tiktok_product_video` API 参考

产品带货视频。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/tiktok-product-video`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`tiktok_product_video`
- **脚本入口**：`scripts/tiktok_product_video.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `product_id` | String | 是 | 商品 ID。 |
| `page` | Integer | 否 | 查询结果的页码。默认第 1 页，每页返回 20 条记录。 |
| `site` | String；允许值："US"、"MY"、"PH"、"VN"、"TH"、"ID"、"GB"、"JP" | 是 | TikTok 站点。 实际调用必须明确指定。 |

## 请求示例

```json
{
  "product_id": "1732349647191642367",
  "site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.author` | String | 创作者的 TikTok 昵称（如 asggkl71，对应 @asggkl71）。 |
| `data.author_fans_count` | Integer | 创作者的粉丝数。 |
| `data.like_count` | Integer | 视频点赞数。 |
| `data.tag` | String | 视频话题标签，逗号分隔（每个以 # 开头）。 |
| `data.title` | String | 视频标题。 |
| `data.url` | String | TikTok 视频 URL。 |
| `data.video_publish_time` | String | 视频发布时间，格式 yyyy-MM-dd HH:mm:ss。 |
| `data.view_count` | Integer | 视频播放数。 |

## 使用要点

- 必填字段：`product_id`, `site`。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/tiktok-product-video" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id":"1732349647191642367","site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。
