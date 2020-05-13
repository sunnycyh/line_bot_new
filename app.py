from flask import Flask, request, abort # build up server

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('SIn7txCvdfFRZp2aN9FwnqGLusdRkPotxhECFkEM3yAKd7d2Yadx7UABYp+VGar1kX3ql+sxoHmukWjSOS/bKkA4STf1de9rA5LB5dRbzkWTtEnyJdhh3Gwy51mMY0HZmydkCtXx2PrUKuXpRp2gwgdB04t89/1O/w1cDnyilFU=')
# YOUR_CHANNEL_ACCESS_TOKEN
handler = WebhookHandler('dea511ddf968cd950ffe10070c3fd5a9')
# YOUR_CHANNEL_SECRET


@app.route("/callback", methods=['POST'])
# route means path of website: eg.www.line-bot.com/callback, the webhook url to callback everything from the user
# line-bot receive the msg and transfer to our server
def callback(): #
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    # trigger the next function: def handle_message(event):
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '唔識應你啊臭豬'
    if msg in ['hi', 'Hi', 'HI']: # check the word is in the sentense or not
        r = 'hi臭豬'
    elif msg == '得唔得閒':
        r = '有咩屁話直接講'
    elif msg == '你係邊個':
        r = '知道我係邊個重要咩？你知唔知你自己係邊個？'
    elif '？' in msg:
        r = '我唔直接答你，有咩問題去搵整我出黎個條契弟'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r)) # event.message.text means the msg sent by the user


if __name__ == "__main__": # to ensure the app.run()(main function) is only executed by the direct action instead of import
    app.run()
