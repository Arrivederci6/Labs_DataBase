from accuweather.auth.dao.general_dao import GeneralDAO
from accuweather.auth.domain.orders.weather_forecast_hourly import WeatherForecastHourly


class WeatherForecastHourlyDao(GeneralDAO):
    _domain_type = WeatherForecastHourly