import time
import RPi.GPIO as GPIO
import logging

import covid_api
from lcd import gpio_init, lcd_init, lcd_print

API_UPDATE_INTERVAL = 60 * 5


def main():
    # Initialise GPIO pins
    print("Initialising GPIO")
    gpio_init()

    # Initialise display
    print("Initialising LCD")
    lcd_init()

    print("Getting covid data")
    #covid_data = covid_api.CovidData.from_worldometer_country()
    covid_data = covid_api.CovidData.from_api()
    last_update = time.time()

    while True:
        print("Printing data on LCD display")
        lcd_print(
            "US Cases:{:7}".format(covid_data.cases),
            "US Today:{:7}".format(covid_data.today),
        )

        time.sleep(4)

        lcd_print(
            "US Death:{:7}".format(covid_data.deaths),
            "US Recov:{:7}".format(covid_data.recovered),
        )

        new_time = time.time()
        if new_time - last_update > API_UPDATE_INTERVAL:
            print("Getting covid data")
            try:
                #covid_data = covid_api.CovidData.from_worldometer_country()
                covid_data = covid_api.CovidData.from_api()
            except Exception as e:
                print("Parsing worldometer failed, Caught exception: {}".format(e))
                covid_data = covid_api.CovidData.na()

            last_update = new_time
        else:
            time.sleep(4)


# Begin program
try:
    main()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
