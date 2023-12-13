from accuweather import db
from typing import Dict, Any
from sqlalchemy.orm import relationship

from accuweather.auth.domain.i_dto import IDto


class WeatherForecastHourly(db.Model, IDto):
    __tablename__ = "weather_forecast_hourly"

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    forecast_id = db.Column(db.Integer, db.ForeignKey('weather_forecast.id'))
    date = db.Column(db.Date, nullable=False)

    weather_forecast = relationship('WeatherForecast', back_populates='weather_forecast_hourlies')

    def __repr__(self):
        return f"WeatherForecastHourly({self.forecast_id}, {self.day_period}, {self.date})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> 'WeatherForecastHourly':
        obj = WeatherForecastHourly(
            forecast_id=dto_dict.get("forecast_id"),
            date=dto_dict.get("date")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "forecast_id": self.forecast_id,
            "date": self.date
        }
