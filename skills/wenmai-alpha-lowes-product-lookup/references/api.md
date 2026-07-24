# Wenmai Alpha Lowes Product Lookup API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/lowes-product-lookup`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_lowes_product_lookup`
- **接口说明**：Lowes Product Lookup
- **脚本入口**：`scripts/alpha_lowes_product_lookup.py`，脚本参数即标准 API POST Body JSON

### 运行时覆盖

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `WENMAI_API_ORIGIN` | Wenmai API 地址 | `https://all-api.wenmai-ai.com` |
| `WENMAI_API_BASE_PATH` | 标准 API Base Path | `/wmapi/v1` |
| `WENMAI_API_TIMEOUT` | HTTP 超时时间，单位秒 | `120` |

## 请求参数

POST Body（JSON）：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `zip` | string | 否 | zip 字段。 |
| `productId` | string | 否 | ID 标识。 |

## 请求示例

脚本入参示例：

```json
{
  "zip": "10918",
  "productId": "3131025"
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `asyncId` | number | ID 标识。 |
| `stores` | string | 店铺信息。 |
| `stores.2685` | string | 2685 字段。 |
| `stores.2685.id` | number | ID 标识。 |
| `stores.2685.name` | string | 名称。 |
| `stores.2685.address` | string | address 字段。 |
| `stores.2685.city` | string | city 字段。 |
| `stores.2685.state` | string | state 字段。 |
| `stores.2685.zip` | string | zip 字段。 |
| `stores.2685.phone` | string | phone 字段。 |
| `stores.2685.distance` | boolean | distance 字段。 |
| `stores.2685.hours` | string | hours 字段。 |
| `stores.2685.hours.mon` | string | mon 字段。 |
| `stores.2685.hours.mon.open` | string | open 字段。 |
| `stores.2685.hours.mon.close` | string | close 字段。 |
| `stores.2685.hours.tue` | string | tue 字段。 |
| `stores.2685.hours.tue.open` | string | open 字段。 |
| `stores.2685.hours.tue.close` | string | close 字段。 |
| `stores.2685.hours.wed` | string | wed 字段。 |
| `stores.2685.hours.wed.open` | string | open 字段。 |
| `stores.2685.hours.wed.close` | string | close 字段。 |
| `stores.2685.hours.thu` | string | thu 字段。 |
| `stores.2685.hours.thu.open` | string | open 字段。 |
| `stores.2685.hours.thu.close` | string | close 字段。 |
| `stores.2685.hours.fri` | string | fri 字段。 |
| `stores.2685.hours.fri.open` | string | open 字段。 |
| `stores.2685.hours.fri.close` | string | close 字段。 |
| `stores.2685.hours.sat` | string | sat 字段。 |
| `stores.2685.hours.sat.open` | string | open 字段。 |
| `stores.2685.hours.sat.close` | string | close 字段。 |
| `stores.2685.hours.sun` | string | sun 字段。 |
| `stores.2685.hours.sun.open` | string | open 字段。 |
| `stores.2685.hours.sun.close` | string | close 字段。 |
| `stores.2685.products` | array | products 字段。 |
| `stores.2685.products.3131025` | array | 3131025 字段。 |
| `stores.2685.products.3131025.name` | array | 名称。 |
| `stores.2685.products.3131025.description` | array | 描述。 |
| `stores.2685.products.3131025.url` | array | 链接地址。 |
| `stores.2685.products.3131025.imageUrl` | array | 链接地址。 |
| `stores.2685.products.3131025.quantityAvailable` | number | 库存信息。 |
| `stores.2685.products.3131025.priceCentsPerUnit` | number | 价格。 |
| `stores.2685.products.3131025.salePriceCentsPerUnit` | number | 价格。 |
| `stores.2685.products.3131025.bulkQuantityRequired` | number | bulkQuantityRequired 字段。 |
| `stores.2685.products.3131025.bulkPriceCentsPerUnit` | number | 价格。 |

## 使用要点

- 本接口适合：Lowes 商品查询。
- 优先使用用户给定的 URL、关键词、商品 ID、站点、国家、语言、排序、分页和数量限制。
- 采集类接口的字段会随目标平台页面结构变化；输出分析时保留原始字段名和 URL，避免把缺失字段补写成事实。
- 当用户需要多平台对比时，分别调用对应 Alpha 原子 Skill，再在上层分析中合并结果。

## 错误处理

| 场景 | 处理建议 |
|------|----------|
| 缺少 API Key | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 获取 secret-key，并设置为 `WENMAI_API_KEY`（或 `WENMAI_SECRET_KEY`）；不要把 Key 写进 Skill 文件或对话。 |
| 余额或额度不足 | 参考 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html 完成充值后重试。 |
| 参数错误 | 按上方请求参数表修正枚举值、日期格式、分页范围、URL/关键词数组、数量范围或必填字段。 |
| 非 OK 响应 | 读取响应 `message` 与 `requestId`，按接口文档或联系网关排查。 |

## curl 示例

```bash
curl -sS -X POST \
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/lowes-product-lookup" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"zip": "10918", "productId": "3131025"}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。
