from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

new_menu = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, keyboard=[
    [KeyboardButton(text="London weather")],
    [KeyboardButton(text="New York weather")],
    [KeyboardButton(text="Tokyo weather")]

])
