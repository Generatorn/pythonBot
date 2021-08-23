from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
button_hi = KeyboardButton('Привет!')
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)
