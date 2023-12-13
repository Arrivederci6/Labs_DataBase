from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class WeatherForecastDaily(db.Model, IDto):
    __tablename__ = "weather_forecast_daily"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    forecast_id = db.Column(db.Integer, db.ForeignKey('weather_forecast.id'))
    day_period = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=False)

    weather_forecast = relationship('WeatherForecast', back_populates='weather_forecast_dailies')

    def __repr__(self):
        return f"WeatherForecastDaily({self.forecast_id}, {self.day_period}, {self.date})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'WeatherForecastDaily':
        obj = WeatherForecastDaily(
            forecast_id=dto_dict.get("forecast_id"),
            day_period=dto_dict.get("day_period"),
            date=dto_dict.get("date")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "forecast_id": self.forecast_id,
            "day_period": self.day_period,
            "date": self.date
        }
