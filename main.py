import requests 
from pprint import pprint

API_KEY = 'b2462bfd708d0604f561e26d128394bb'

city = input('Enter name of the City: ')

sending_response = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY+'&q='+city

weather_data = requests.get(sending_response).json()

pprint(weather_data)  #printing the data in pretty print