import pytest
import requests

@pytest.fixture(scope="module")
def session():
    url = "https://fjfinance.gxq168.com/depository/user/queryUserInformation"
    data = {"app_source":2,"c_androidId":"EDC54BA7-97FD-4EE8-B628-E964D981C7FE","c_channelId": "iOS",
            "c_identify": "EDC54BA7-97FD-4EE8-B628-E964D981C7FE", "c_ip": "192.168.10.83", "c_model":"iPhone",
            "c_networkType":"WiFi", "c_systemVersion":"10.0.1", "c_userInfo":"1607055354", "nonce":"1511435775",
            "serialId":"EDC54BA7-97FD-4EE8-B628-E964D981C7FE1511435775.349628","sid":"a15825c2dca99512a6d78107f991593c2e26aa37",
            "sign":"8aa36648b9cec79a32e5a30c1a94e063","ssid":"a15825c2dca99512a6d78107f991593c2e26aa37","uid":"1607055354","version":"1.2.5"}
    session = requests.session()
    headers =  {"Content-Type": "application/x-www-form-urlencoded"}
    session.post(url,data = data, headers = headers)
    yield session