# Python 程式入門設計
# 網路爬蟲 Web Crawler - Cookie
# 基本流程
# 1.連線到特定網址，抓取資料
# 2.解析資料，取得實際想要的部分
# 關鍵心法
# 盡可能地，讓程式模仿一個普通使用者的樣子
# Cookie
# 什麼是 Cookie?
# 網站存放在瀏覽器的一小段內容
# 與伺服器的互動
# 連線時，放在Request Headers 中送出
# 追蹤連結
# HTML 超連結
# <html>
#     <head>
#         <title>HTML 格式</title>
#     </head>
#     <body>
#         <a href="https://www.google.com/">Google</a>  # a 超連結的意思
#     </body>
# </html>            
# 連續抓取頁面實務
# 解析頁面的超連結，並結合程式邏輯完成
# 抓取 PTT 八卦版的網頁原始碼 (HTML)
# 開發人員> Applc
import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index.html"
# 建立一個 Request 物件, 附加 Request Headers 的資訊
request=req.Request(url,headers={
    "cookis":"over18=1"
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"    
}) # User-Agent 使用者代理 (設定-開發人員選項 上方 Network)
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)    
#解析原始碼, 取得每篇文章的標題
import bs4  # bs4 套件名稱
root=bs4.BeautifulSoup(data,"html.parser")  # parser 解析器
print(root.title.string)  # title 標題 string 文字
# titles=root.find("div", class_="title")  # 尋找 class="title"的div標籤
# print(titles.a.string)
titles=root.find_all("div",class_="title")  # find_all 尋找所有
for title in titles:
    if title.a !=None:  # 如果標題包含 a 標籤(每有被刪除). 印出來
        print(title.a.string)
# F12開發人員 > Application > Cookies
