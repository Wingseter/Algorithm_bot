import requests
from datetime import datetime

from secure import token_key

# slack 챗 봇
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text})
    print(response)

# slack 토큰
myToken = token_key 


# message로 받은 인자를 파이썬 쉘과 슬랙 #채널이름 에 동시에 출력한다
def dbgout(message):
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + message
    post_message(myToken, "#algorithem", strbuf)

dbgout("확인해 보자")