from logging import getLogger

from ninja import NinjaAPI

from apps.weather.gps_api_service import get_coordinates
from apps.weather.weather_api_service import get_weather

api = NinjaAPI()
logger = getLogger('debug')


@api.get('/weather/')
def get_weather_by_city_name(request, city: str):
    logger.info(f'Get weather by city name: {city}')
    if city:
        coordinates = get_coordinates(city.lower())
        logger.info(f'Coordinates: {coordinates}')
        if coordinates:
            weather = get_weather(coordinates)
            logger.info(f'Weather: {weather}')
            if weather:
                data = {
                    'temperature': weather.temperature,
                    'pressure': weather.pressure,
                    'wind_speed': weather.wind_speed,
                }
                return data
        return {'error': 'something went wrong'}
