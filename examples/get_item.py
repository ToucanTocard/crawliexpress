from crawliexpress import Client

client = Client("https://fr.aliexpress.com")
item = client.get_item("4000505787173")
print(dict(item))
