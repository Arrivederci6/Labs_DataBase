from accuweather.auth.dao import weather_cataclysm_warning_dao
from accuweather.auth.service.general_service import GeneralService


class WeatherCataclysmWarningService(GeneralService):
    _dao = weather_cataclysm_warning_dao