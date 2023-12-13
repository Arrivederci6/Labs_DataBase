from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.city import City


class CityDao(GeneralDAO):
    _domain_type = City