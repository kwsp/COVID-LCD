from typing import NamedTuple

# import bs4
# from bs4 import BeautifulSoup
import requests


class CovidData(NamedTuple):
    cases: str
    today: str
    deaths: str
    recovered: str

    # @classmethod
    # def from_worldometer_country(cls, country: str = "USA") -> "CovidData":

    # try:
    # row = get_row(country)
    # country = row.td
    # cases = country.find_next("td")
    # today = cases.find_next("td")
    # deaths = today.find_next("td")
    # recovered = deaths.find_next("td").find_next("td")
    # except Exception as e:
    # raise ValueError("Parsing of worldometer country data failed: {}".format(e))

    # return cls(
    # cases=cases.string.strip(),
    # today=today.string.strip(),
    # deaths=deaths.string.strip(),
    # recovered=recovered.string.strip(),
    # )

    @classmethod
    def from_api(cls, country: str = "USA") -> "CovidData":
        try:
            data = requests.get("https://corona.lmao.ninja/countries/" + country).json()
        except Exception as e:
            raise ValueError("API call failed: {}".format(e))

        return cls(
            cases=data["cases"],
            today=data["todayCases"],
            deaths=data["deaths"],
            recovered=data["recovered"],
        )


# def parse_wordometer() -> bs4.element.ResultSet:
# """
# Parse the worldometer covid 19 page
# Return the data table in soup format
# """
# worldometer_page = requests.get("https://www.worldometers.info/coronavirus/")

# soup = BeautifulSoup(worldometer_page.text, "html.parser")

# # Find all table rows
# rows = soup.find_all("tr")

# return rows


# def get_row(country: str = "USA") -> bs4.element.Tag:
# """
# Find the USA row from the table
# """
# rows = parse_wordometer()

# for row in rows[1:]:
# if row.td.string == country:
# return row

# raise ValueError("Country name not found")


# if __name__ == "__main__":
# data = CovidData.from_worldometer_country()
# breakpoint()
