# 🌦️ Python Weather App

A simple command-line weather application built with Python. It fetches real-time weather information from the OpenWeather API based on the city entered by the user.

## Features

* Search weather by city name
* Displays:

  * City Name
  * Weather Description
  * Temperature (°C)
  * Humidity
  * Visibility
  * Wind Speed
* Handles invalid city names
* Allows multiple searches using a loop
* Type `exit` anytime to quit the program

## Technologies Used

* Python
* Requests Library
* OpenWeather API
* JSON
* HTTP Requests

## Installation

1. Clone the repository.
2. Install the required package:

```bash
pip install requests
```

3. Get your free API key from OpenWeather.
4. Open the Python file and replace:

```python
api_key = "YOUR_API_KEY"
```

with your own API key.

5. Run the program:

```bash
python live_weather.py
```

## Example Output

```
Type your city name here
Or type exit to stop here: Raipur

City: Raipur
Description: few clouds
Temperature: 37.15°C
Humidity: 35%
Visibility: 10000
Wind Speed: 6.15
```


