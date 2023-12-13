from accuweather.auth.controller.general_controller import GeneralController
from accuweather.auth.service import country_service


class CountryController(GeneralController):
    _service = country_service

    def get_regions_from_country(self, id):
        return [region.put_into_dto() for region in self._service.get_regions_from_country(id)]
