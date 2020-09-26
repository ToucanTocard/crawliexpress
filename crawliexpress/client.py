from crawliexpress.item import Item
from crawliexpress.feedback_page import FeedbackPage

import requests
import urllib


class Client:
    base_url = None
    feedback_url = "https://feedback.aliexpress.com/display/productEvaluation.htm"

    def __init__(self, base_url):
        self.base_url = base_url

    def get_item(self, item_id):
        r = requests.get(f"{self.base_url}/item/{item_id}.html")
        item = Item()
        item.from_html(r.text)
        return item

    def get_feedbacks(
        self,
        product_id,
        owner_member_id,
        company_id=None,
        v=2,
        member_type="seller",
        page=1,
        with_picture=False,
    ):
        params = urllib.parse.urlencode(
            {
                "productId": product_id,
                "ownerMemberId": owner_member_id,
                "companyId": company_id,
                "v": v,
                "memberType": member_type,
                "page": str(page),
                "withPictures": with_picture,
            }
        )
        url = f"{self.feedback_url}?{params}"
        r = requests.get(url)
        feedback_page = FeedbackPage()
        feedback_page.from_html(r.text)
        return feedback_page
