from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import city_controller
from accuweather.auth.domain.orders.city import City

city_bp = Blueprint('city', __name__, url_prefix='/city/')

@city_bp.get('')
def get_all_city() -> Response:
    return make_response(jsonify(city_controller.find_all()), HTTPStatus.OK)

@city_bp.get('/<int:id>')
def get_city(id: int) -> Response:
    return make_response(jsonify(city_controller.find_by_id(id)), HTTPStatus.OK)

@city_bp.post('')
def post_city() -> Response:
    json = request.get_json()
    city = City.create_from_dto(json)
    city_controller.create(city)
    return make_response(jsonify(city.put_into_dto()), HTTPStatus.OK)

@city_bp.put('/<int:id>')
def put_city(id: int) -> Response:
    json = request.get_json()
    city = City.create_from_dto(json)
    city_controller.update(id, city)
    return make_response("City updated successfully", HTTPStatus.OK)

@city_bp.patch('/<int:id>')
def patch_city(id: int) -> Response:
    json = request.get_json()
    city_controller.patch(id, json)
    return make_response("City patched successfully", HTTPStatus.OK)

@city_bp.delete('/<int:id>')
def delete_city(id: int) -> Response:
    city_controller.delete(id)
    return make_response("City deleted successfully", HTTPStatus.OK)

@city_bp.get('/water_temperatures/<int:id>')
def get_all_water_temperatures_from_city(id: int):
    return city_controller.get_water_temperatures_from_city(id)

@city_bp.get('/air_qualities/<int:id>')
def get_all_air_qualities_from_city(id: int):
    return city_controller.get_air_qualities_from_city(id)

@city_bp.get('/weather_cataclysm_warnings/<int:id>')
def get_all_weather_cataclysm_warnings_from_city(id: int):
    return city_controller.get_weather_cataclysm_warnings_from_city(id)

@city_bp.get('/weather_forecasts/<int:id>')
def get_all_weather_forecasts_from_city(id: int):
    return city_controller.get_weather_forecasts_from_city(id)