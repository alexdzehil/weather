import unittest
from unittest.mock import Mock, patch

from apps.weather.gps_api_service import Coordinates, get_coordinates


class TestGetCoordinates(unittest.TestCase):
    @patch('apps.weather.gps_api_service.get_coordinates')
    def test_get_coordinates_success(self, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'response': {
                'GeoObjectCollection': {
                    'metaDataProperty': {'GeocoderResponseMetaData': {'found': '1'}},
                    'featureMember': [
                        {'GeoObject': {'Point': {'pos': '27.561831 53.902284'}}}
                    ],
                }
            }
        }
        mock_requests_get.return_value = mock_response

        result = get_coordinates('Минск')

        expected_coordinates = Coordinates(latitude='53.902284', longitude='27.561831')
        self.assertEqual(result, expected_coordinates)

    @patch('apps.weather.gps_api_service.requests.get')
    def test_get_coordinates_not_found(self, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'response': {
                'GeoObjectCollection': {
                    'metaDataProperty': {'GeocoderResponseMetaData': {'found': '0'}}
                }
            }
        }
        mock_requests_get.return_value = mock_response

        result = get_coordinates('SomeNonExistentCity')

        self.assertIsNone(result)
