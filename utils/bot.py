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
        self.wx_key = cfg.BOT_DEFAULT_KEY
        self.msg = MsgDTO()

    def send_channel(self, *args):
        title = args[0]
        body = args[1]

        content = title + body

        headers = {'Content-Type': 'application/json'}
        data = {
            "msgtype": "text",
            "text": {
                "content": content,
                # "mentioned_list": ["huangyi@so366.com", "@all"],
                # "mentioned_mobile_list": user_list
            }
        }
        url = self.api + self.wx_key

        requests.post(url=url, headers=headers, data=json.dumps(data))

    def data(self):
        call_time = time.strftime('%H:%M:%S')
        # 告警模板
        title = '{0} {1}'
        body = '{0},项目:{1},当前取值:{2}'

        get_data = request.json
        if 'evalMatches' not in get_data:
            return False

        eval_matches = get_data['evalMatches'][0]
        self.msg.state = get_data['state']
        self.msg.rule_name = get_data['ruleName']
        self.msg.msg = get_data['message']
        self.msg.metric = eval_matches['metric']
        self.msg.judge_get_value = round(eval_matches['value'], 1)

        if self.msg.state == 'alerting':
            title = title.format(call_time, '告警')
            body = body.format(self.msg.msg, self.msg.metric, self.msg.judge_get_value)

        if self.msg.state == 'ok':
            pass

        self.send_channel(title, body)
