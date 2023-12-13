from http import HTTPStatus

from flask import abort

from accuweather.auth.dao import country_dao
from accuweather.auth.service.general_service import GeneralService


class CountryService(GeneralService):
    _dao = country_dao

    def get_regions_from_country(self, id):
        country = self._dao.find_by_id(id)
        if country is None:
            abort(HTTPStatus.NOT_FOUND)
        return country.regions
