from crawliexpress import Client

from time import sleep

client = Client(
    "https://fr.aliexpress.com",
    "ali_apache_id=11.10.63.129.1586181829601.188727.3; xman_us_f=x_lid=uk371767861kjwae&x_l=0&x_locale=fr_FR&no_popup_today=n&x_c_chg=0&x_user=UK|Robin|Kleinermanns|ifm|1970445861&acs_rt=685ea3b02d9545168344bc19d3615958&last_popup_time=1599496152399&x_as_i=%7B%22cookieCacheEffectTime%22%3A1601980214495%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D; aep_usuc_f=site=fra&c_tp=EUR&x_alimid=1970445861&isb=y&ups_u_t=1635073090737&region=FR&b_locale=fr_FR&ae_u_p_s=0; intl_common_forever=UNMZnVxobMAoQG2onDHfbyiXtnJyza5W06GWPE6ySITNW9ITqlYDCQ==; xman_f=IE0BZ/k9Q9CRv8NFsantvn8dlV2NwgpAo62kWC3+lu2iwMszBjIUUk/XMoFz8LfahdOOk9j2OHK0Mr2qv8LC+cgk6IgoJavebARFEqMzZUfKBDkcHD8b8aRK9DMABlFWumazZfgCHYYwxw2r5YkDHeNFvkCh5yfR093M8iGe3/yr7uPFpNKz4FWBAIUIsEUuq7R2qBHqpP2/RXXnoq2DpI5F0CRXbi1e6B/gmoivTehQLrSiencQNN2AD4Ccz6gA090RkIcSYRlPRZcP4Xd8wYSFP7/gMlQTj4pNebDmjshLj/H9aIpz6NIZtREZSMpPqXZV4dN7oW510F+9NghVG9ly2aeINBTM8At/t2s1oRlwHTR7Z69RcKaGWVlLolmMyGQstCsiJhk35vzqawxjFH9/6v6bv3y6/q+KrClQNtcXpblk47Z0zg==; isg=BDQ0YlVA1xsMDEIgSEI-w5JeBvumDVj3R33PYs6VwL9COdSD9h0oh-r7uenh2pBP; l=eBNCro_RQm7O-QcBBOfahurza77OSIOYYuPzaNbMiOCP_ICp5TChBZzK7iL9C36Nh6yHR3Svv4UwBeYBYIcTIM3CwI20F8Mmn; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%094000760753072%094000761580287%0920000001708485%094000505787173%0920000001708485%094001231996341; ali_apache_track=mt=1|mid=uk371767861kjwae; tfstk=cxCABPqUOvYbaFaWxtek5t_ioJzlZ_r9Vqti6yU1GcumQahdi_5h9vMbhFTJKzC..; e_id=pt80; aep_common_f=qwDZQ05s2OeJEfll38R8uLmYaTTJhCAI/xeBtvyK7QsQluKxTsWYxA==; _m_h5_tk=cfe9e16c0386a49fd52b8c0f2125b1ac_1601982257346; _m_h5_tk_enc=8f43d1f299525fd24f6bed31cd33475b; acs_usuc_t=x_csrf=yf39mezi717y&acs_rt=f242f5fa5d004484b821269fa7042712; intl_locale=fr_FR; AKA_A2=A; xman_t=oRkon0f0E3DowKuWqPai4L/dC9aQhLjVt/xhWPPs4ea2LYLRcbci3b3Slq/ju/Bq; JSESSIONID=009BB86A8AD984908D26D5A567EAC94E; _bl_uid=m3kkef8jxUttCXhX3byLi52sO44d; xlly_s=1; ali_apache_tracktmp=",
)

page = 1
while True:
    search_page = client.get_category(205000314, "t-shirts", page=page)
    # page = client.get_search(page, search_text="allo le monde")
    print(search_page.page)
    if search_page.has_next_page() is False:
        break
    page += 1
    sleep(1)
