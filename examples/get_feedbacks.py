from crawliexpress import Client

from pprint import pprint
from time import sleep

client = Client("https://fr.aliexpress.com")
item = client.get_item("20000001708485")

page_no = 1
pages = list()
while True:
    page = client.get_feedbacks(
        item.product_id,
        item.owner_member_id,
        item.company_id,
        with_picture=True,
        page=page_no,
    )
    if page.has_next_page() is False:
        break
    page_no += 1
    sleep(1)
