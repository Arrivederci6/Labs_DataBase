from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import weather_forecast_controller
from accuweather.auth.domain.orders.weather_forecast import WeatherForecast

weather_forecast_bp = Blueprint('weather_forecast', __name__, url_prefix='/weather_forecast/')


@weather_forecast_bp.get('')
def get_all_weather_forecast() -> Response:
    return make_response(jsonify(weather_forecast_controller.find_all()), HTTPStatus.OK)


@weather_forecast_bp.get('/<int:id>')
def get_weather_forecast(id: int) -> Response:
    return make_response(jsonify(weather_forecast_controller.find_by_id(id)), HTTPStatus.OK)


@weather_forecast_bp.post('')
def post_weather_forecast() -> Response:
    json = request.get_json()
    weather_forecast = WeatherForecast.create_from_dto(json)
    weather_forecast_controller.create(weather_forecast)
    return make_response(jsonify(weather_forecast.put_into_dto()), HTTPStatus.OK)


@weather_forecast_bp.put('/<int:id>')
def put_weather_forecast(id: int) -> Response:
    json = request.get_json()
    weather_forecast = WeatherForecast.create_from_dto(json)
    weather_forecast_controller.update(id, weather_forecast)
    return make_response("Weather forecast updated successfully", HTTPStatus.OK)


@weather_forecast_bp.patch('/<int:id>')
def patch_weather_forecast(id: int) -> Response:
    json = request.get_json()
    weather_forecast_controller.patch(id, json)
    return make_response("Weather forecast patched successfully", HTTPStatus.OK)


@weather_forecast_bp.delete('/<int:id>')
def delete_weather_forecast(id: int) -> Response:
    weather_forecast_controller.delete(id)
    return make_response("Weather forecast deleted successfully", HTTPStatus.OK)


@weather_forecast_bp.get('/weather_forecast_dailies/<int:id>')
def get_all_weather_forecast_dailies_from_weather_forecast(id: int):
    return weather_forecast_controller.get_weather_forecast_dailies_from_weather_forecast(id)


@weather_forecast_bp.get('/weather_forecast_hourlies/<int:id>')
def get_all_weather_forecast_hourlies_from_weather_forecast(id: int):
    return weather_forecast_controller.get_weather_forecast_hourlies_from_weather_forecast(id)

