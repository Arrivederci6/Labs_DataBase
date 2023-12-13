from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.water_temperature import WaterTemperature


class WaterTemperatureDao(GeneralDAO):
    _domain_type = WaterTemperature