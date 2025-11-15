import requests

def main():
    API_KEY = "9498c5c6f88b8633198ecb4f2182314f"
    LAT = 7.367
    LON = 45.133

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        temp = data["main"]["temp"]
        conditions = data["weather"][0]["description"]

        print("Current Weather:")
        print(f"Temperature: {temp}°C")
        print(f"Conditions: {conditions}")

    except requests.exceptions.HTTPError as err:
        print("HTTP error:", err)
    except requests.exceptions.ConnectionError:
        print("Network error: Unable to connect to the weather service.")
    except Exception as err:
        print("Unexpected error:", err)

if __name__ == "__main__":
    main()