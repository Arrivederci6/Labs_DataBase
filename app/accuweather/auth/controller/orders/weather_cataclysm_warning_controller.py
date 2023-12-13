from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import weather_cataclysm_warning_service


class WeatherCataclysmWarningController(GeneralController):
    _service = weather_cataclysm_warning_service