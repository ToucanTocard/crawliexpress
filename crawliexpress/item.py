from crawliexpress.exception import CrawliexpressException

import re
import json


class Item:
    product_id = None
    owner_member_id = None
    company_id = None

    def from_html(self, html):
        matches = re.search(
            r"window\.runParams = ({.+?};)$", html, re.MULTILINE | re.DOTALL
        )

        if matches is None:
            raise CrawliexpressException("could not parse item from html")

        run_params = matches.group(1)
        # run_params = json.loads(matches.group(1))
        print(run_params)
