from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
# from xxx import xxx是Python輸入模組的方式，如果遇到不存在的模組會運用在終端機輸入pip install 模組名稱讓電腦至網路安裝模組。引入模組的規則如下:
# 以下節錄您所複製的官方程式碼，都在讓程式知道您要用的模組及取用方法，譬如: from flask import Flask ，接著後續程式出現 request (不是 requests ，沒有s)時，其實意思是使用了 flask.request 這個模組功能，也是物件導向 ( Object Oriented Programming, OOP)對使用者的意義，在此初學階段我們會用即可。
app = Flask(__name__)
# app = Flask(__name__)將載入的flask模組實例化，即建立了flask伺服器，後續以app這變數操作。
line_bot_api = LineBotApi('006378e4f1a25fa6f6096493df7086c7')
handler = WebhookHandler('006378e4f1a25fa6f6096493df7086c7')


@app.route("/callback", methods=['POST'])
# 接下來牽涉到Python比較進階的物件導向裝飾器decorator用法，你先這樣理解:當@app.route("/callback", methods=['POST'])被觸發時，也就是收到有來自某網址/callback的POST方法時執行以下callback()函數內的程式。而以下這段callback()函數做的是身分認證，另外callback()函數的名稱可以改，命名只是方便呼叫，不影響該函數內容的執行，你也可以改名叫callcallback()。
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#    if event.source.user_id ==''
    line_bot_api.reply_message(
        event.reply_token, #event.reply_token是每則使用者訊息 LINE Sever 都賦予的獨特 token ，僅供觸發一次不能重複使用。
        TextSendMessage(text=event.message.text))
# event.message.text是使用者傳來的文字訊息， TextSendMessage(text=...) 是我們要回傳給使用者的訊息，範例讓此兩者相等，就是echo回去啦!

if __name__ == "__main__": # if __name__ == "__main__" 是 Python 執行程式碼時會進行的內容，此段之前的引入模組、函式 function() 的設計在此主程式執行時才會呼叫使用，
    app.run(debug=True) # app.run() 是flask執行程式的慣用寫法，加入 debug=True 開啟除錯模式，好處是當程式執行期間，您對程式內容的任何修改都會及時讓開啟的服務更新，是為了等等建立webhook的必要程序喔。