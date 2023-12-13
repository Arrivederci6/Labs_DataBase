from accuweather.auth.dao.orders.air_quality_dao import AirQualityDao
from accuweather.auth.dao.orders.city_dao import CityDao
from accuweather.auth.dao.orders.country_dao import CountryDao
from accuweather.auth.dao.orders.region_dao import RegionDao
from accuweather.auth.dao.orders.water_temperature_dao import WaterTemperatureDao
from accuweather.auth.dao.orders.weather_cataclysm_warning_dao import WeatherCataclysmWarningDao
from accuweather.auth.dao.orders.weather_dao import WeatherDao
from accuweather.auth.dao.orders.weather_forecast_daily_dao import WeatherForecastDailyDao
from accuweather.auth.dao.orders.weather_forecast_dao import WeatherForecastDao
from accuweather.auth.dao.orders.weather_forecast_hourly_dao import WeatherForecastHourlyDao

air_quality_dao = AirQualityDao()
city_dao = CityDao()
country_dao = CountryDao()
region_dao = RegionDao()
water_temperature_dao = WaterTemperatureDao()
weather_cataclysm_warning_dao = WeatherCataclysmWarningDao()
weather_dao = WeatherDao()
weather_forecast_daily_dao = WeatherForecastDailyDao()
weather_forecast_dao = WeatherForecastDao()
weather_forecast_hourly_dao = WeatherForecastHourlyDao()