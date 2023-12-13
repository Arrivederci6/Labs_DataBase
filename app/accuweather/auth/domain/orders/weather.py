from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class Weather(db.Model, IDto):
    __tablename__ = "weather"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    weather_title = db.Column(db.String(45), nullable=False)
    weather_icon_url = db.Column(db.String(255), nullable=False)

    weather_forecasts = relationship('WeatherForecast', back_populates='weather')

    def __repr__(self):
        return f"Weather({self.weather_title}, {self.weather_icon_url})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'Weather':
        obj = Weather(
            weather_title=dto_dict.get("weather_title"),
            weather_icon_url=dto_dict.get("weather_icon_url")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "weather_title": self.weather_title,
            "weather_icon_url": self.weather_icon_url
        }
