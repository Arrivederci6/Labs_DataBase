from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import weather_forecast_hourly_controller
from accuweather.auth.domain.orders.weather_forecast_hourly import WeatherForecastHourly

weather_forecast_hourly_bp = Blueprint('weather_forecast_hourly', __name__, url_prefix='/weather_forecast_hourly/')

@weather_forecast_hourly_bp.get('')
def get_all_weather_forecast_hourly() -> Response:
    return make_response(jsonify(weather_forecast_hourly_controller.find_all()), HTTPStatus.OK)

@weather_forecast_hourly_bp.get('/<int:id>')
def get_weather_forecast_hourly(id: int) -> Response:
    return make_response(jsonify(weather_forecast_hourly_controller.find_by_id(id)), HTTPStatus.OK)

@weather_forecast_hourly_bp.post('')
def post_weather_forecast_hourly() -> Response:
    json = request.get_json()
    weather_forecast_hourly = WeatherForecastHourly.create_from_dto(json)
    weather_forecast_hourly_controller.create(weather_forecast_hourly)
    return make_response(jsonify(weather_forecast_hourly.put_into_dto()), HTTPStatus.OK)

@weather_forecast_hourly_bp.put('/<int:id>')
def put_weather_forecast_hourly(id: int) -> Response:
    json = request.get_json()
    weather_forecast_hourly = WeatherForecastHourly.create_from_dto(json)
    weather_forecast_hourly_controller.update(id, weather_forecast_hourly)
    return make_response("Weather forecast hourly updated successfully", HTTPStatus.OK)

@weather_forecast_hourly_bp.patch('/<int:id>')
def patch_weather_forecast_hourly(id: int) -> Response:
    json = request.get_json()
    weather_forecast_hourly_controller.patch(id, json)
    return make_response("Weather forecast hourly patched successfully", HTTPStatus.OK)

@weather_forecast_hourly_bp.delete('/<int:id>')
def delete_weather_forecast_hourly(id: int) -> Response:
    weather_forecast_hourly_controller.delete(id)
    return make_response("Weather forecast hourly deleted successfully", HTTPStatus.OK)