import os
import requests


def main() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY is not set!")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        text = data["current"]["condition"]["text"]
        print(f"Weather in Paris: {temp} Celsius, {text}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    main()
