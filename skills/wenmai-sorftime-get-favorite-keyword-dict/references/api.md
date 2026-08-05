# Wenmai Sorftime `get_favorite_keyword_dict` API 参考

查询收藏夹列表。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/get-favorite-keyword-dict`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`get_favorite_keyword_dict`
- **脚本入口**：`scripts/get_favorite_keyword_dict.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword_support_site` | String；允许值："US"、"GB"、"DE"、"FR"、"CA"、"JP"、"ES"、"IT"、"MX"、"AE"、"AU"、"BR"、"SA" | 是 | Amazon 商城站点。允许值：US、GB、DE、FR、CA、JP、ES、IT、MX、AE、AU、BR、SA。 实际调用必须明确指定。 |
| `page` | Number | 否 | 查询结果的页码。默认 1，每页返回 100 条记录。 |

## 请求示例

```json
{
  "keyword_support_site": "US"
}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `data.code` | Integer | API 状态码；0 表示成功。 |
| `data.data[]` | Array | 文件夹名字符串数组，即当前账号下所有关键词收藏夹文件夹名称的列表。 |

## 使用要点

- 必填字段：`keyword_support_site`。
- 保留源文档字段名、类型和层级；数组字段以 `[]` 标识。
- 结果摘要必须保留到原始响应字段的映射，不推断缺失值。
- **远程状态变更**：此操作会修改远程状态；执行前必须向用户复核最终完整请求，确认全部目标/作用域字段 `keyword_support_site`, `page`；可选字段未提供时也必须确认采用上游默认作用域。


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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sorftime/get-favorite-keyword-dict" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword_support_site":"US"}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-07-27）。
