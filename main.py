import time
import RPi.GPIO as GPIO
import covid_api
from lcd import gpio_init, lcd_init, lcd_print

API_UPDATE_INTERVAL = 60 * 5


def main():
    # Initialise GPIO pins
    gpio_init()

    # Initialise display
    lcd_init()

    covid_data = covid_api.CovidData.from_worldometer_country()
    last_update = time.time()

    while True:
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
            covid_data.update()
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
