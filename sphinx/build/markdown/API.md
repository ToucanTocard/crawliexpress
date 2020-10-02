# API


### class crawliexpress.Client(base_url, xman_t=None, x5sec=None, aep_usuc_f=None)
Exposes methods to fetch various resources.


* **Parameters**

    
    * **base_url** – allows to change locale (not sure about this one)


    * **xman_t** – must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls


    * **x5sec** – must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls


    * **aep_usuc_f** – must be taken from your browser cookies, to avoid captcha and empty result pages on get_search() calls



#### get_item(item_id)
Fetches a product informations from its id


#### get_search(page_no, category_id=0, search_text=None, sort_by='default')
sort_by can be:
- default: best
- orders: total_tranpro_desc


### exception crawliexpress.CrawliexpressCaptchaException()

### exception crawliexpress.CrawliexpressException()
