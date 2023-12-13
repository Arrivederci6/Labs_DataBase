from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class WaterTemperature(db.Model, IDto):
    __tablename__ = "water_temperature"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    water_temperature = db.Column(db.DECIMAL(2, 0), nullable=False)
    date = db.Column(db.Date, nullable=False)

    city = relationship('City', back_populates='water_temperatures')

    def __repr__(self):
        return f"WaterTemperature({self.city_id}, {self.water_temperature}, {self.date})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'WaterTemperature':
        obj = WaterTemperature(
            city_id=dto_dict.get("city_id"),
            water_temperature=dto_dict.get("water_temperature"),
            date=dto_dict.get("date")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "city_id": self.city_id,
            "water_temperature": self.water_temperature,
            "date": self.date
        }
