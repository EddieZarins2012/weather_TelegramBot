from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Here is some useful information")