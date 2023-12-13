from accuweather.auth.dao import weather_forecast_hourly_dao
from accuweather.auth.service.general_service import GeneralService


class WeatherForecastHourlyService(GeneralService):
    _dao = weather_forecast_hourly_dao