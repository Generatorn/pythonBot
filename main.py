import asyncio
import telegramconfig
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

logging.basicConfig(filename="bot.log", level=logging.INFO)

loop = asyncio.get_event_loop()

bot = Bot(token=telegramconfig.bot_token, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)


if __name__ == "__main__":
    from hendlers import dp, send_to_admin
    executor.start_polling(dp, skip_updates=True, on_startup=send_to_admin)