from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import weather_forecast_hourly_service


class WeatherForecastHourlyController(GeneralController):
    _service = weather_forecast_hourly_service