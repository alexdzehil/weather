from typing import NamedTuple

import requests
from cachetools import TTLCache

from django.conf import settings

from .constants import WEATHER_URL
from .gps_api_service import Coordinates

cache = TTLCache(maxsize=128, ttl=1800)


class Weather(NamedTuple):
    temperature: int
    pressure: int
    wind_speed: int
    condition: str


def get_weather(coordinates: Coordinates) -> Weather | None:
    if coordinates in cache:
        return cache[coordinates]

    url = WEATHER_URL.replace('LAT', str(coordinates.latitude)).replace(
        'LON', str(coordinates.longitude)
    )
    headers = {'X-Yandex-API-Key': settings.WEATHER_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        weather_data = response.json()
        weather = Weather(
            temperature=weather_data['fact']['temp'],
            pressure=weather_data['fact']['pressure_mm'],
            wind_speed=weather_data['fact']['wind_speed'],
            condition=weather_data['fact']['condition'],
        )
        cache[coordinates] = weather
        return weather
    return None
