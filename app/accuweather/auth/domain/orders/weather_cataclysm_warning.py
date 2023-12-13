from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class WeatherCataclysmWarning(db.Model, IDto):
    __tablename__ = "weather_cataclysm_warning"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    warning_description = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)

    city = relationship('City', back_populates='weather_cataclysm_warnings')

    def __repr__(self):
        return f"WeatherCataclysmWarning({self.city_id}, {self.warning_description}, {self.date})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'WeatherCataclysmWarning':
        obj = WeatherCataclysmWarning(
            city_id=dto_dict.get("city_id"),
            warning_description=dto_dict.get("warning_description"),
            date=dto_dict.get("date")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "city_id": self.city_id,
            "warning_description": self.warning_description,
            "date": self.date
        }
