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
        city_dict = res.json()

        print("The weather in " + city + ", " + city_dict['sys']['country'] +
              " is:\n")

        loop_guard = True
        while loop_guard:
            choice = input("\nWould you like to enter another city?(Y/N): ")

            if choice.upper() == 'N':
                run = False
                loop_guard = False
            elif choice.upper() == 'Y':
                loop_guard = False

    else:

        print("The city wasn't found please try again.")

