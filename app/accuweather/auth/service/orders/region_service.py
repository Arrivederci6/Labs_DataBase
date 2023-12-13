from http import HTTPStatus

from flask import abort

from accuweather.auth.dao import region_dao
from accuweather.auth.service.general_service import GeneralService


class RegionService(GeneralService):
    _dao = region_dao

    def get_cities_from_region(self, id):
        region = self._dao.find_by_id(id)
        if region is None:
            abort(HTTPStatus.NOT_FOUND)
        return region.cities
