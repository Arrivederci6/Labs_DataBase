from accuweather.auth.service.orders.air_quality_service import AirQualityService
from accuweather.auth.service.orders.city_service import CityService
from accuweather.auth.service.orders.country_service import CountryService
from accuweather.auth.service.orders.region_service import RegionService
from accuweather.auth.service.orders.water_temperature_service import WaterTemperatureService
from accuweather.auth.service.orders.weather_cataclysm_warning_service import WeatherCataclysmWarningService
from accuweather.auth.service.orders.weather_forecast_daily_service import WeatherForecastDailyService
from accuweather.auth.service.orders.weather_forecast_hourly_service import WeatherForecastHourlyService
from accuweather.auth.service.orders.weather_forecast_service import WeatherForecastService
from accuweather.auth.service.orders.weather_service import WeatherService

air_quality_service = AirQualityService()
city_service = CityService()
country_service = CountryService()
region_service = RegionService()
water_temperature_service = WaterTemperatureService()
weather_cataclysm_warning_service = WeatherCataclysmWarningService()
weather_forecast_daily_service = WeatherForecastDailyService()
weather_forecast_hourly_service = WeatherForecastHourlyService()
weather_forecast_service = WeatherForecastService()
weather_service = WeatherService()