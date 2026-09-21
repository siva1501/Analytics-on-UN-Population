"""
Module to read and plot ASEAN population from 2004 to 2014.
"""

import csv
from pathlib import Path

from bar_plots import grouped_bar_plot


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

YEARS = list(range(2004, 2015))


def asean_population(data_path):
    """Read ASEAN population from 2004 to 2014."""
    population = {
        year: {
            country: 0
            for country in ASEAN_COUNTRIES
        }
        for year in YEARS
    }

    with open(data_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            country = row["Country Name"].strip()
            year = int(row["Year"])

            if country in ASEAN_COUNTRIES and year in YEARS:
                population[year][country] = float(row["Value"])

    return population


if __name__ == "__main__":
    population_data = asean_population(DATA_CSV)

    grouped_bar_plot(
        counts=population_data,
        years=YEARS,
        categories=ASEAN_COUNTRIES,
        x_label="Years",
        y_label="Population",
        title="ASEAN Population from 2004 to 2014",
    )