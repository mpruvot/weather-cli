import typer
from weather_data import WeatherData

app = typer.Typer()


@app.command()
def weather(city_name: str):
    """
    Get weather data for a specific city.
    """
    weather_data = WeatherData(city_name)
    typer.echo(f"City: {weather_data.get_city_name()}")
    typer.echo(f"Country: {weather_data.get_country_name()}")
    typer.echo(f"Temperature: {weather_data.get_temperature()}°C")
    typer.echo(f"Humidity: {weather_data.get_humidity()}%")
    typer.echo(f"Weather Code: {weather_data.get_weather_code()}")
    typer.echo(f"Wind Speed: {weather_data.get_wind_speed()} km/h")
    typer.echo(f"Wind Direction: {weather_data.get_wind_direction()}")
    typer.echo(f"Local Time: {weather_data.get_local_time()}")


if __name__ == "__main__":
    app()
