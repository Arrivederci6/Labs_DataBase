from http import HTTPStatus

from flask import abort

from accuweather.auth.dao import weather_forecast_dao
from accuweather.auth.service.general_service import GeneralService


class WeatherForecastService(GeneralService):
    _dao = weather_forecast_dao

    def get_weather_forecast_dailies_from_weather_forecast(self, id):
        weather_forecast = self._dao.find_by_id(id)
        if weather_forecast is None:
            abort(HTTPStatus.NOT_FOUND)
        return weather_forecast.weather_forecast_dailies

    def get_weather_forecast_hourlies_from_weather_forecast(self, id):
        weather_forecast = self._dao.find_by_id(id)
        if weather_forecast is None:
            abort(HTTPStatus.NOT_FOUND)
        return weather_forecast.weather_forecast_hourlies
