from http import HTTPStatus

from flask import abort

from accuweather.auth.dao import city_dao
from accuweather.auth.service.general_service import GeneralService


class CityService(GeneralService):
    _dao = city_dao

    def get_water_temperatures_from_city(self, id):
        city = self._dao.find_by_id(id)
        if city is None:
            abort(HTTPStatus.NOT_FOUND)
        return city.water_temperatures

    def get_air_qualities_from_city(self, id):
        city = self._dao.find_by_id(id)
        if city is None:
            abort(HTTPStatus.NOT_FOUND)
        return city.air_qualities

    def get_weather_cataclysm_warnings_from_city(self, id):
        city = self._dao.find_by_id(id)
        if city is None:
            abort(HTTPStatus.NOT_FOUND)
        return city.weather_cataclysm_warnings

    def get_weather_forecasts_from_city(self, id):
        city = self._dao.find_by_id(id)
        if city is None:
            abort(HTTPStatus.NOT_FOUND)
        return city.weather_forecasts

