from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import water_temperature_service


class WaterTemperatureController(GeneralController):
    _service = water_temperature_service