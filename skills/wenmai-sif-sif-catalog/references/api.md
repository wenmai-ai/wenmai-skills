# Wenmai SIF `sif_catalog` API 参考

返回 SIF 可用接口的分类目录。触发时机：用户询问'有哪些工具' / '能做什么' / '功能列表' / '工具介绍' 时使用。返回内容按大类组织。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/sif-catalog`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`sif_catalog`
- **脚本入口**：`scripts/sif_catalog.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `body` | object | 否 | 请求体按接口参数传入。 |

## 请求示例

```json
{}
```

## 响应结构

Wenmai 网关外层通常包含 `code`、`message`、`requestId`、`supplier`、`apiCode` 和 `data`。下表忠实保留源文档列出的业务字段。

| 字段 | 类型 | 说明 |
|---|---|---|
| `title` | string | 记录的展示标题。 |
| `categories[]` | array | 工具目录中的一级分类列表。 |
| `categories[].category` | string | 类目。 |
| `categories[].description` | string | 说明。 |
| `categories[].tools[]` | array | 一级分类直接包含的工具列表。 |
| `categories[].tools[].tool` | string | 工具名称。 |
| `categories[].tools[].summary` | string | 摘要。 |
| `categories[].subcategories[]` | array | 一级分类下的子分类列表。 |
| `categories[].subcategories[].subcategory` | string | 子分类名称。 |
| `categories[].subcategories[].description` | string | 说明。 |
| `categories[].subcategories[].tools[]` | array | 子分类包含的工具列表。 |
| `categories[].subcategories[].tools[].tool` | string | 工具名称。 |
| `categories[].subcategories[].tools[].summary` | string | 摘要。 |
| `tip` | string | 使用提示。 |

## 使用要点

- 必填字段：无。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sif/sif-catalog" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
