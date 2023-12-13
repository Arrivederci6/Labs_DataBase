from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class WeatherForecast(db.Model, IDto):
    __tablename__ = "weather_forecast"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    weather_id = db.Column(db.Integer, db.ForeignKey('weather.id'))
    temperature = db.Column(db.DECIMAL(2, 0), nullable=False)
    wind_speed = db.Column(db.DECIMAL(2, 0), nullable=False)
    humidity = db.Column(db.DECIMAL(3, 0), nullable=False)
    precipitation_probability = db.Column(db.DECIMAL(3, 0), nullable=False)

    city = relationship('City', back_populates='weather_forecasts')
    weather = relationship('Weather', back_populates='weather_forecasts')
    weather_forecast_dailies = relationship('WeatherForecastDaily', back_populates='weather_forecast')
    weather_forecast_hourlies = relationship('WeatherForecastHourly', back_populates='weather_forecast')

    def __repr__(self):
        return f"WeatherForecast({self.city_id}, {self.weather_id}, {self.temperature}, {self.wind_speed}, {self.humidity}, {self.precipitation_probability})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'WeatherForecast':
        obj = WeatherForecast(
            city_id=dto_dict.get("city_id"),
            weather_id=dto_dict.get("weather_id"),
            temperature=dto_dict.get("temperature"),
            wind_speed=dto_dict.get("wind_speed"),
            humidity=dto_dict.get("humidity"),
            precipitation_probability=dto_dict.get("precipitation_probability")

        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "city_id": self.city_id,
            "weather_id": self.weather_id,
            "temperature": self.temperature,
            "wind_speed": self.wind_speed,
            "humidity": self.humidity,
            "precipitation_probability": self.precipitation_probability
        }
