# Wenmai SellerSprite `product_node` API 参考

查询 Amazon 产品类目信息的工具。。

## 调用规范

- **standard API 地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/product-node`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，兼容 `WENMAI_SECRET_KEY`
- **接口代码**：`product_node`
- **脚本入口**：`scripts/product_node.py`
- **API key 与充值**：https://agent.wenmai-ai.com/

## 请求参数

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `request` | object | 是 | 业务请求对象。 |
| `request.marketplace` | string；可选值：US、JP、UK、DE、FR、IT、ES、CA、IN | 是 | 供应商返回的扩展属性；当前契约未定义可供调用方依赖的稳定业务语义。 |
| `request.nodeIdPath` | string | 否 | 类目节点 id 字符串；示例：2619525011:3741271:3741281。 |
| `request.keyword` | string | 否 | 查询关键词文本；示例：Books 或者 4053。 |
| `request.month` | string | 否 | 查询历史月份类目，格式yyyyMM；示例：202502。 |

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
| `nodeIdPath` | string | 类目 id 字符串，即 nodeIdPath；官方示例值：2619525011:3741271。 |
| `nodeLabelPath` | string | 类目名称；官方示例值：Appliances:Dishwashers。 |
| `products` | integer | 类目下产品数；官方示例值：42。 |
| `nodeLabelLocale` | string | 类目节点名称中文；官方示例值：洗碗机。 |
| `nodeLabelPathLocale` | string | 类目所属所有节点名称中文；官方示例值：大家电:洗碗机。 |

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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/sellersprite/product-node" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"request":{"marketplace":"US"}}'
```

---

来源：Wenmai WMAPI 文档 https://all-api.wenmai-ai.com/wmapi/docs（来源日期：2026-08-05）。
