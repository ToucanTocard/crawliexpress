from crawliexpress.exceptions import (
    CrawliexpressException,
    CrawliexpressCaptchaException,
)
from crawliexpress.item import Item
from crawliexpress.feedback_page import FeedbackPage
from crawliexpress.search_page import SearchPage

import requests
import urllib


FEEDBACK_URL = "https://feedback.aliexpress.com/display/productEvaluation.htm"


class Client:

    """
    Exposes methods to fetch various resources.

    :param base_url: allows to change locale (not sure about this one)
    :param xman_t: must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls
    :param x5sec: must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls
    :param aep_usuc_f: must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls
    """

    base_url = None

    # cookies to avoid capcha
    xman_t = None
    x5sec = None

    # cookies for category search
    aep_usuc_f = None

    def __init__(self, base_url, xman_t=None, x5sec=None, aep_usuc_f=None):

        self.base_url = base_url
        self.xman_t = xman_t
        self.x5sec = x5sec
        self.aep_usuc_f = aep_usuc_f

    def __analyze_response(self, response):
        if response.status_code != 200:
            raise CrawliexpressException(f"invalid status code {response.status_code}")
        elif (
            not response.headers["Content-Type"].startswith("application/json")
            and "captcha" in response.text
        ):
            raise CrawliexpressCaptchaException()

    def get_item(self, item_id):

        """
        Fetches a product informations from its id

        :param item_id: id of the product to fetch, item id of https://fr.aliexpress.com/item/20000001708485.html is 20000001708485
        :return: a product
        :rtype: Crawliexpress.Item
        :raises CrawliexpressException: if there was an error fetching the dataz
        """

        r = requests.get(f"{self.base_url}/item/{item_id}.html")
        self.__analyze_response(r)
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

        """
        Fetches a product feedback page

        :param product_id: id of the product, item id of https://fr.aliexpress.com/item/20000001708485.html is 20000001708485
        :param owner_member_id: member id of the product owner, as stored in **Crawliexpress.Item.owner_member_id**
        :param page: page number
        :param with_picture: limit to feedbacks with a picture
        :return: a feedback page
        :rtype: Crawliexpress.FeedbackPage
        :raises CrawliexpressException: if there was an error fetching the dataz
        """

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
        url = f"{FEEDBACK_URL}?{params}"
        r = requests.get(url)
        self.__analyze_response(r)
        feedback_page = FeedbackPage()
        feedback_page.from_html(r.text)
        return feedback_page

    def get_search(self, page_no=1, category_id=0, search_text=None, sort_by="default"):

        """
        Fetches a search page

        :param page_no: page number
        :param category_id: id of the category, category id of https://fr.aliexpress.com/category/205000221/t-shirts.html is 205000221
        :param search_text: text search
        :param sort_by: indeed
        :type sort_by:
            **default**: best match
            **total_tranpro_desc**: number of orders
        :return: a search page
        :rtype: Crawliexpress.SearchPage
        :raises CrawliexpressException: if there was an error fetching the dataz
        :raises CrawliexpressCaptchaException: if there is a captcha, make sure to use valid **xman_t, x5sec, aep_usuc_f** cookie values to avoid this
        """

        params = {
            "trafficChannel": "main",
            "d": "y",
            "CatId": category_id,
            "ltype": "wholesale",
            "SortType": sort_by,
            "page": page_no,
            "origin": "y",
            "isrefine": "y",
        }
        if search_text is not None:
            params["SearchText"] = search_text
        params = urllib.parse.urlencode(params)
        url = f"{self.base_url}/glosearch/api/product?{params}"
        headers = {"Accept": "application/json"}
        cookies = {
            "xman_t": self.xman_t,
            "x5sec": self.x5sec,
            "aep_usuc_f": self.aep_usuc_f,
        }
        r = requests.get(url, headers=headers, cookies=cookies)
        self.__analyze_response(r)
        search_page = SearchPage()
        search_page.from_json(page_no, r.json())
        return search_page
