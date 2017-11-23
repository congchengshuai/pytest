import pytest
from conftest import session

def test_JJD(session):
    url = "https://fjfinance.gxq168.com/depository/query/queryChangeList?app_source=2&bizTypes=&c_androidId=EDC54BA7-97FD-4EE8-B628-E964D981C7FE&c_channelId=iOS&c_identify=EDC54BA7-97FD-4EE8-B628-E964D981C7FE&c_imei=&c_ip=192.168.10.83&c_macAddress=&c_model=iPhone&c_networkType=WiFi&c_phone=&c_systemVersion=10.0.1&c_userInfo=1607055354&cid=&length=20&nonce=1511438678&offset=0&platform=1&serialId=EDC54BA7-97FD-4EE8-B628-E964D981C7FE1511438678.815320&sid=a15825c2dca99512a6d78107f991593c2e26aa37&sign=01f67ff18cb92996aa5ea8a982bd2379&ssid=a15825c2dca99512a6d78107f991593c2e26aa37&uid=1607055354&version=1.2.5"
    res = session.get(url)
    assert res.status_code