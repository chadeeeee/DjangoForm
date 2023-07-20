import asyncio
import logging
import sqlite3 as sq
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "5446809526:AAGuUhPdrfHF74uGhCr-fBFoLHmtFApTa34"

router = Router()

base = sq.connect(r'C:\Users\Admin\Desktop\Django\myfirst\data.sqlite3')
cur = base.cursor()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"Привіт, <b>{message.from_user.full_name}<b/>")


async def fetch_last_data_id():
    r = cur.execute("SELECT MAX(id) FROM userdata")
    return r.fetchone()[0]


async def fetch_data_by_id(data_id):
    r = cur.execute("SELECT name, email, message FROM userdata WHERE id = ?", (data_id,))
    return r.fetchone()


async def send_new_data_to_tg(data, chat_id):
    if data:
        bot = Bot(TOKEN, parse_mode="HTML")
        await bot.send_message(chat_id=chat_id, text=f"<b>Ім'я - {data[0]}\nEmail - {data[1]}\nТекст - {data[2]}</b>")


async def check_for_new_data():
    last_data_id = await fetch_last_data_id()

    while True:
        new_data_id = await fetch_last_data_id()

        if new_data_id > last_data_id:
            for data_id in range(last_data_id + 1, new_data_id + 1):
                data = await fetch_data_by_id(data_id)
                await send_new_data_to_tg(data,
                                          5197139803)  # Replace YOUR_CHAT_ID with the chat ID where you want to send the data

            last_data_id = new_data_id

        await asyncio.sleep(1)


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode="HTML")

    asyncio.create_task(check_for_new_data())

    await dp.start_polling(bot)


if __name__ == "__main__":
    print('Bot was started successfully!')
    asyncio.run(main())
