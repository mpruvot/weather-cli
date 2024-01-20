# WeatherStack CLI

WeatherStack CLI is a command-line interface (CLI) application that fetches weather data for a specific city using the WeatherStack API.

## Table of Contents

- [WeatherStack CLI](#weatherstack-cli)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Usage](#usage)

## Introduction

This CLI application utilizes Typer to provide an interactive way to retrieve weather data for a given city. The weather information includes temperature, humidity, weather code, wind speed, wind direction, and local time.

## Project Structure

- **app:** Contains the main application files.
  - **main.py:** The entry point for the CLI application.
  - **weather_data.py:** Contains the WeatherData class that is responsible for fetching and processing weather data from the WeatherStack API.
- **venv:** Virtual environment for managing dependencies.
- **.env_example:** An example environment file. You need to replace the placeholder with your actual WeatherStack API key and rename the file to `.env`.
- **.gitignore:** Specifies intentionally untracked files that Git should ignore.
- **README.md:** This file, which provides an overview of the project and instructions for installation and usage.
- **requirements.txt:** Lists the Python dependencies required by the project.

## Installation

Before running the application, install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Usage
To fetch weather data for a specific city, run the following command:

```
python app/main.py <city_name>
```

Replace <city_name> with the name of the city you want to fetch weather data for.

Environment Variables
Don't forget to replace the placeholder in .env_example with your actual WeatherStack API key and rename the file to .env. The application reads from this file to get the API key.

