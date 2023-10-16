from logging import getLogger

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from django.conf import settings

from apps.weather.gps_api_service import get_coordinates
from apps.weather.weather_api_service import get_weather

from . import static_text as txt

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)
logger = getLogger('bot')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    logger.info(f'Start command: {message.from_user.username}')
    kb = [[types.KeyboardButton(text='Узнать погоду')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(
        txt.START_MSG.format(name=message.from_user.username),
        parse_mode='html',
        reply_markup=keyboard,
    )


@dp.message_handler(text='Узнать погоду')
async def get_weather_command(message: types.Message):
    await message.answer('Напиши название города')


@dp.message_handler(
    lambda message: message.text and not message.text.startswith('Погода в ')
)
async def message(message: types.Message):
    answer = txt.CITY_NOT_FOUND
    logger.info(f'Message: {message.text}')
    coordinates = get_coordinates(message.text.lower())
    logger.info(f'Coordinates: {coordinates}')
    if coordinates:
        weather = get_weather(coordinates)
        logger.info(f'Weather: {weather}')
        if weather:
            answer = txt.WEATHER_MSG.format(
                city=message.text,
                temperature=weather.temperature,
                pressure=weather.pressure,
                wind_speed=weather.wind_speed,
            )
    await message.answer(answer, parse_mode='html')


def main():
    executor.start_polling(dp, skip_updates=True)
