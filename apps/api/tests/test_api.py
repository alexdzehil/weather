from unittest.mock import patch

from django.test import Client

from apps.weather.gps_api_service import Coordinates
from apps.weather.weather_api_service import Weather


def test_bad_city_name_get_weather_by_city_name():
    client = Client()

    response = client.get('/api/weather/?city=йцу')

    assert response.status_code == 200
    assert response.json() == {'error': 'something went wrong'}


def test_get_weather_by_city_name():
    client = Client()

    with (
        patch('apps.weather.gps_api_service.get_coordinates') as mock_get_coordinates,
        patch('apps.weather.weather_api_service.get_weather') as mock_get_weather,
    ):
        mock_get_coordinates.return_value = Coordinates(
            latitude=53.902284, longitude=27.561831
        )
        mock_get_weather.return_value = Weather(
            temperature=25, pressure=1010, wind_speed=5
        )

        response = client.get('/api/weather/?city=Минск')
        assert response.status_code == 200

        data = response.json()
        assert 'temperature' in data
        assert 'pressure' in data
        assert 'wind_speed' in data


def test_no_city_name_get_weather_by_city_name():
    client = Client()

    response = client.get('/api/weather/')

    assert response.status_code == 422
