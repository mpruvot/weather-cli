# WeatherStack CLI

WeatherStack CLI is a command-line interface (CLI) application that fetches weather data for a specific city.

## Introduction

This CLI application utilizes Typer to provide an interactive way to retrieve weather data for a given city. The weather information includes temperature, humidity, weather code, wind speed, wind direction, and local time.

## Project Structure

- **app:** Contains the main application files.
  - **main.py:** The entry point for the CLI application.
  - **weather_data.py:** Module to fetch weather data.
- **requirements.txt:** List of project dependencies.

## Installation

Before running the application, install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

To fetch weather data for a specific city, run the following command in app directory:
````
python main.py <city_name>
````

### Environment Variables
Don't forget to replace the environment variable in .env_example with your WeatherStack API key and rename .env_example to .env.

