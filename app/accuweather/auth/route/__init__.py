from flask import Flask


def register_routes(app: Flask) -> None:
    from accuweather.auth.route.orders.air_quality import air_quality_bp
    from accuweather.auth.route.orders.city import city_bp
    from accuweather.auth.route.orders.country import country_bp
    from accuweather.auth.route.orders.region import region_bp
    from accuweather.auth.route.orders.water_temperature import water_temperature_bp
    from accuweather.auth.route.orders.weather import weather_bp
    from accuweather.auth.route.orders.weather_cataclysm_warning import weather_cataclysm_warning_bp
    from accuweather.auth.route.orders.weather_forecast import weather_forecast_bp
    from accuweather.auth.route.orders.weather_forecast_daily import weather_forecast_daily_bp
    from accuweather.auth.route.orders.weather_forecast_hourly import weather_forecast_hourly_bp

    app.register_blueprint(air_quality_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(country_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(water_temperature_bp)
    app.register_blueprint(weather_bp)
    app.register_blueprint(weather_cataclysm_warning_bp)
    app.register_blueprint(weather_forecast_bp)
    app.register_blueprint(weather_forecast_daily_bp)
    app.register_blueprint(weather_forecast_hourly_bp)
