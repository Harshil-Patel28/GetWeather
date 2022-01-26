from urllib import request
import datetime
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
        #print(city_dict)
        print("\nThe weather in " + city[0].upper() + city[1:] + ", " + city_dict['sys']['country'] +
              " is " + str(round((city_dict['main']['temp'] - 273.15), 2))
              + "°C with " + city_dict['weather'][0]['description'])

        print("Sunrise in " + city[0].upper() + city[1:] +": " +
              str(datetime.datetime.fromtimestamp(city_dict['sys']['sunrise']).time()))

        print("Sunset in " + city[0].upper() + city[1:] +": " +
              str(datetime.datetime.fromtimestamp(city_dict['sys']['sunset']).time()))

        if '-' in str(float((city_dict['timezone'] / 3600) + 5)):
            print(city[0].upper() + city[1:] + "'s Timezone: " +
                  str((float((city_dict['timezone'] / 3600) + 5)) * -1) +
                  " hours behind the Eastern Time Zone.")

        elif str(float((city_dict['timezone'] / 3600) + 5)) == '0.0':
            print(city[0].upper() + city[1:] + "'s Timezone: Eastern Time Zone.")
        else:

            print(city[0].upper() + city[1:] + "'s Timezone:" +
                  str(float((city_dict['timezone'] / 3600) + 5)) +
                  " hours ahead of the Eastern Time Zone.")

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

