import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
)

TOKEN = "8801313308:AAG1pDo4iXHj78iNGHuNsCv87hUGH3dpURI"

WEBAPP_URL = "https://rashbaholash.rf.gd/taker.html"

# Premium emoji ID'lari
SALOM_EMOJI = "5891184096192763888"

# /start uchun keyboard
def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Test ishlash",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                    style="danger",
                )
            ]
        ],
        resize_keyboard=True,
    )


dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    text = (
        f'<tg-emoji emoji-id="{SALOM_EMOJI}">⭐</tg-emoji> '
        "Assalomu alaykum!"
    )

    await message.answer(
        text,
        reply_markup=main_keyboard(),
        parse_mode="HTML",
    )


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import os

from aiogram import Bot, Dispatcher
from fastapi import FastAPI
import uvicorn

TOKEN = "8801313308:AAG1pDo4iXHj78iNGHuNsCv87hUGH3dpURI"

bot = Bot(TOKEN)
dp = Dispatcher()

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


async def start_bot():
    await dp.start_polling(bot)


async def main():
    await asyncio.gather(
        start_bot(),
        uvicorn.Server(
            uvicorn.Config(
                app,
                host="0.0.0.0",
                port=int(os.getenv("PORT", 10000)),
            )
        ).serve()
    )


if __name__ == "__main__":
    asyncio.run(main())