from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import water_temperature_controller
from accuweather.auth.domain.orders.water_temperature import WaterTemperature

water_temperature_bp = Blueprint('water_temperature', __name__, url_prefix='/water_temperature/')

@water_temperature_bp.get('')
def get_all_water_temperature() -> Response:
    return make_response(jsonify(water_temperature_controller.find_all()), HTTPStatus.OK)

@water_temperature_bp.get('/<int:id>')
def get_water_temperature(id: int) -> Response:
    return make_response(jsonify(water_temperature_controller.find_by_id(id)), HTTPStatus.OK)

@water_temperature_bp.post('')
def post_water_temperature() -> Response:
    json = request.get_json()
    water_temperature = WaterTemperature.create_from_dto(json)
    water_temperature_controller.create(water_temperature)
    return make_response(jsonify(water_temperature.put_into_dto()), HTTPStatus.OK)

@water_temperature_bp.put('/<int:id>')
def put_water_temperature(id: int) -> Response:
    json = request.get_json()
    water_temperature = WaterTemperature.create_from_dto(json)
    water_temperature_controller.update(id, water_temperature)
    return make_response("Water temperature updated successfully", HTTPStatus.OK)

@water_temperature_bp.patch('/<int:id>')
def patch_water_temperature(id: int) -> Response:
    json = request.get_json()
    water_temperature_controller.patch(id, json)
    return make_response("Water temperature patched successfully", HTTPStatus.OK)

@water_temperature_bp.delete('/<int:id>')
def delete_water_temperature(id: int) -> Response:
    water_temperature_controller.delete(id)
    return make_response("Water temperature deleted successfully", HTTPStatus.OK)