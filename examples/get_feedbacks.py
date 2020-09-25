from crawliexpress import Client

from pprint import pprint

client = Client("https://fr.aliexpress.com")
item = client.get_item("20000001708485")
feedbacks = client.get_feedbacks(item.product_id, item.owner_member_id, item.company_id)

print(feedbacks)
