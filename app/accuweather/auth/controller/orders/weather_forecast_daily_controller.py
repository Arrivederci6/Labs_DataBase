from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import weather_forecast_daily_service


class WeatherForecastDailyController(GeneralController):
    _service = weather_forecast_daily_service