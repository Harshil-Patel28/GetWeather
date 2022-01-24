from urllib import request
import requests

API_KEY = "efb7ddca990388e37e96615e788890f2"
URL = "http://api.openweathermap.org/data/2.5/weather"

run = True
while run:
    city = input("Please enter a city (Quit or Q to stop): ")

    if city.lower() == 'q' or city.lower() == 'quit':
        run = False
        break

    res = requests.get(f"{URL}?appid={API_KEY}&q={city}")

    if res.status_code == 200:
        print(res.json())

    else:

        print("The city wasn't found please try again.")
