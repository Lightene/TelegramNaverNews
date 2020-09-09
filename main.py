import telegram
import news_crawler
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError

import time

TELEGRAM_TOKEN = ''

bot = telegram.Bot(token=TELEGRAM_TOKEN)
updates = bot.getUpdates()
chat_id = updates[-1].message.chat_id


def news_message():
    dt = datetime.now()
    today = dt.strftime("%Y-%m-%d")
    str = today + " 네이버 뉴스\n"+news_crawler.naver_news()
    bot.sendMessage(chat_id=chat_id, text=str)


def select_message():
    bot.sendMessage(chat_id='{지인 id 코드}', text="한번 쯤은 편지 보내주실 때가 됬습니다. 뉴스 스크랩해서 보내주세요~") #chat_id 지인 코드


for update in updates:
    print(update.message)


sched = BackgroundScheduler()
sched.add_job(news_message, 'cron', hour='9', minute='30') # 매일 9시 반 메세지
sched.add_job(select_message, 'cron', day_of_week='2', hour='20', minute='30') # 매주 수요일 밤 8시 반 메세지
sched.start()


while True:
    time.sleep(1)