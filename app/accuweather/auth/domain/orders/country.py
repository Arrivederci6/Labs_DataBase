from sqlalchemy.orm import relationship

from accuweather import db
from typing import Dict, Any

from accuweather.auth.domain.i_dto import IDto


class Country(db.Model, IDto):
    __tablename__ = "country"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    country_name = db.Column(db.String(45), nullable=False)
    latitude = db.Column(db.Double, nullable=False)
    longtitude = db.Column(db.Double, nullable=False)

    regions = relationship('Region', back_populates='country')
    def __repr__(self):
        return f"Country({self.country_name}, {self.latitude}, {self.longtitude})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'Country':
        obj = Country(
            country_name=dto_dict.get("country_name"),
            latitude=dto_dict.get("latitude"),
            longtitude=dto_dict.get("longtitude")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "country_name": self.country_name,
            "latitude": self.latitude,
            "longtitude": self.longtitude
        }
