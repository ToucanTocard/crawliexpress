import requests
from crawliexpress.item import Item


class Client:
    base_url = None

    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_item(self, item_id):
        r = requests.get(f"{self.base_url}/item/{item_id}.html")
        item = Item()
        item.from_html(r.text)
        return item
