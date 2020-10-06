from crawliexpress import Client

from time import sleep

client = Client(
    "https://www.aliexpress.com",
    # copy it from your browser cookies
    "xxxx",
)

page = 1
while True:
    search_page = client.get_search("akame ga kill", page=page)
    print(search_page.page)
    if search_page.has_next_page() is False:
        break
    page += 1
    sleep(1)
