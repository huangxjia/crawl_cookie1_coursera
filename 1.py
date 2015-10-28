__author__ = 'Administrator'

import random
import string
import requests
import urllib2

url = "https://www.coursera.org/api/login/v3"
user_info = {"email": "982789611@qq.com", "password":"huangxj9xyz","webrequest":"true"}
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

def randomString(length):
    return ''.join(random.choice(string.letters + string.digits) for i in xrange(length))

XCSRF2Cookie = 'csrf2_token_%s' % ''.join(randomString(8))
XCSRF2Token = ''.join(randomString(24))
XCSRFToken = ''.join(randomString(24))
cookie = "csrftoken=%s; %s=%s" % (XCSRFToken, XCSRF2Cookie, XCSRF2Token)

post_headers = {"User-Agent": user_agent,
                "Referer": "https://accounts.coursera.org/signin",
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRF2-Cookie": XCSRF2Cookie,
                "X-CSRF2-Token": XCSRF2Token,
                "X-CSRFToken": XCSRFToken,
                "Cookie": cookie}

if __name__ == "__main__":
    coursera_session = requests.Session()
    login = coursera_session.post(url, data=user_info,headers= post_headers)

    if login.status_code == 200:
        print "Login Successfully!"

    content = coursera_session.get('https://www.coursera.org/')
