from flask import Flask, request, abort
import requests
import json
from bs4 import BeautifulSoup

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import tempfile, os
import datetime
import time

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

#important !!!!!
line_bot_api = LineBotApi('your_channel_access_token')
handler = WebhookHandler('your_channel_secret')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '板塊' ==  msg:
        response = requests.get("https://dncapi.bqrank.net/api/concept/web-conceptlist?page=1&webp=1")
        plats = json.loads(response.text)
        information= ""
        for index,item in enumerate(plats['data']):
            index +=1
            information += item['name']+","+"\nBest: "+item['best']+", "+" Precent: "+str(item['best_percent'])+"%"+'\n'
            if index == 10:
                break
        message = TextSendMessage(text=information)
        line_bot_api.reply_message(event.reply_token, message)
    elif '貪婪指標' ==  msg:
        response = requests.get("https://api.alternative.me/fng/?limit=2")
        fear_index = json.loads(response.text)
        now = "Fear/Greed Index--> "+fear_index['data'][0]['value_classification']+'\nValue -->'+fear_index['data'][0]['value']
        yes = "Fear/Greed Index--> "+fear_index['data'][1]['value_classification']+'\nValue --> '+fear_index['data'][1]['value']
        message2 = "今天: \n"+now+"\n"+"昨天: \n"+yes+"\n"
        message = TextSendMessage(text=message2)
        line_bot_api.reply_message(event.reply_token, message)
    elif '漲跌分佈' == msg:
        response3 = requests.get("https://dncapi.bqrank.net/api/home/global?webp=1")
        total_coins_count = json.loads(response3.text)
        risenum = total_coins_count['data']['risenum']
        fallnum = total_coins_count['data']['fallnum']
        summary = "24H漲跌分佈： \n"+"上漲: "+str(risenum)+"種\n"+"下跌: "+str(fallnum)+"種\n"
        message = TextSendMessage(text=summary)
        line_bot_api.reply_message(event.reply_token, message)
    elif '市佔率' ==  msg:
        response4 = requests.get("https://dncapi.bqrank.net/api/coin/coin_accounting?webp=1")
        dom = json.loads(response4.text)
        list = ""
        for index, coin in enumerate(dom['data']):
            index += 1
            list+= str(index)+". "+coin['symbol']+" 市佔: "+str(coin["percentage"])+"%\n"
            if index == 10:
                break
        message = TextSendMessage(text=list)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'help' == msg or '幫助'== msg:
        msga = "查詢\n 1. 板塊\n 2. 貪婪指標\n 3. 漲跌分佈 \n 4. 市佔率"
        message = TextSendMessage(text=msga)
        line_bot_api.reply_message(event.reply_token, message)
    elif '嗨' == msg or 'hi'==msg:
        msg = "不要再跟我說嗨了～快打 help"
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
