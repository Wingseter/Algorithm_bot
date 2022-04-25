# solved.ac
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

result = pd.DataFrame()
# 1: Bronze5, 30: Ruby1
print("Crawling Solved.ac Start")
print("==============================================")
for level in range(1, 31):
    print("Level" + str(level))
    print("==============================================")
    page = 0
    while True:
        page += 1
        print("page" + str(page))
        print("==============================================")

        URL = f"https://solved.ac/problems/level/{level}?page={page}"

        response = requests.get(URL)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        prob_nums = []
        for nums in soup.select('a.ProblemInline__ProblemStyle-sc-yu6g1r-0.jRAQI > span'):
            prob_nums.append(nums.contents)
        prob_titles = []
        for title in soup.select('div.ProblemTitleLink__ProblemTitle-sc-2ljb1q-1.gBCZWH > a > span'):
            prob_titles.append(title.contents)
        prob_urls = []
        for url in soup.select('div.ProblemTitleLink__ProblemTitle-sc-2ljb1q-1.gBCZWH > a'):
            prob_urls.append(url['href'])

        if len(prob_nums) != len(prob_titles) and len(prob_titles) != len(prob_urls):
            print("I Think It have something Problems")

        if len(prob_nums) != 0:
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

result.to_csv('data/backjoon.csv', index=False, encoding='utf-8-sig')

        
        # if i % 60 == 0:
        #     print("Sleep 90seconds. Count:" + str(i)\
        #         +", Local Time:"\
        #         + time.strftime('%Y-%m-%d', time.localtime(time.time())\
        #         + " " + time.strftime('%X', time.localtime(time.time()))\
        #         + ", Data Length:" + str(len(result))))
        #     time.sleep(90)