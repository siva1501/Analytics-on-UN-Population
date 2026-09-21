"""
Module to read and plot India's population data from a CSV file.
"""

import csv
from pathlib import Path

from bar_plots import bar_plot


DATA_CSV = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "country_pop.csv"
)
def india_population(data_path):
    """Read population data for India from a CSV file."""
    country = "india"
    year_population = {}
    with open(data_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            get_country = row["country"].strip().lower()
            get_population = float(row["population"])
            year = int(row["year"])
            if get_country == country:
                year_population[year] = get_population
    return year_population
    
if __name__ == "__main__":
    year_population_dict = india_population(DATA_CSV)

    years = list(year_population_dict.keys())
    population = list(year_population_dict.values())

    bar_plot(
        years,
        population,
        "Years",
        "Population",
        "India Population over Years",
    )