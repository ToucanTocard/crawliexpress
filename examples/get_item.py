from crawliexpress import Client

client = Client("https://www.aliexpress.com")
item = client.get_item("4000505787173")
print(dict(item))
