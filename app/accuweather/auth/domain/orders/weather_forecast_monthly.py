from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class WeatherForecastMonthly(db.Model, IDto):
    __tablename__ = "weather_forecast_monthly"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    forecast_id = db.Column(db.Integer, db.ForeignKey('weather_forecast.id'))
    dateStart = db.Column(db.Date, nullable=False)
    dateEnd = db.Column(db.Date, nullable=False)
    txt = db.Column(db.String(14), nullable=False)

    weather_forecast = relationship('WeatherForecast', back_populates='weather_forecast_monthlies')
    weather_forecast_dailies = relationship('WeatherForecastDaily', back_populates='weather_forecast_monthly')

    def __repr__(self):
        return f"WeatherForecastMonthly({self.forecast_id}, {self.day_period}, {self.dateStart}, {self.dateEnd},{self.txt}) "

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'WeatherForecastMonthly':
        obj = WeatherForecastMonthly(
            forecast_id=dto_dict.get("forecast_id"),
            dateStart=dto_dict.get("dateStart"),
            dateEnd=dto_dict.get("dateEnd"),
            txt=dto_dict.get("txt")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "forecast_id": self.forecast_id,
            "dateStart": self.dateStart,
            "dateEnd": self.dateEnd,
            "txt": self.txt
        }
