# crawl_cookie1_coursera

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
                "Cookie": cookie
                }
