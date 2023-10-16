from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from django.conf import settings

from . import static_text as txt

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(
        txt.START_MESSAGE.format(name=message.from_user.username), parse_mode='html'
    )


@dp.message_handler(commands=['get_weather'])
async def get_weather_command(message: types.Message):
    await message.reply(
        txt.START_MESSAGE.format(name=message.from_user.username), parse_mode='html'
    )


def main():
    executor.start_polling(dp, skip_updates=True)
