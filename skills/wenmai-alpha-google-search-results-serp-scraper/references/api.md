# Wenmai Alpha Google Search Results Serp Scraper API 参考

## 调用规范

- **请求地址**：`${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/google-search-results-serp-scraper`
- **请求方式**：POST，`Content-Type: application/json`
- **认证方式**：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`；secret-key 获取与充值指引见 https://skill.wenmai-ai.com/wenmaiskills/use_guide.html。
- **接口编码**：`alpha_google_search_results_serp_scraper`
- **接口说明**：Google Search Results (SERP) Scraper
- **脚本入口**：`scripts/alpha_google_search_results_serp_scraper.py`，脚本参数即标准 API POST Body JSON

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
| `keyword` | string | 是 | 搜索关键词。 |
| `include_merged` | boolean | 否 | 是否启用该选项。 |
| `limit` | string | 否 | 最大采集或返回数量。可选值：10、20、30、40、50、100、all。 |
| `start` | integer | 否 | 时间或日期。 |
| `page` | integer | 否 | page 字段。 |
| `country` | string | 否 | 国家或站点。可选值：AF、AL、DZ、AS、AD、AO、AI、AQ、AG、AR、AM、AW、AU、AT、AZ、BS、BH、BD、BB、BY、BE、BZ、BJ、BM、BT、BO、BA、BW、BV、BR、IO、VG、BN、BG、BF、BI、KH、CM、CA、CV、KY、CF、TD、CL、CN、CX、CC、CO、KM、CG、CD、CK、CR、CI、HR、CU、CY、CZ、DK、DJ、DM、DO、EC、EG、SV、GQ、ER、EE、SZ、ET、FK、FO、FJ、FI、FR、GF、PF、TF、GA、GM、等。 |
| `gl` | string | 否 | gl 字段。可选值：AF、AL、DZ、AS、AD、AO、AI、AQ、AG、AR、AM、AW、AU、AT、AZ、BS、BH、BD、BB、BY、BE、BZ、BJ、BM、BT、BO、BA、BW、BV、BR、IO、VG、BN、BG、BF、BI、KH、CM、CA、CV、KY、CF、TD、CL、CN、CX、CC、CO、KM、CG、CD、CK、CR、CI、HR、CU、CY、CZ、DK、DJ、DM、DO、EC、EG、SV、GQ、ER、EE、SZ、ET、FK、FO、FJ、FI、FR、GF、PF、TF、GA、GM、等。 |
| `hl` | string | 否 | hl 字段。可选值：af、ar、hy、be、bg、ca、zh-CN、zh-TW、hr、cs、da、nl、en、eo、et、tl、fi、fr、de、el、iw、hi、hu、is、id、it、ja、ko、lv、lt、no、fa、pl、pt、ro、ru、sr、sk、sl、es、sw、sv、th、tr、uk、vi。 |
| `tbs` | string | 否 | tbs 字段。 |
| `lr` | string | 否 | lr 字段。可选值：lang_af、lang_ar、lang_hy、lang_be、lang_bg、lang_ca、lang_zh-CN、lang_zh-TW、lang_hr、lang_cs、lang_da、lang_nl、lang_en、lang_eo、lang_et、lang_tl、lang_fi、lang_fr、lang_de、lang_el、lang_iw、lang_hi、lang_hu、lang_is、lang_id、lang_it、lang_ja、lang_ko、lang_lv、lang_lt、lang_no、lang_fa、lang_pl、lang_pt、lang_ro、lang_ru、lang_sr、lang_sk、lang_sl、lang_es、lang_sw、lang_sv、lang_th、lang_tr、lang_uk、lang_vi。 |
| `cr` | string | 否 | cr 字段。可选值：countryAF、countryAL、countryDZ、countryAS、countryAD、countryAO、countryAI、countryAQ、countryAG、countryAR、countryAM、countryAW、countryAU、countryAT、countryAZ、countryBS、countryBH、countryBD、countryBB、countryBY、countryBE、countryBZ、countryBJ、countryBM、countryBT、countryBO、countryBA、countryBW、countryBV、countryBR、countryIO、countryVG、countryBN、countryBG、countryBF、countryBI、countryKH、countryCM、countryCA、countryCV、countryKY、countryCF、countryTD、countryCL、countryCN、countryCX、countryCC、countryCO、countryKM、countryCG、countryCD、countryCK、countryCR、countryCI、countryHR、countryCU、countryCY、countryCZ、countryDK、countryDJ、countryDM、countryDO、countryEC、countryEG、countrySV、countryGQ、countryER、countryEE、countrySZ、countryET、countryFK、countryFO、countryFJ、countryFI、countryFR、countryGF、countryPF、countryTF、countryGA、countryGM、等。 |

## 请求示例

脚本入参示例：

```json
{
  "cr": "countryAF",
  "gl": "AF",
  "hl": "af",
  "lr": "lang_af",
  "tbs": "keyboard",
  "page": 10,
  "limit": "all",
  "start": 1,
  "country": "AF",
  "keyword": "nike",
  "include_merged": true
}
```

## 响应结构

Wenmai 标准 API 返回统一响应。成功时 `code` 为 `OK`，业务数据位于 `data`；失败时 `data` 通常为 `null`，错误信息位于 `message`。ALPHA 采集类接口可能同步返回业务字段，也可能返回任务状态、数据集记录或分页字段；以下为该接口文档列出的业务字段。

| 字段 | 类型 | 说明 |
|------|------|------|
| `page_number` | integer | 数量。 |
| `search_term` | string | search_term 字段。 |
| `results` | array | results 字段。 |
| `related_keywords` | object | related_keywords 字段。 |
| `related_keywords.spelling_suggestion` | string | spelling_suggestion 字段。 |
| `related_keywords.keywords` | array | 搜索关键词列表。 |

## 使用要点

- 本接口适合：Google Search / SERP / Trends。
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
  "${WENMAI_API_ORIGIN:-https://all-api.wenmai-ai.com}/wmapi/v1/alpha/google-search-results-serp-scraper" \
  -H "secret-key: $WENMAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cr": "countryAF", "gl": "AF", "hl": "af", "lr": "lang_af", "tbs": "keyboard", "page": 10, "limit": "all", "start": 1, "country": "AF", "keyword": "nike", "include_merged": true}'
```

---

来源：Wenmai WMAPI 文档（生成日期：2026-07-03）。
