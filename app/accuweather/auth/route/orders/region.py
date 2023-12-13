from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import region_controller
from accuweather.auth.domain.orders.region import Region

region_bp = Blueprint('region', __name__, url_prefix='/region/')

@region_bp.get('')
def get_all_region() -> Response:
    return make_response(jsonify(region_controller.find_all()), HTTPStatus.OK)

@region_bp.get('/<int:id>')
def get_region(id: int) -> Response:
    return make_response(jsonify(region_controller.find_by_id(id)), HTTPStatus.OK)

@region_bp.post('')
def post_region() -> Response:
    json = request.get_json()
    region = Region.create_from_dto(json)
    region_controller.create(region)
    return make_response(jsonify(region.put_into_dto()), HTTPStatus.OK)

@region_bp.put('/<int:id>')
def put_region(id: int) -> Response:
    json = request.get_json()
    region = Region.create_from_dto(json)
    region_controller.update(id, region)
    return make_response("Region updated successfully", HTTPStatus.OK)

@region_bp.patch('/<int:id>')
def patch_region(id: int) -> Response:
    json = request.get_json()
    region_controller.patch(id, json)
    return make_response("Region patched successfully", HTTPStatus.OK)

@region_bp.delete('/<int:id>')
def delete_region(id: int) -> Response:
    region_controller.delete(id)
    return make_response("Region deleted successfully", HTTPStatus.OK)

@region_bp.get('/cities/<int:id>')
def get_all_cities_from_region(id: int):
    return region_controller.get_cities_from_region(id)
