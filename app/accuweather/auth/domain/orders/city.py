from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class City(db.Model, IDto):
    __tablename__ = "city"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    city_name = db.Column(db.String(45), nullable=False)
    latitude = db.Column(db.Double, nullable=False)
    longtitude = db.Column(db.Double, nullable=False)

    region = relationship('Region', back_populates='cities')
    water_temperatures = relationship('WaterTemperature', back_populates='city')
    air_qualities = relationship('AirQuality', back_populates='city')
    weather_cataclysm_warnings = relationship('WeatherCataclysmWarning', back_populates='city')
    weather_forecasts = relationship('WeatherForecast', back_populates='city')

    def __repr__(self):
        return f"City({self.region_id}, {self.city_name}, {self.latitude}, {self.longtitude})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'City':
        obj = City(
            region_id=dto_dict.get("region_id"),
            city_name=dto_dict.get("city_name"),
            latitude=dto_dict.get("latitude"),
            longtitude=dto_dict.get("longtitude")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "region_id": self.region_id,
            "city_name": self.city_name,
            "latitude": self.latitude,
            "longtitude": self.longtitude
        }
