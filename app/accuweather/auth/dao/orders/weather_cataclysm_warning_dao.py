from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.weather_cataclysm_warning import WeatherCataclysmWarning


class WeatherCataclysmWarningDao(GeneralDAO):
    _domain_type = WeatherCataclysmWarning