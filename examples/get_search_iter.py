from crawliexpress import Client, Search

from time import sleep

client = Client(
    "https://www.aliexpress.com",
    # copy it from your browser cookies
    "xxxx",
)

search = Search(client, "akame ga kill")
for page in search:
    print(page.page)
    sleep(1)
