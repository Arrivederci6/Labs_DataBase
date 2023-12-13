from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import air_quality_controller
from accuweather.auth.domain.orders.air_quality import AirQuality

air_quality_bp = Blueprint('air_quality', __name__, url_prefix='/air_quality/')


@air_quality_bp.get('')
def get_all_air_quality() -> Response:
    return make_response(jsonify(air_quality_controller.find_all()), HTTPStatus.OK)

@air_quality_bp.get('/<int:id>')
def get_air_quality(id: int) -> Response:
    return make_response(jsonify(air_quality_controller.find_by_id(id)), HTTPStatus.OK)

@air_quality_bp.post('')
def post_air_quality() -> Response:
    json = request.get_json()
    air_quality = AirQuality.create_from_dto(json)
    air_quality_controller.create(air_quality)
    return make_response(jsonify(air_quality.put_into_dto()), HTTPStatus.OK)

@air_quality_bp.put('/<int:id>')
def put_air_quality(id: int) -> Response:
    json = request.get_json()
    air_quality = AirQuality.create_from_dto(json)
    air_quality_controller.update(id, air_quality)
    return make_response("Air Quality updated successfully", HTTPStatus.OK)

@air_quality_bp.patch('/<int:id>')
def patch_air_quality(id: int) -> Response:
    json = request.get_json()
    air_quality_controller.patch(id, json)
    return make_response("Air Quality patched successfully", HTTPStatus.OK)

@air_quality_bp.delete('/<int:id>')
def delete_air_quality(id: int) -> Response:
    air_quality_controller.delete(id)
    return make_response("Air Quality deleted successfully", HTTPStatus.OK)