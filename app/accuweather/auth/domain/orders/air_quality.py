from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class AirQuality(db.Model, IDto):
    __tablename__ = "air_quality"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    air_quality = db.Column(db.DECIMAL(3,0), nullable=False)

    city = relationship('City', back_populates='air_qualities')

    def __repr__(self):
        return f"AirQuality({self.city_id}, {self.date}, {self.air_quality})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'AirQuality':
        obj = AirQuality(
            city_id=dto_dict.get("city_id"),
            date=dto_dict.get("date"),
            air_quality=dto_dict.get("air_quality")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "city_id": self.city_id,
            "date": self.date,
            "air_quality": self.air_quality
        }