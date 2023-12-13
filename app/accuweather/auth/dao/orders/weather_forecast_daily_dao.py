from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.weather_forecast_daily import WeatherForecastDaily


class WeatherForecastDailyDao(GeneralDAO):
    _domain_type = WeatherForecastDaily