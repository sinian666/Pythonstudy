import hashlib
import hmac
import json
import random

import requests

ak = "f3e7f342755aacd03c40922ad662799c"
sk = "0a404cd490e28d130289a14c6e1e4cbf"
# 模拟的did个数
device_count = 26

rawbody = {
    "app_pkg": "com.lcx",
    "os_ver": 28,
    "brand": "HUAWEI",
    "model": "SEA-AL10",
    "did": "2qlaj6ty1ckoe3vb",
    "local_sdks": [
        {
            "pkg": "adfwe.efwq.few",
            "ver": 0,
            "api_ver": 1
        }
    ]
}


def auth(body):
    header1 = "X-Mars-Date"
    date = "20210906T213338Z"
    headers = {header1: date, "Content-Type": "application/json"}
    body_str = json.dumps(body)

    k_sign = hmac.new(bytes(sk, encoding="utf8"), bytes(date, encoding="utf8"), digestmod=hashlib.sha256).hexdigest()
    v_sign = header1.lower() + ":" + date + "\n" + hashlib.md5(bytes(body_str, encoding="utf8")).hexdigest()
    signature = hmac.new(bytes(k_sign, encoding="utf8"), bytes(v_sign, encoding="utf8"),
                         digestmod=hashlib.sha256).hexdigest()
    authorization = "HMAC-SHA256 Credential=" + ak + ",SignedHeaders=" + header1.lower() + ";,Signature=" + signature
    headers["Authorization"] = authorization
    return headers, body_str


def main():
    # 重复的did

    for i in range(0, device_count):
        print("第%d次生成did: ", i)
        rawbody["did"] = "".join(random.sample("1234567890qwertyuioplkjhgfdsazxcvbnm", 16))
        print("did = %s", rawbody["did"])

    # 重复did
    redid = ["2qlaj6ty1ckoe3vb", "75z2urtsx0joylh6", "nmci68w2qgp19u37", "5q8d9vzi6c3wtxfk", "tach8op5q0mdzr6s",
            "qfzsex9cija7pvw3", "vwne4mc87lpgko1r"]
    for did in redid:
        rawbody["did"] = did

    # #多sdk
    # sdks = ["com.wzl4", "com.wzl3""com.wzl2", "com.wzl1", "com.wzl","adfwe.efwq.few"]
    # for sdk in sdks:
    #     rawbody["local_sdks"][0]["pkg"] = sdk
        for j in range(0, 10):
            headers, body = auth(rawbody)
            resp = requests.post('http://mira-boe.bytedance.net/zeus/client/query', headers=headers, data=body)
            m = json.loads(resp.text)
            print(resp.text)


if __name__ == '__main__':
    main()