"""
Module to read and plot the 2014 population of ASEAN countries from a CSV file.
"""
import csv
from pathlib import Path

from bar_plots import bar_plot


DATA_CSV = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "population.csv"
)

ASEAN_COUNTRIES = [
    "Brunei Darussalam",
    "Cambodia",
    "Indonesia",
    "Lao PDR",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Viet Nam",
]


def asian_pop_2014(data_path):
    """Read the population of ASEAN countries for 2014."""
    asian_pop = {}

    with open(data_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            country = row["Country Name"].strip()
            year = int(row["Year"])

            if country in ASEAN_COUNTRIES and year == 2014:
                population = float(row["Value"])
                asian_pop[country] = population

    return asian_pop


if __name__ == "__main__":
    asian_population = asian_pop_2014(DATA_CSV)

    countries = list(asian_population.keys())
    populations_2014 = list(asian_population.values())

    bar_plot(
        x_bar=countries,
        y_bar=populations_2014,
        x_label="ASEAN Countries",
        y_label="Population",
        title="ASEAN Countries Population in 2014",
    )