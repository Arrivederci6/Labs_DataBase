from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import city_service


class CityController(GeneralController):
    _service = city_service

    def get_water_temperatures_from_city(self, id):
        return [water_temperature.put_into_dto() for water_temperature in self._service.get_water_temperatures_from_city(id)]

    def get_air_qualities_from_city(self, id):
        return [air_quality.put_into_dto() for air_quality in self._service.get_air_qualities_from_city(id)]

    def get_weather_cataclysm_warnings_from_city(self, id):
        return [weather_cataclysm_warning.put_into_dto() for weather_cataclysm_warning in self._service.get_weather_cataclysm_warnings_from_city(id)]

    def get_weather_forecasts_from_city(self, id):
        return [weather_forecast.put_into_dto() for weather_forecast in self._service.get_weather_forecasts_from_city(id)]