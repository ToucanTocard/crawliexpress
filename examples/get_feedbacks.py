from crawliexpress import Client

from pprint import pprint
from time import sleep

client = Client("https://www.aliexpress.com")
item = client.get_item("20000001708485")

page = 1
pages = list()
while True:
    feedback_page = client.get_feedbacks(
        item.product_id,
        item.owner_member_id,
        item.company_id,
        with_picture=True,
        page=page,
    )
    print(feedback_page.page)
    if feedback_page.has_next_page() is False:
        break
    page += 1
    sleep(1)
