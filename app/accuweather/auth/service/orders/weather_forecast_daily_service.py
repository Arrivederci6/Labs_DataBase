from accuweather.auth.dao import weather_forecast_daily_dao
from accuweather.auth.service.general_service import GeneralService


class WeatherForecastDailyService(GeneralService):
    _dao = weather_forecast_daily_dao