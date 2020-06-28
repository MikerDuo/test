#!/usr/bin/python
# coding:utf-8

import hashlib
import hmac
import base64
import time
import json
import random
from urllib import request

post_domain = 'http://online.dgweb-icslbox.huawei.com'
post_url = '/api/tenants/25/rest/channels/19/messages'
client_id = 'ea85abb0-8244-4c4a-9d53-cb8a733140b6'
client_secret = '34e639798cd2b41a0b06193d533e978a7a97f65f1dd37100ae0595b5294f42b37580c554'
json_body = {
  "bodies": [
    {
      "msg": "testmsg2",
      "type": "txt"
    }
  ],
  "ext": {
    "queue_id": "",
    "queue_name": "",
    "agent_username": "",
    "visitor": {
      "user_nickname": "userNickname1sunkai",
      "true_name": "userTrueName-sunkai",
      "qq": "9999999919",
      "email": "sunkai@test1.test",
      "phone": "188888881888",
      "company_name": "comp1anyName",
      "description": "descr1iption"
    }
  },
  "msg_id": "143324231421234234",
  "origin_type": "rest",
  "from": "test_weichat_visi1tor051",
  "timestamp": 1468832767680
}

while True:
    msg = input('Input:')
    now_time = int(round(time.time() * 1000))
    json_body['timestamp'] = now_time
    json_body['msg_id'] = str(random.randint(1,6000000))
    json_body['bodies'][0]['msg'] = msg

    body = json.dumps(json_body)
    md_body = hashlib.sha256(bytes(body, 'utf-8')).hexdigest()
    timestamp = str(now_time + 60000)
    signature = base64.b64encode(hmac.new(bytes(client_secret, 'utf-8'), bytes('POST\n' + post_url + '\n' + timestamp + '\n' + md_body, 'utf-8'), digestmod=hashlib.sha256).digest())
    headers = {'Content-Type': 'application/json; utf-8', 'X-Auth-Expires' : timestamp, 'Authorization' : 'hmac ' + client_id + ':' + str(signature, encoding = "utf8")}
    req = request.Request(post_domain + post_url, bytes(body, 'utf-8'), headers)
    with request.urlopen(req) as response:
        print(str(response.read(), encoding = "utf8"))