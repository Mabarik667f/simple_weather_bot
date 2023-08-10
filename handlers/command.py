from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from math import ceil
from config_reader import config
import datetime
import requests

router = Router()


@router.message(Command('start'))
async def cmd_start(msg: Message):
    await msg.reply('Привет, Напиши название города и получи прогноз погоды')


@router.message()
async def get_weather(msg: Message):
    appid = config.appid.get_secret_value()
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': msg.text, 'units': 'metric', 'APPID': appid, 'lang': 'ru'})

    try:
        data = res.json()
        data = data['list'][0]
        temp = data["main"]['feels_like']
        pressure = data["main"]['pressure']
        humidity = data["main"]['humidity']
        wind = ceil(data['wind']['speed'])
        weather = data['weather'][0]['description']

        w = f"---{datetime.datetime.now().strftime('%Y.%m.%d %H:%M')}---\n" \
            f"Погода в городе {msg.text.title()}:\n" \
            f"Температура: {temp}° {weather.title()}\n" \
            f"Атмосферное давление: {pressure} мм. рт. ст.\n"\
            f"Влажность: {humidity} %\n" \
            f"Ветер: {wind} м/с\n" \


        await msg.reply(w)

    except Exception as ex:
        await msg.reply('Такого города нет')
