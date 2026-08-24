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

TOKEN = "8801313308:AAEhgLI2MfSIoLfiMFNLaajQdTKm5Yy9UI0"

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
