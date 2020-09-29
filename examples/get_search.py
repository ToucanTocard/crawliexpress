from crawliexpress import Client

from time import sleep

client = Client(
    "https://fr.aliexpress.com",
    xman_t="1k++kIGjVqO0lCuOTMhKQUevJCW3sdIn4iNmwfMA7Pj/OqiTgTOYZUJ73JKhAufD1QMqkx8WKpiBq82niJM+AAPFH5pDadbfbs6bo6blWmTKXGATIXt6U19wbWEXrsyXkWREZmTQA0hE6fR6VsvMksQGjgbMHw1OuTKykAN7V+1SGr2lSDxZrWHTVjiQr5KHW+B3J5tfdUL/kD3x0Cks99EIJk3DASJUHTm5JXFbWZk6mAENwoMKA7UcNIa2qJ9L9svSVh913O4YHrv8fE7g1MR2OCMucyISEDhE4oocRZOr20AiPnA7K0saIrCL1YlTsdYrfrT3NvQsosnRJ5kcK6wCNCN2Mb1+RNe7YYEvW9owYF4zr/+Wlgf3bdAsknBq/X2JP8mOnjmMRaHXMk0NI2HrMejliPvsSRUixBHuzLoQgNjpZlzf6PdHD4qfSZAmGTpemKlvm3sU02GbahHPYLe4EU050PJOfdcki/EFV2lp3tZpMP5OkKRzZykcZ2zuicjnPUQM/FFkztEAQEjiWHYcL0vA9/4DTd47mz8tXL2wq0s8HdJ3mWPpyazZAKSb8EDauOLgifNs5cl8VPDV8SIPBfW7mAYw7Fi2zMzAgUdO28+o2zTYszr8rjzNhtOgqybvMH8bao5xTXIzjbcLbQ600vPzdYO0",
    x5sec="7b2261652d676c6f7365617263682d7765623b32223a226164326232393838396239363337363335333865353262623839616339633365434f43787a507346454c364b682f4b626973755264526f4d4d546b334d4451304e5467324d547378227d",
    aep_usuc_f="site=fra&c_tp=EUR&x_alimid=1970445861&isb=y&ups_u_t=1635073090737&region=FR&b_locale=fr_FR&ae_u_p_s=0",
)

page_no = 1
while True:
    page = client.get_search(page_no, category_id=205000314)
    # page = client.get_search(page_no, search_text="allo le monde")
    print(page.page)
    if page.has_next_page() is False:
        break
    page_no += 1
    sleep(1)
