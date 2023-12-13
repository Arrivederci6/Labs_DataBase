from http import HTTPStatus

from flask import abort

from accuweather.auth.dao import weather_dao
from accuweather.auth.service.general_service import GeneralService


class WeatherService(GeneralService):
    _dao = weather_dao

    def get_weather_forecasts_from_weather(self, id):
        weather = self._dao.find_by_id(id)
        if weather is None:
            abort(HTTPStatus.NOT_FOUND)
        return weather.weather_forecasts
