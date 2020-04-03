import requests


def get_us_current():
    res = requests.get("https://coronavirus-19-api.herokuapp.com/countries/usa").json()
    return res

class CovidDataUS():
    __slots__ = ('cases', 'today', 'deaths', 'recovered')

    def __init__(self):
        self.update()

    def update(self):
        res = requests.get("https://coronavirus-19-api.herokuapp.com/countries/usa").json()
        self.cases = res["cases"]
        self.today = res["todayCases"]
        self.deaths = res["deaths"]
        self.recovered = res["recovered"]



