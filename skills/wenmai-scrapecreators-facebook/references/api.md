# Wenmai SCRAPECREATORS Facebook 套件 API 参考

## 调用规范

- 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要要求用户在对话中粘贴密钥。
- 顶层 Skill 是索引目录，真正请求发到下表 23 个 `/wmapi/v1/scrapecreators/facebook-*` 端点。不要因为套件有 23 个接口就全打一遍。
- 认证：Header `secret-key: $WENMAI_API_KEY`，也兼容 `WENMAI_SECRET_KEY`
- 凭据与充值：在 https://agent.wenmai-ai.com/app/account 获取 `secret-key`
- 稳卖积分：普通接口成功为 2。贵参数会提高官方成本，默认不要开。

## 接口索引

| 子 Skill | 接口代码 | 请求地址 | 稳卖积分 | 详细契约 |
|---|---|---|---|---|
| 获取 Facebook 主页详情 | `scrapecreators_facebook_profile` | `/wmapi/v1/scrapecreators/facebook-profile` | 2 | [modules/profile/references/api.md](../modules/profile/references/api.md) |
| 获取 Facebook 主页 Reels | `scrapecreators_facebook_profile_reels` | `/wmapi/v1/scrapecreators/facebook-profile-reels` | 2 | [modules/profile-reels/references/api.md](../modules/profile-reels/references/api.md) |
| 获取 Facebook 主页相册照片 | `scrapecreators_facebook_profile_photos` | `/wmapi/v1/scrapecreators/facebook-profile-photos` | 2 | [modules/profile-photos/references/api.md](../modules/profile-photos/references/api.md) |
| 获取 Facebook 主页帖子 | `scrapecreators_facebook_profile_posts` | `/wmapi/v1/scrapecreators/facebook-profile-posts` | 2 | [modules/profile-posts/references/api.md](../modules/profile-posts/references/api.md) |
| 获取 Facebook 主页活动 | `scrapecreators_facebook_profile_events` | `/wmapi/v1/scrapecreators/facebook-profile-events` | 2 | [modules/profile-events/references/api.md](../modules/profile-events/references/api.md) |
| 搜索 Facebook 公开视频和 Reels | `scrapecreators_facebook_search_videos` | `/wmapi/v1/scrapecreators/facebook-search-videos` | 2 | [modules/search-videos/references/api.md](../modules/search-videos/references/api.md) |
| 获取 Facebook 帖子或 Reel 详情 | `scrapecreators_facebook_post` | `/wmapi/v1/scrapecreators/facebook-post` | 2 | [modules/post/references/api.md](../modules/post/references/api.md) |
| 获取 Facebook 帖子或 Reel 字幕 | `scrapecreators_facebook_post_transcript` | `/wmapi/v1/scrapecreators/facebook-post-transcript` | 2 | [modules/post-transcript/references/api.md](../modules/post-transcript/references/api.md) |
| 获取 Facebook 帖子评论 | `scrapecreators_facebook_post_comments` | `/wmapi/v1/scrapecreators/facebook-post-comments` | 2 | [modules/post-comments/references/api.md](../modules/post-comments/references/api.md) |
| 获取指定 Facebook 评论的回复 | `scrapecreators_facebook_post_comment_replies` | `/wmapi/v1/scrapecreators/facebook-post-comment-replies` | 2 | [modules/post-comment-replies/references/api.md](../modules/post-comment-replies/references/api.md) |
| 获取 Facebook 公开群组信息 | `scrapecreators_facebook_group` | `/wmapi/v1/scrapecreators/facebook-group` | 2 | [modules/group/references/api.md](../modules/group/references/api.md) |
| 获取 Facebook 公开群组帖子 | `scrapecreators_facebook_group_posts` | `/wmapi/v1/scrapecreators/facebook-group-posts` | 2 | [modules/group-posts/references/api.md](../modules/group-posts/references/api.md) |
| 搜索 Facebook Marketplace 地点 | `scrapecreators_facebook_marketplace_location_search` | `/wmapi/v1/scrapecreators/facebook-marketplace-location-search` | 2 | [modules/marketplace-location-search/references/api.md](../modules/marketplace-location-search/references/api.md) |
| 搜索 Facebook Marketplace 商品 | `scrapecreators_facebook_marketplace_search` | `/wmapi/v1/scrapecreators/facebook-marketplace-search` | 2 | [modules/marketplace-search/references/api.md](../modules/marketplace-search/references/api.md) |
| 获取 Facebook Marketplace 商品详情 | `scrapecreators_facebook_marketplace_item` | `/wmapi/v1/scrapecreators/facebook-marketplace-item` | 2 | [modules/marketplace-item/references/api.md](../modules/marketplace-item/references/api.md) |
| 搜索 Facebook 活动 | `scrapecreators_facebook_events_search` | `/wmapi/v1/scrapecreators/facebook-events-search` | 2 | [modules/events-search/references/api.md](../modules/events-search/references/api.md) |
| 获取某城市 Facebook 活动 | `scrapecreators_facebook_events` | `/wmapi/v1/scrapecreators/facebook-events` | 2 | [modules/events/references/api.md](../modules/events/references/api.md) |
| 获取 Facebook 活动详情 | `scrapecreators_facebook_event_details` | `/wmapi/v1/scrapecreators/facebook-event-details` | 2 | [modules/event-details/references/api.md](../modules/event-details/references/api.md) |
| 获取 Facebook 广告库广告详情 | `scrapecreators_facebook_ad_library_ad` | `/wmapi/v1/scrapecreators/facebook-ad-library-ad` | 2 | [modules/ad-library-ad/references/api.md](../modules/ad-library-ad/references/api.md) |
| 获取 Facebook 广告库视频字幕 | `scrapecreators_facebook_ad_library_ad_transcript` | `/wmapi/v1/scrapecreators/facebook-ad-library-ad-transcript` | 2 | [modules/ad-library-ad-transcript/references/api.md](../modules/ad-library-ad-transcript/references/api.md) |
| 按关键词搜索 Facebook 广告库 | `scrapecreators_facebook_ad_library_search_ads` | `/wmapi/v1/scrapecreators/facebook-ad-library-search-ads` | 2 | [modules/ad-library-search-ads/references/api.md](../modules/ad-library-search-ads/references/api.md) |
| 获取某公司在 Facebook 广告库的在投广告 | `scrapecreators_facebook_ad_library_company_ads` | `/wmapi/v1/scrapecreators/facebook-ad-library-company-ads` | 2 | [modules/ad-library-company-ads/references/api.md](../modules/ad-library-company-ads/references/api.md) |
| 在 Facebook 广告库搜索广告主 | `scrapecreators_facebook_ad_library_search_companies` | `/wmapi/v1/scrapecreators/facebook-ad-library-search-companies` | 2 | [modules/ad-library-search-companies/references/api.md](../modules/ad-library-search-companies/references/api.md) |

每个子 Skill 的请求参数、响应字段、示例和 curl 写在对应模块的 `references/api.md`，不要在索引页发明字段。

## 错误处理

| 场景 | 处理建议 |
|---|---|
| 缺少 API Key | 先自主检查当前进程环境变量 `WENMAI_API_KEY`，未获取到时再检查 `WENMAI_SECRET_KEY`；仅当两个环境变量都未获取到时，才提示用户在本机配置。不得在未检查环境变量的情况下声称缺少 API Key，也不要在文件、日志或对话中写入密钥。 |
| 余额或额度不足 | 前往 https://agent.wenmai-ai.com/app/account 充值。 |
| 参数错误 | 打开对应子 Skill 的 `references/api.md` 核对必填字段、主页/帖子链接、pageId、商品/广告 ID 和 cursor。 |
| HTTP 或网关错误 | 保留状态码、`requestId` 和脱敏后的错误消息用于排查。 |

---

来源：ScrapeCreators 官方页面及 OpenAPI 成功响应示例（采集日期：2026-11-26），不是本次线上实测记录。各模块的官方来源链接见对应接口参考。响应表相对网关外层 `data` 展开，`[]` 表示数组元素；官方响应自带的内层 `data` 保留原名。仅为 null、空数组或空对象的字段不推测非空类型或子字段。字段来自多个官方成功样例的并集，不代表所有请求或 `trim=true` 都会返回全部字段，也不据示例声明必填。官方未提供独立解释的字段已明确标注。对外仍隐藏 `credits_remaining`、`credits_charged`。
