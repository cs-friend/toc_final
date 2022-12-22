from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

channel_secret = "27b6044fca2f0f59f46001283189e291"
channel_access_token = "0YptVYTNVQbhpRCezn9hCys1U1nLiQyW6WWAI79h0fUhnUPnFigeXKuSkCDGfwMqYEGkz0X3wz8lqtS3Hbcg2eGpm1GnUyjBHpgcMTCe0tcpDxk34PL9EMk8/5tKi/0QRej7A1Jv5JsjbNEwA1YlgAdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # try:
    #     handler.handle(body, signature)
    # except InvalidSignatureError:
    #     abort(400)
    print(body)

    return 'OK'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)