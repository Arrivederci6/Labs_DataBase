from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import weather_controller
from accuweather.auth.domain.orders.weather import Weather

weather_bp = Blueprint('weather', __name__, url_prefix='/weather/')

@weather_bp.get('')
def get_all_weather() -> Response:
    return make_response(jsonify(weather_controller.find_all()), HTTPStatus.OK)

@weather_bp.get('/<int:id>')
def get_weather(id: int) -> Response:
    return make_response(jsonify(weather_controller.find_by_id(id)), HTTPStatus.OK)

@weather_bp.post('')
def post_weather() -> Response:
    json = request.get_json()
    weather = Weather.create_from_dto(json)
    weather_controller.create(weather)
    return make_response(jsonify(weather.put_into_dto()), HTTPStatus.OK)

@weather_bp.put('/<int:id>')
def put_weather(id: int) -> Response:
    json = request.get_json()
    weather = Weather.create_from_dto(json)
    weather_controller.update(id, weather)
    return make_response("Weather updated successfully", HTTPStatus.OK)

@weather_bp.patch('/<int:id>')
def patch_weather(id: int) -> Response:
    json = request.get_json()
    weather_controller.patch(id, json)
    return make_response("Weather patched successfully", HTTPStatus.OK)

@weather_bp.delete('/<int:id>')
def delete_weather(id: int) -> Response:
    weather_controller.delete(id)
    return make_response("Weather deleted successfully", HTTPStatus.OK)

@weather_bp.get('/weather_forecasts/<int:id>')
def get_all_weather_forecasts_from_weather(id:int):
    return weather_controller.get_weather_forecasts_from_weather(id)