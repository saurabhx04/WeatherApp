import requests 
import datetime 

#api_key = "56e544883e62521a536c81c0a7967a0d"
api_key = "aff4546cfa968d59b4e160a0b1fa5acd"

base_url = "http://api.openweathermap.org/data/2.5/weather"
#print(api_key)

city_name = input("Enter city name: ")

params = {
    'q': city_name,
    'appid': api_key,
    'units': 'metric'  # To get temperature in Celsius
}
response = requests.get(base_url, params=params)
data = response.json()
#print(response)
#print(data)

if data["cod"] == 200:
    # Extract the necessary information
    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]
    sunrise_sunset = data["sys"]
    #sunset = data["sys"]
     
    #sunrise = datetime.datetime.fromtimestamp(sunrise_sunset['sunrise'])
    #sunset = datetime.datetime.fromtimestamp(sunrise_sunset['sunset'])
    

    # Print the weather information
    print(f"City: {city_name}")
    print(f"Temperature: {main['temp']}°C")
    print(f"Feels Like: {main['feels_like']}°C")
    print(f"Weather: {weather['description']}")
    print(f"Humidity: {main['humidity']}%")
    print(f"Wind Speed: {wind['speed']} m/s")
    #print(f"Sunset : {sunset}")
    #print(f"Sunrise : {sunrise}")
    print(f"Sunset : {datetime.datetime.fromtimestamp(sunrise_sunset['sunrise'])}")
    print(f"Sunrise : {datetime.datetime.fromtimestamp(sunrise_sunset['sunset'])}")
else:
    print("City not found, please check the name and try again.")