import requests
from datetime import datetime
from datetime import timedelta
import pandas as pd
import re
from secure import token_key, backjoon_level, solved_level

# slack 챗 봇
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text})
    print(response)

# slack 토큰
myToken = token_key 

def pick_problem(platform, level):
    if platform == "backjoon":
        prob_df = pd.read_csv("data/backjoon.csv")
    else:   # samsung
        prob_df = pd.read_csv("data/samsungsw.csv")

    avaiable_prob = prob_df[prob_df['level'] == level]


    result = avaiable_prob.sample(n=1).values.tolist()[0]

    return level, re.sub(r'[^0-9]', '', result[1]), result[2], result[3]


def make_message(year, month, day, platform, level, prob_num, title, url):
    level_dict = {1:"Bronze V",\
                2:"Bronze IV",\
                3:"Bronze III",\
                4:"Bronze II",\
                5:"Bronze I",\
                6:"Silver V",\
                7:"Silver IV",\
                8:"Silver III",\
                9:"Silver II",\
                10:"Silver I",\
                11:"Gold V",\
                12:"Gold IV",\
                13:"Gold III",\
                14:"Gold II",\
                15:"Gold I",\
                16:"Platinum V",\
                17:"Platinum IV",\
                18:"Platinum III",\
                19:"Platinum II",\
                20:"Platinum I",\
                21:"Diamond V",\
                22:"Diamond IV",\
                23:"Diamond III",\
                24:"Diamond II",\
                25:"Diamond I",\
                26:"Ruby V",\
                27:"Ruby IV",\
                28:"Ruby III",\
                29:"Ruby II",\
                30:"Ruby I",\
                     }
    if platform == "backjoon":
        hardness = level_dict[level]
    else:
        hardness = str(level)

    base_line = "❤️ " + year + "." + month + "." + day + "1일 1 문제\n" +\
            "*" + title + "*" +\
            "오늘의 문제 난의도: " + hardness + "\n" + \
            "URL: " + url + "\n" + \
            "문제 풀이가 막히거나 문제를 풀었다면 해당 스레드에\n 링크, 코드, 질문 등을 올려줘!\n" +\
            "+이번 문제에 대해 \"반응\"을 통해서 의견을 남겨줘✅" +\
            '😁 난이도 + 1' +\
            "😑: 현 상황 유지" +\
            "🥵:뜨거워하는_얼굴:: 난이도 - 1"
    base_line = "test"

    return base_line

def dbgout(message):
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + message
    post_message(myToken, "#algorithem", strbuf)

if __name__ == "__main__":
    day = (datetime.now() + timedelta(hours=9)).strftime("%y %m %d") 
    year, month, day = day.split()

    if int(day) % 2 == 0:
        platform = "backjoon"
        level = backjoon_level
    else:
        platform = "samsung"
        level = solved_level
    
    level, prob_num, title, url = pick_problem(platform, level)

    final_message = make_message(year= year, month = month, day = day, platform=platform, level=level, prob_num=prob_num, title=title, url = url)

    post_message("token", "#algorithem", final_message)