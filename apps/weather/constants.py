from django.conf import settings

GEO_URL = f'https://geocode-maps.yandex.ru/1.x?apikey={settings.GEO_API_KEY}&geocode=CITY_NAME&format=json'
WEATHER_URL = 'https://api.weather.yandex.ru/v2/forecast?lat=LAT&lon=LON&extra=true'

CONDITIONS = {
    'clear': ':sun:',
    'partly-cloudy': ':sun_behind_cloud:',
    'cloudy': ':cloud:',
    'overcast': ':cloud:',
    'light-rain': ':cloud_with_rain:',
    'rain': ':rain:',
    'heavy-rain': ':umbrella_with_rain_drops:',
    'showers': ':umbrella_with_rain_drops:',
    'wet-snow': ':cloud_with_snow:',
    'light-snow': ':cloud_with_snow:',
    'snow': ':cloud_with_snow:',
    'snow-showers': ':cloud_with_snow:',
    'hail': ':tornado:',
    'thunderstorm': ':tornado:',
    'thunderstorm-with-rain': ':tornado:',
    'thunderstorm-with-hail': ':tornado:',
}
