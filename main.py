import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    WebAppInfo,
)
from fastapi import FastAPI
import uvicorn


# =========================
# SOZLAMALAR
# =========================

TOKEN = "8801313308:AAGessGbwgmBdHHQFrEBuauE0_gJGHE1q6o"

WEBAPP_URL = "https://rashbaholash.rf.gd/taker.html"

# Premium emoji ID'lari
SALOM_EMOJI = "5891184096192763888"


# =========================
# BOT
# =========================

dp = Dispatcher()


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


# =========================
# FASTAPI
# =========================

app = FastAPI()


@app.get("/")
async def home():
    return {"status": "ok", "bot": "running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


# =========================
# BOT POLLING
# =========================

async def start_bot():
    bot = Bot(token=TOKEN)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


# =========================
# MAIN
# =========================

async def main():
    logging.basicConfig(level=logging.INFO)

    port = int(os.environ.get("PORT", 10000))

    server = uvicorn.Server(
        uvicorn.Config(
            app,
            host="0.0.0.0",
            port=port,
            log_level="info",
        )
    )

    await asyncio.gather(
        start_bot(),
        server.serve(),
    )


if __name__ == "__main__":
    asyncio.run(main())