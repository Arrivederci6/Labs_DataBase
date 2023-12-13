from accuweather.auth.dao import water_temperature_dao
from accuweather.auth.service.general_service import GeneralService


class WaterTemperatureService(GeneralService):
    _dao = water_temperature_dao