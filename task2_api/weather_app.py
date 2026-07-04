"""
API Integration - Weather Lookup Tool
Internship Task 2: API Integration (Weather / Crypto / News)

Goal:
    Fetch live weather data using the Requests module, parse the
    JSON response, and let the user search for any city.

Uses wttr.in's free JSON weather API (no API key/signup required),
so this runs out-of-the-box for grading/demo purposes.

Author: Riya Gupta
"""

import requests


def get_weather(city):
    """
    Fetch current weather data for a given city using wttr.in's
    free JSON API and return a parsed dictionary of key details.
    """
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises HTTPError for bad status codes

        data = response.json()

        current = data["current_condition"][0]
        area = data["nearest_area"][0]

        weather_info = {
            "city": area["areaName"][0]["value"],
            "region": area["region"][0]["value"],
            "country": area["country"][0]["value"],
            "temp_C": current["temp_C"],
            "feels_like_C": current["FeelsLikeC"],
            "condition": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "wind_kmph": current["windspeedKmph"],
        }
        return weather_info

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error: please check your internet connection.")
    except requests.exceptions.Timeout:
        print("The request timed out. Try again.")
    except (KeyError, IndexError):
        print(f"Could not parse weather data for '{city}'. Check the city name.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return None


def display_weather(info):
    """Nicely print the weather details."""
    print("-" * 45)
    print(f"Weather for {info['city']}, {info['region']}, {info['country']}")
    print("-" * 45)
    print(f"Condition     : {info['condition']}")
    print(f"Temperature   : {info['temp_C']}°C (feels like {info['feels_like_C']}°C)")
    print(f"Humidity      : {info['humidity']}%")
    print(f"Wind Speed    : {info['wind_kmph']} km/h")
    print("-" * 45)


def search_multiple_cities(cities):
    """Fetch weather for a list of cities. Returns list of result dicts."""
    results = []
    for city in cities:
        city = city.strip()
        if not city:
            continue
        info = get_weather(city)
        if info:
            results.append(info)
    return results


def filter_by_temperature(results, min_temp=None, max_temp=None):
    """Filter a list of weather results by a temperature range (°C)."""
    filtered = []
    for r in results:
        try:
            temp = float(r["temp_C"])
        except (ValueError, TypeError):
            continue
        if min_temp is not None and temp < min_temp:
            continue
        if max_temp is not None and temp > max_temp:
            continue
        filtered.append(r)
    return filtered


def filter_by_condition(results, keyword):
    """Filter a list of weather results by a condition keyword (e.g. 'rain', 'clear')."""
    keyword = keyword.lower()
    return [r for r in results if keyword in r["condition"].lower()]


def run_single_search():
    city = input("Enter a city name: ").strip()
    if not city:
        print("Please enter a valid city name.")
        return
    info = get_weather(city)
    if info:
        display_weather(info)


def run_multi_city_filter():
    raw = input("Enter city names separated by commas (e.g. Delhi,London,Tokyo): ").strip()
    cities = [c for c in raw.split(",") if c.strip()]
    if not cities:
        print("No valid cities entered.")
        return

    print(f"\nFetching weather for {len(cities)} cities...")
    results = search_multiple_cities(cities)

    if not results:
        print("No results could be fetched.")
        return

    print("\nFilter options:")
    print("  1. Filter by temperature range")
    print("  2. Filter by weather condition keyword (e.g. 'rain', 'clear')")
    print("  3. No filter — show all")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == "1":
        min_t = input("Minimum temperature (°C, leave blank for none): ").strip()
        max_t = input("Maximum temperature (°C, leave blank for none): ").strip()
        min_temp = float(min_t) if min_t else None
        max_temp = float(max_t) if max_t else None
        filtered = filter_by_temperature(results, min_temp, max_temp)
    elif choice == "2":
        keyword = input("Enter condition keyword: ").strip()
        filtered = filter_by_condition(results, keyword)
    else:
        filtered = results

    if not filtered:
        print("\nNo cities matched your filter.")
    else:
        print(f"\n{len(filtered)} of {len(results)} cities matched:")
        for info in filtered:
            display_weather(info)


def main():
    print("=" * 45)
    print(" WEATHER LOOKUP TOOL (Requests + JSON)")
    print("=" * 45)

    while True:
        print("\n1. Search a single city")
        print("2. Search & filter multiple cities")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_single_search()
        elif choice == "2":
            run_multi_city_filter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
