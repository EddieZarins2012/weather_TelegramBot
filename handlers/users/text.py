from aiogram import types
from aiogram.dispatcher.filters import Text
import random
import requests
import datetime
from data.config import WEATHER_KEY

from aiogram.types import message

from loader import dp
async def weather_forecast(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_KEY}&q={city}&days=3&aqi=no&alerts=no"
    response = requests.get(url).json()['forecast']['forecastday']
    beginner = f'Here is the {city} forecast for 3 days.'
    days = []
    icons = []
    for i in range(3):
      days.append(f"""Date: {response[i]['date']}
The highest temperature will be {response[i]['day']['maxtemp_c']}°C
The minimal temperature will be {response[i]['day']['mintemp_c']}°C
Condition: {response[i]['day']['condition']['text']}
Sunrise at {response[i]['astro']['sunrise']}
Sunset at {response[i]['astro']['sunset']}""")
      icons.append('https:' + response[i]['day']['condition']['icon'])
    return beginner, days, icons

async def weather_answer(message, city):
    beginner, days, icons = await weather_forecast(city)
    await message.answer(beginner)
    for i in range(3):
        await message.answer_photo(
            photo=icons[i],
            caption=days[i]
        )



@dp.message_handler(Text(equals="Profile"))
async def show_profile(message: types.Message):
    await message.answer('Your profile:\n'
                        f'Name of user: {message.from_user.username}\n'
                        f'Name: {message.from_user.first_name}\n'
                         )
@dp.message_handler(Text(equals="Random Number"))
async def random_number(message: types.message):
    ran = random.randint(0, 5000)
    await message.answer(ran)

@dp.message_handler(Text(equals="London weather"))
async def weather(message: types.message):
    await weather_answer(message, "London")

@dp.message_handler(Text(equals="New York weather"))
async def weather(message: types.message):
    await weather_answer(message, "New York")

@dp.message_handler(Text(equals="Tokyo weather"))
async def weather(message: types.message):
    await weather_answer(message, "Tokyo")


