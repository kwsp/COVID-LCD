import requests


def get_us_current():
    res = requests.get("http://covidtracking.com/api/us").json()
    return res[0]
