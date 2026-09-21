"""Total SAARC population over the years."""

import csv
from pathlib import Path

from bar_plots import bar_plot


DATA_CSV = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "population.csv"
)

SAARC_COUNTRIES = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka",
]

population_by_year = {}

with open(DATA_CSV, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        country = row["Country Name"]

        if country in SAARC_COUNTRIES:
            year = int(row["Year"])
            population = float(row["Value"])

            if year not in population_by_year:
                population_by_year[year] = 0

            population_by_year[year] += population

years = sorted(population_by_year)
total_population = [
    population_by_year[year]
    for year in years
]

bar_plot(
    years,
    total_population,
    "Year",
    "Total Population",
    "Total SAARC Population Over the Years",
)