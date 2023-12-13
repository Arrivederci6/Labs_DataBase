from sqlalchemy.orm import relationship

from accuweather import db
from typing import Dict, Any

from accuweather.auth.domain.i_dto import IDto


class Region(db.Model, IDto):
    __tablename__ = "region"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    region_name = db.Column(db.String(45), nullable=False)

    country = relationship('Country', back_populates='regions')
    cities = relationship('City', back_populates='region')

    def __repr__(self):
        return f"Region({self.country_id}, {self.region_name})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'Region':
        obj = Region(
            country_id=dto_dict.get("country_id"),
            region_name=dto_dict.get("region_name")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "country_id": self.country_id,
            "region_name": self.region_name
        }
