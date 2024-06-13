"""Данный Telegram-бот предназначен для ежедневной отправки сообщения 
со статистикой за вчерашний день Лидов/Продаж/Суммы сделок.
"""

import aioschedule as schedule
import asyncio
import os
import requests
import time

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

Gateway = os.getenv("GATEWAY")
# эндпоинт со списком лидов за вчерашний день:
URL_LEADS = f"http://{Gateway}/api/leads"
# эндпоинт со списком сделок за вчерашний день:
URL_DEALS = f"http://{Gateway}/api/deals"
# параметры, которые передаем в запросе:
headers = {
    "Authorization": os.getenv("AUTHORIZATION_TOKEN"),
}
body = {
    "username": os.getenv("USERNAME"),
    "password": os.getenv("PASSWORD"),
}
# делаем запрос к эндпоинту, в запросе передаем необходимые параметры
try:
    response_leads = requests.get(
        URL_LEADS, params=body, headers=headers
    ).json()
except requests.exceptions.JSONDecodeError:
    response_leads = []
# число лидов за вчерашний день:
leads_count = len(response_leads)
# делаем запрос к эндпоинту, в запросе передаем необходимые параметры
try:
    response_deals = requests.get(
        URL_DEALS, params=body, headers=headers
    ).json()
except requests.exceptions.JSONDecodeError:
    response_deals = []
# число сделок за вчерашний день:
deals_count = len(response_deals)
deals_sum = 0
# подсчитываем сумму сделок за вчерашний день:
for deal in response_deals:
    deals_sum += deal.get("total")
# указываем токен от бота:
bot = Bot(token=os.getenv("TOKEN"))
# id получателя сообщения:
chat_id = os.getenv("CHAT_ID")
# текст сообщения:
text = f"""Статистика за вчерашний день:
Новых лидов - {leads_count}
Сделок - {deals_count}
Сумма сделок (₽) - {deals_sum}"""


# функция отправки сообщения со статистикой:
async def send_message():
    await bot.send_message(chat_id, text)


# делаем отправку сообщения ежедневно в 10:00:
schedule.every().day.at("10:00").do(send_message)
loop = asyncio.get_event_loop()
while True:
    loop.run_until_complete(schedule.run_pending())
    time.sleep(30)
