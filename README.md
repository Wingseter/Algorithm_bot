# Algorithm_bot
JobKill &amp; Javis Algorithm Bot

# 프로젝트 설명
---
 Slack 알고리즘 채널에서 사용할 매일마다 문제를 하나씩 추천해주는 Slack Bot 입니다.
 
 # How to Use
 ---
 이 프로그램은 WayScript 사이트에서 사용될수 있도록 만들어 졌습니다.
 https://wayscript.com/
 

1. data 폴더 생성
2. Run crawling_samsumg_sw.py -> csv 파일 생성됨
3. Run crawling_solved.py -> csv 파일 생성됨

이후 wayScript 워크 스페이스를 생성한 후에 
새로운 lair 생성합니다.

4. 생성된 lair에 data 폴더 생성 후 upload file을 선택해 csv 파일을 업로드합니다.
5. requirement.txt 파일과 slackbot.py 파일을 업로드 합니다.
6. slack auth token은 .secrets 파일에 입력해 주고 워크 스페이스를 재시작 합니다. (key 이름은 default: algKey 이후 필요할시 slackbot.py 수정 필요)

7. secure.py 파일을 생성하고 
backjoon_level = 원하는 래밸 1-30
solved_level = 원하는 래밸 1-8 을 지정합니다.

8. .trigger 파일로 이용해 cron 트리거를 만들어 줍니다. 실행할 명령어는 

  pip install -r requirements.txt && python slackbot.py  
  
crontab 예시: 30 14 * * *
= 매일 11시 30분에 실행

 9. deploy 해줍니다.
