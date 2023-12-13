from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.region import Region


class RegionDao(GeneralDAO):
    _domain_type = Region