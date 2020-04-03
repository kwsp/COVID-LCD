import time
import RPi.GPIO as GPIO
import covid_api
from lcd import gpio_init, lcd_init, lcd_print


def main():
    # Initialise GPIO pins
    gpio_init()

    # Initialise display
    lcd_init()

    while True:
        data = covid_api.get_us_current()
        lcd_print("US Positive", "{}".format(data.get("positive")))
        time.sleep(3)

        lcd_print("US Death", "{}".format(data.get("death")))
        time.sleep(3)

        lcd_print("US Recovered", "{}".format(data.get("recovered")))
        time.sleep(3)

        lcd_print("COVID-19", "US Tracker")
        time.sleep(1)


# Begin program
try:
    main()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
