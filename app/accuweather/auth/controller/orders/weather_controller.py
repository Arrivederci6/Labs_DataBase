from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import weather_service


class WeatherController(GeneralController):
    _service = weather_service

    def get_weather_forecasts_from_weather(self, id):
        return [weather_forecast.put_into_dto() for weather_forecast in self._service.get_weather_forecasts_from_weather(id)]