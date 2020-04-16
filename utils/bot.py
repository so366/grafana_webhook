# _*_coding:utf-8_*_
from flask import request
import time
import requests
import json
from utils.msg_dto import MsgDTO
import config as cfg


class Bot:
    """
       企业微信接口
    """
    def __init__(self):

        self.api = cfg.BOT_API
        self.msg = MsgDTO()

    def send_channel(self, *args):
        title = args[0]
        body = args[1]
        wx_key = args[2]
        user_list = args[3]

        content = title + body

        headers = {'Content-Type': 'application/json'}
        data = {
            "msgtype": "text",
            "text": {
                "content": content,
                # "mentioned_list": ["huangyi@so366.com", "@all"],
                "mentioned_mobile_list": user_list
            }
        }
        url = self.api + wx_key

        requests.post(url=url, headers=headers, data=json.dumps(data))

    def put_data(self):
        call_time = time.strftime('%H:%M:%S')
        get_data = request.json
        print(get_data)

        # title = call_time + ' ' + get_data['title']
        # body = get_data['body']
        # if 'wx_key' in get_data and 'phone_list' in get_data:
        #     wx_key = get_data['wx_key']
        # else:
        #     wx_key = '8cdf1c7d-93b7-41d5-aaf8-7ebcdfd2ae69'
        #
        # self.send_channel(title, body, wx_key)

