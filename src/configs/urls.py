class ChromeUrl:
    SETTING_PAGE_URL = "chrome://settings/downloads"


class PROTOCOL:
    HTTP = 'http'
    HTTPS = 'https'


class MYSYCM:
    USERNAME = '16744757719'
    PASSWORD = '1234567'
    HOST = 'www.mysycm.com'
    DOMAIN = f'{PROTOCOL.HTTP}://{HOST}'
    LOGIN = f'{DOMAIN}/login.html'
    SSFX = f'{DOMAIN}/dzy/ssfx.html'
