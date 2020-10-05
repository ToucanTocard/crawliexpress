# Crawliexpress

- [Crawliexpress](#crawliexpress)
  - [TODO](#todo)
  - [Description](#description)
  - [Usage](#usage)
    - [Install](#install)
    - [Item](#item)
    - [Feedbacks](#feedbacks)
    - [Search / Category](#search--category)
  - [API](#api)

## TODO

* finir docstrings

## Description

Allows to fetch various resources from Aliexpress, such as category, text search, product, feedbacks.

It does not use official API nor a headless browser, but parses page source.

Obviously, it is very vulnerable to DOM changes.

## Usage

### Install

```bash
pip install crawliexpress
```

### Item

```python
from crawliexpress import Client

client = Client("https://fr.aliexpress.com")
client.get_item("4000505787173")
```

### Feedbacks

```python
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
```

### Search / Category

```python
from crawliexpress import Client

from time import sleep

client = Client(
    "https://fr.aliexpress.com",
    xman_t="k++kIGjVqO0lCuOTMhKQUevJCW3sdIn4iNmwfMA7Pj/OqiTgTOYZUJ73JKhAufD1QMqkx8WKpiBq82niJM+AAPFH5pDadbfbs6bo6blWmTKXGATIXt6U19wbWEXrsyXkWREZmTQA0hE6fR6VsvMksQGjgbMHw1OuTKykAN7V+1SGr2lSDxZrWHTVjiQr5KHW+B3J5tfdUL/kD3x0Cks99EIJk3DASJUHTm5JXFbWZk6mAENwoMKA7UcNIa2qJ9L9svSVh913O4YHrv8fE7g1MR2OCMucyISEDhE4oocRZOr20AiPnA7K0saIrCL1YlTsdYrfrT3NvQsosnRJ5kcK6wCNCN2Mb1+RNe7YYEvW9owYF4zr/+Wlgf3bdAsknBq/X2JP8mOnjmMRaHXMk0NI2HrMejliPvsSRUixBHuzLoQgNjpZlzf6PdHD4qfSZAmGTpemKlvm3sU02GbahHPYLe4EU050PJOfdcki/EFV2lp3tZpMP5OkKRzZykcZ2zuicjnPUQM/FFkztEAQEjiWHYcL0vA9/4DTd47mz8tXL2wq0s8HdJ3mWPpyazZAKSb8EDauOLgifNs5cl8VPDV8SIPBfW7mAYw7Fi2zMzAgUdO28+o2zTYszr8rjzNhtOgqybvMH8bao5xTXIzjbcLbQ600vPzdYO0",
    x5sec="b2261652d676c6f7365617263682d7765623b32223a226164326232393838396239363337363335333865353262623839616339633365434f43787a507346454c364b682f4b626973755264526f4d4d546b334d4451304e5467324d547378227d",
    aep_usuc_f="site=fra&c_tp=EUR&x_alimid=1970445861&isb=y&ups_u_t=1635073090737&region=FR&b_locale=fr_FR&ae_u_p_s=0",
)

page_no = 1
while True:

    # category
    page = client.get_search(page_no, category_id=205000314)

    # text search
    # page = client.get_search(page_no, search_text="allo le monde")
    if page.has_next_page() is False:
        break
    page_no += 1
    sleep(1)
```

- **xman_t**, **x5sec**, **aep_usuc_f**: must be taken from your browser cookies, to avoid captcha and empty result pages

## API

### class crawliexpress.Client(base_url, xman_t=None, x5sec=None, aep_usuc_f=None)
Exposes methods to fetch various resources.


* **Parameters**


    * **base_url** – allows to change locale (not sure about this one)


    * **xman_t** – must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls


    * **x5sec** – must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls


    * **aep_usuc_f** – must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls



#### get_feedbacks(product_id, owner_member_id, company_id=None, v=2, member_type='seller', page=1, with_picture=False)
Fetches a product feedback page


* **Parameters**


    * **product_id** – id of the product, item id of [https://fr.aliexpress.com/item/20000001708485.html](https://fr.aliexpress.com/item/20000001708485.html) is 20000001708485


    * **owner_member_id** – member id of the product owner, as stored in **Crawliexpress.Item.owner_member_id**


    * **page** – page number


    * **with_picture** – limit to feedbacks with a picture



* **Returns**

    a feedback page



* **Return type**

    Crawliexpress.FeedbackPage



* **Raises**

    **CrawliexpressException** – if there was an error fetching the dataz



#### get_item(item_id)
Fetches a product informations from its id


* **Parameters**

    **item_id** – id of the product to fetch, item id of [https://fr.aliexpress.com/item/20000001708485.html](https://fr.aliexpress.com/item/20000001708485.html) is 20000001708485



* **Returns**

    a product



* **Return type**

    Crawliexpress.Item



* **Raises**

    **CrawliexpressException** – if there was an error fetching the dataz



#### get_search(page_no=1, category_id=0, search_text=None, sort_by='default')
Fetches a search page


* **Parameters**


    * **page_no** – page number


    * **category_id** – id of the category, category id of [https://fr.aliexpress.com/category/205000221/t-shirts.html](https://fr.aliexpress.com/category/205000221/t-shirts.html) is 205000221


    * **search_text** – text search


    * **sort_by** (**default**: best match
    **total_tranpro_desc**: number of orders) – indeed



* **Returns**

    a search page



* **Return type**

    Crawliexpress.SearchPage



* **Raises**


    * **CrawliexpressException** – if there was an error fetching the dataz


    * **CrawliexpressCaptchaException** – if there is a captcha, make sure to use valid **xman_t, x5sec, aep_usuc_f** cookie values to avoid this



### exception crawliexpress.CrawliexpressCaptchaException()

### exception crawliexpress.CrawliexpressException()

### class crawliexpress.Feedback()
A user feedback


#### comment( = None)
Review


#### country( = None)
Country code


#### datetime( = None)
Raw datetime from DOM


#### images( = None)
List of image links


#### profile( = None)
Profile link


#### rating( = None)
Rating out of 100


#### user( = None)
Name


### class crawliexpress.FeedbackPage()
A feedback page


#### feedbacks( = None)
List of **Crawliexpress.Feedback** objects


#### has_next_page()
Returns true if there is a following page, useful for crawling


* **Rtype bool**



#### known_pages( = None)
Sibling pages


#### page( = None)
Page number


### class crawliexpress.SearchPage()
A search page


#### has_next_page()
Returns true if there is a following page, useful for crawling


* **Rtype bool**



#### items( = None)
List of products, raw from JS parsing


#### page( = None)
page number


#### result_count( = None)
Number of result for the whole search


#### size_per_page( = None)
Number of result per page
