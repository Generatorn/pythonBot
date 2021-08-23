from main import bot, dp
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
@dp.message_handler(commands=['help'])
async def process_start_command(message: Message):
#    await message.answer("Привет!", reply_markup=kb.greet_kb)
    message.reply("Привет!", reply_markup=kb.greet_kb)
    print("hello")
