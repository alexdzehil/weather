from django.conf import settings

GEO_URL = f'https://geocode-maps.yandex.ru/1.x?apikey={settings.GEO_API_KEY}&geocode=CITY_NAME&format=json'
WEATHER_URL = 'https://api.weather.yandex.ru/v2/forecast?lat=LAT&lon=LON&extra=true'
