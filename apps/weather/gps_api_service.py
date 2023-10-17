from functools import lru_cache
from typing import NamedTuple

import requests

from .constants import GEO_URL


class Coordinates(NamedTuple):
    latitude: str
    longitude: str


@lru_cache(maxsize=128)
def get_coordinates(city_name: str) -> Coordinates | None:
    url = GEO_URL.replace('CITY_NAME', city_name)
    response = requests.get(url)
    if response.status_code == 200:
        res = response.json()['response']['GeoObjectCollection']
        if res['metaDataProperty']['GeocoderResponseMetaData']['found'] == '0':
            return None

        geo_object = response.json()['response']['GeoObjectCollection'][
            'featureMember'
        ][0]['GeoObject']
        return Coordinates(
            latitude=geo_object['Point']['pos'].split(' ')[1],
            longitude=geo_object['Point']['pos'].split(' ')[0],
        )
