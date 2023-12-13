from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.weather import Weather


class WeatherDao(GeneralDAO):
    _domain_type = Weather