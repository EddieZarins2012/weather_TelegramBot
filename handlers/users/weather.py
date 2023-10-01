from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default.new_keyboard import new_menu
from loader import dp


@dp.message_handler(Command("weather"))
async def weather_cnd(message: types.Message):
    await message.answer("Choose a city", reply_markup=new_menu)