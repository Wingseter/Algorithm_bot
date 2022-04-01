# solved.ac
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time

result = pd.DataFrame()
# 1: level1, 8: level8
print("Crawling Solved.ac Start")
print("==============================================")
for level in range(1, 9):
    print("Level" + str(level))
    print("==============================================")
    page = 0
    while True:
        page += 1
        print("page" + str(page))
        print("==============================================")
        URL = f"https://swexpertacademy.com/main/code/problem/problemList.do?problemLevel={level}&pageIndex={page}"

        response = requests.get(URL)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        prob_nums = []
        for nums in soup.select('div.widget-list > div.widget-box-sub > div > div > span.week_num'):
            prob_nums.append(nums.contents)
        prob_titles = []
        for title in soup.select('div.widget-list > div.widget-box-sub > div > div > span.week_text > a'):
            real_title = str(title.contents[0].string)
            real_title = real_title.strip('\r\n\t\xa0')
            prob_titles.append(real_title)
        prob_urls = []
        for url in soup.select('div.widget-list > div.widget-box-sub > div > div > span.week_text > a'):
            prob_urls.append("https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=" + url['onclick'][25: -3])

        if len(prob_nums) != len(prob_titles) and len(prob_titles) != len(prob_urls):
            print("I Think It have something Problems")
            break

        if len(prob_nums) != 0 and len(title) != 0:
            for i in range(len(prob_nums)):
                df1 = pd.DataFrame({'level':[level],\
                    'prob_num':[prob_nums[i]],\
                    'prob_titles':[prob_titles[i]],\
                    'prob_urls':[prob_urls[i]]
                    })
                result = pd.concat([result, df1])
                result.index = np.arange(len(result))
        else:
            break

result.to_csv('data/samsungsw.csv', index=False, encoding='utf-8-sig')

        
        # if i % 60 == 0:
        #     print("Sleep 90seconds. Count:" + str(i)\
        #         +", Local Time:"\
        #         + time.strftime('%Y-%m-%d', time.localtime(time.time())\
        #         + " " + time.strftime('%X', time.localtime(time.time()))\
        #         + ", Data Length:" + str(len(result))))
        #     time.sleep(90)