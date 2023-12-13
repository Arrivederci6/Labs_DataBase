from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import weather_forecast_service


class WeatherForecastController(GeneralController):
    _service = weather_forecast_service

    def get_weather_forecast_dailies_from_weather_forecast(self, id):
        return [weather_forecast_daily.put_into_dto() for weather_forecast_daily in self._service.get_weather_forecast_dailies_from_weather_forecast(id)]

    def get_weather_forecast_hourlies_from_weather_forecast(self, id):
        return [weather_forecast_hourly.put_into_dto() for weather_forecast_hourly in self._service.get_weather_forecast_hourlies_from_weather_forecast(id)]