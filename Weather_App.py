import requests

country=input("Enter your country in short form(like 'in' for India):")
city=input("Enter your city:")
location=",".join([city,country])

api_key="Your_api_key" # get your api key from openweatherapp
url=(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}")

response=requests.get(url)
data=response.json()

print(f"\nRegion:{city.capitalize()},{country.upper()}")
print(f"Weather:{(data["weather"][0]["description"]).capitalize()}")
print(f"Temperature(in farenhit):{data["main"]["temp"]}, feels like:{data["main"]["feels_like"]}")
print(f"Humidity:{data["main"]["humidity"]} and Pressure:{data["main"]["pressure"]}")
print(f"Visibility:{data["visibility"]}")
print(f"Wind speed:{data["wind"]["speed"]}")

