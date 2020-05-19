import unittest
from typing import NamedTuple

import requests

BASE_URL = "https://disease.sh"


class CovidData(NamedTuple):
    cases: str
    today: str
    deaths: str
    recovered: str

    @classmethod
    def from_api(cls, country: str = "USA") -> "CovidData":
        try:
            data = requests.get(BASE_URL + "/v2/countries/" + country).json()
        except Exception as e:
            raise ValueError("API call failed: {}".format(e))

        return cls(
            cases=data["cases"],
            today=data["todayCases"],
            deaths=data["deaths"],
            recovered=data["recovered"],
        )

    @classmethod
    def na(cls) -> "CovidData":
        return cls(cases="N/A", today="N/A", deaths="N/A", recovered="N/A")


class TestCovidData(unittest.TestCase):
    def test_api(self):
        data = CovidData.from_api()
        self.assertGreater(data.cases, 0)
        self.assertGreater(data.deaths, 0)
        self.assertGreater(data.recovered, 0)
        self.assertGreater(data.today, 0)

    def test_na(self):
        data = CovidData.na()
        self.assertEqual(data.cases, "N/A")
        self.assertEqual(data.deaths, "N/A")
        self.assertEqual(data.recovered, "N/A")
        self.assertEqual(data.today, "N/A")


if __name__ == "__main__":
    unittest.main()

