# Task 2: API Integration (Weather)

## Goal
Fetch API data using Requests and display results properly.

## Requirements Met
- ✅ Uses the `requests` module to call a live weather API (wttr.in — free, no key needed)
- ✅ Parses the JSON response returned by the API
- ✅ Search: look up weather for any single city
- ✅ Filter: enter multiple cities and filter results by temperature range or weather condition keyword

## How to Run
```bash
pip install requests
python weather_app.py
```
Menu options:
1. Search a single city
2. Search & filter multiple cities (by temperature range or condition keyword)
3. Exit

## Sample Output
```
1. Search a single city
2. Search & filter multiple cities
3. Exit
Choose an option: 1
Enter a city name: bengaluru
---------------------------------------------
Weather for Bangalore, Karnataka, India
---------------------------------------------
Condition     : Partly cloudy
Temperature   : 25°C (feels like 27°C)
Humidity      : 69%
Wind Speed    : 35 km/h
---------------------------------------------
```

## Deliverables
- ✅ Python script (`weather_app.py`)
- ✅ GitHub link (this folder)
- ✅ Sample output (above, from a real run)
