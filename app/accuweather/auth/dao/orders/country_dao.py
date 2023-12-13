from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.country import Country


class CountryDao(GeneralDAO):
    _domain_type = Country