from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.weather_forecast import WeatherForecast


class WeatherForecastDao(GeneralDAO):
    _domain_type = WeatherForecast