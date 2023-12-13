from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import weather_cataclysm_warning_controller
from accuweather.auth.domain.orders.weather_cataclysm_warning import WeatherCataclysmWarning

weather_cataclysm_warning_bp = Blueprint('weather_cataclysm_warning', __name__, url_prefix='/weather_cataclysm_warning/')

@weather_cataclysm_warning_bp.get('')
def get_all_weather_cataclysm_warning() -> Response:
    return make_response(jsonify(weather_cataclysm_warning_controller.find_all()), HTTPStatus.OK)

@weather_cataclysm_warning_bp.get('/<int:id>')
def get_weather_cataclysm_warning(id: int) -> Response:
    return make_response(jsonify(weather_cataclysm_warning_controller.find_by_id(id)), HTTPStatus.OK)

@weather_cataclysm_warning_bp.post('')
def post_weather_cataclysm_warning() -> Response:
    json = request.get_json()
    weather_cataclysm_warning = WeatherCataclysmWarning.create_from_dto(json)
    weather_cataclysm_warning_controller.create(weather_cataclysm_warning)
    return make_response(jsonify(weather_cataclysm_warning.put_into_dto()), HTTPStatus.OK)

@weather_cataclysm_warning_bp.put('/<int:id>')
def put_weather_cataclysm_warning(id: int) -> Response:
    json = request.get_json()
    weather_cataclysm_warning = WeatherCataclysmWarning.create_from_dto(json)
    weather_cataclysm_warning_controller.update(id, weather_cataclysm_warning)
    return make_response("Weather cataclysm warning updated successfully", HTTPStatus.OK)

@weather_cataclysm_warning_bp.patch('/<int:id>')
def patch_weather_cataclysm_warning(id: int) -> Response:
    json = request.get_json()
    weather_cataclysm_warning_controller.patch(id, json)
    return make_response("Weather cataclysm warning patched successfully", HTTPStatus.OK)

@weather_cataclysm_warning_bp.delete('/<int:id>')
def delete_weather_cataclysm_warning(id: int) -> Response:
    weather_cataclysm_warning_controller.delete(id)
    return make_response("Weather cataclysm warning deleted successfully", HTTPStatus.OK)