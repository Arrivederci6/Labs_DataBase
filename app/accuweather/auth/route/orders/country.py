from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from accuweather.auth.controller import country_controller
from accuweather.auth.domain.orders.country import Country

country_bp = Blueprint('country', __name__, url_prefix='/country/')

@country_bp.get('')
def get_all_country() -> Response:
    return make_response(jsonify(country_controller.find_all()), HTTPStatus.OK)

@country_bp.get('/<int:id>')
def get_country(id: int) -> Response:
    return make_response(jsonify(country_controller.find_by_id(id)), HTTPStatus.OK)

@country_bp.post('')
def post_country() -> Response:
    json = request.get_json()
    country = Country.create_from_dto(json)
    country_controller.create(country)
    return make_response(jsonify(country.put_into_dto()), HTTPStatus.OK)

@country_bp.put('/<int:id>')
def put_country(id: int) -> Response:
    json = request.get_json()
    country = Country.create_from_dto(json)
    country_controller.update(id, country)
    return make_response("Country updated successfully", HTTPStatus.OK)

@country_bp.patch('/<int:id>')
def patch_country(id: int) -> Response:
    json = request.get_json()
    country_controller.patch(id, json)
    return make_response("Country patched successfully", HTTPStatus.OK)

@country_bp.delete('/<int:id>')
def delete_country(id: int) -> Response:
    country_controller.delete(id)
    return make_response("Country deleted successfully", HTTPStatus.OK)

@country_bp.get('/regions/<int:id>')
def get_all_regions_from_country(id: int):
    return country_controller.get_regions_from_country(id)