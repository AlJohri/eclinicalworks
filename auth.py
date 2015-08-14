import os, hashlib, requests

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2467.2 Safari/537.36'

BASE_URL = "https://mycw72.ecwcloud.com/portal9438/jsp/100mp/"
hex_md5 = lambda x: hashlib.md5(x.encode('utf-8')).hexdigest()

response = s.get(BASE_URL + "login.jsp")

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

login_payload = {
    "nact": 1,
    "password": hex_md5(hex_md5(password) + s.cookies['JSESSIONID']),
    "redirect": "",
    "loginid": email,
    "txtPlainPassword": "",
    "pwdStore": "123411111111"
}

response = s.post(BASE_URL + "login.jsp", data=login_payload)
