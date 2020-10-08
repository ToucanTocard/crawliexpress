from crawliexpress import Client
from pprint import pprint

client = Client("https://www.aliexpress.com")
item = client.get_item("4000505787173")
pprint(vars(item))
