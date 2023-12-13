from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import weather_forecast_daily_controller
from accuweather.auth.domain.orders.weather_forecast_daily import WeatherForecastDaily

weather_forecast_daily_bp = Blueprint('weather_forecast_daily', __name__, url_prefix='/weather_forecast_daily/')

@weather_forecast_daily_bp.get('')
def get_all_weather_forecast_daily() -> Response:
    return make_response(jsonify(weather_forecast_daily_controller.find_all()), HTTPStatus.OK)

@weather_forecast_daily_bp.get('/<int:id>')
def get_weather_forecast_daily(id: int) -> Response:
    return make_response(jsonify(weather_forecast_daily_controller.find_by_id(id)), HTTPStatus.OK)

@weather_forecast_daily_bp.post('')
def post_weather_forecast_daily() -> Response:
    json = request.get_json()
    weather_forecast_daily = WeatherForecastDaily.create_from_dto(json)
    weather_forecast_daily_controller.create(weather_forecast_daily)
    return make_response(jsonify(weather_forecast_daily.put_into_dto()), HTTPStatus.OK)

@weather_forecast_daily_bp.put('/<int:id>')
def put_weather_forecast_daily(id: int) -> Response:
    json = request.get_json()
    weather_forecast_daily = WeatherForecastDaily.create_from_dto(json)
    weather_forecast_daily_controller.update(id, weather_forecast_daily)
    return make_response("Weather forecast daily updated successfully", HTTPStatus.OK)

@weather_forecast_daily_bp.patch('/<int:id>')
def patch_weather_forecast_daily(id: int) -> Response:
    json = request.get_json()
    weather_forecast_daily_controller.patch(id, json)
    return make_response("Weather forecast daily patched successfully", HTTPStatus.OK)

@weather_forecast_daily_bp.delete('/<int:id>')
def delete_weather_forecast(id: int) -> Response:
    weather_forecast_daily_controller.delete(id)
    return make_response("Weather forecast daily deleted successfully", HTTPStatus.OK)