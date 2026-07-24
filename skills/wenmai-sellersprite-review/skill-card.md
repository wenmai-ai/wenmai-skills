# 稳卖 SellerSprite review

查询指定 Amazon ASIN 的商品评论列表，返回评论标题、评论内容、评分、评论人、评论时间等信息，用于获取商品的用户反馈和评价数据

- Runtime: Wenmai standard API `POST /wmapi/v1/sellersprite/review`
- Supplier: `SELLERSPRITE`
- API: `review`
- Script: `scripts/review.py`
- Auth: `WENMAI_API_KEY` sent as `secret-key`; see the usage guide at https://skill.wenmai-ai.com/wenmaiskills/use_guide.html to get the key and recharge
