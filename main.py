#! /usr/bin/env python
#coding=utf-8
#test git commits

from weibo import APIClient

APP_KEY = '4043432041' # app key
CALLBACK_URL = 'http://apps.weibo.com/meihuayishu' # callback url
APP_SECRET = 'bec86e354c588f8a7bbbc8758f746ba6' # app secret
code = "8a3731c89191adfa4f328686b40c66e9"
def get_url():
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    return client.get_authorize_url()
    
def get_client_info():    
    # 获取URL参数code:

    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    r = client.request_access_token(code)
    access_token = r.access_token # 新浪返回的token，类似abc123xyz456
    expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    # TODO: 在此可保存access token
    print access_token
    print expires_in

    
def get_client():
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET)
    client.set_access_token("2.00gYWiIBp4pd6Ee7d5f05165UEjaFE", "1339487211")
    return client