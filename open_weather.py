import requests



WEATHER = "API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
KELVIN = 273.15

city = input("Enter the city name: ")

request_url = f"{BASE_URL}?q={city}&appid={WEATHER}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data.keys())
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - KELVIN, 2)
    print(f"The weather for {city} is {weather} and the temperature is {temperature}C. ")
else:
    print("Invalid city name")