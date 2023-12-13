from accuweather.auth.dao import air_quality_dao
from accuweather.auth.service.general_service import GeneralService


class AirQualityService(GeneralService):
    _dao = air_quality_dao