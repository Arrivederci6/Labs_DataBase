from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.air_quality import AirQuality


class AirQualityDao(GeneralDAO):
    _domain_type = AirQuality