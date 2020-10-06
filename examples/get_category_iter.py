from crawliexpress import Client, Category

from time import sleep

client = Client(
    "https://www.aliexpress.com",
    # copy it from your browser cookies
    "xxxx",
)
category = Category(client, 205000314, "t-shirts")

for page in category:
    print(page.page)
    sleep(1)
