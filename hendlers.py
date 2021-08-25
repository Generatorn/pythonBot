from main import bot, dp, types
import keyboards as kb
from aiogram.types import Message
from config import admin_id


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


#@dp.message_handler()
#async def echo(message: Message):
#    text = f"Привет, ты написал: {message.text}"
#    await message.answer(text=text)


# Обработчик кнопки
@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.answer("Привет!", reply_markup=kb.greet_kb)
    #message.reply("Привет!", reply_markup=kb.greet_kb)
#    print("hello")


#@dp.message_handler(commands="start")
#async def cmd_start(message: Message):
#    keyboard = types.ReplyKeyboardMarkup()
#    button_1 = types.KeyboardButton(text="С пюрешкой")
#    keyboard.add(button_1)
#    button_2 = "Без пюрешки"
#    keyboard.add(button_2)
#    await message.answer("Как подавать котлеты?", reply_markup=keyboard)
