from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import air_quality_service


class AirQualityController(GeneralController):
    _service = air_quality_service