from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import region_service


class RegionController(GeneralController):
    _service = region_service

    def get_cities_from_region(self, id):
        return [city.put_into_dto() for city in self._service.get_cities_from_region(id)]
