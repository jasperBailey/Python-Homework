united_kingdom = [
  {
    "name": "Scotland",
    "population": 5_295_000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3_063_000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53_010_000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list
# (The capital is Belfast, and the population is 1,811,000).
northern_ireland = {
    "name": "Northern Ireland",
    "population": 1_811_000,
    "capital": "Belfast"
}
united_kingdom.append(northern_ireland)

# 3. Use a loop to print the names of all the countries in the UK.
for elem in united_kingdom:
    print(elem["name"])

# 4. Use a loop to find the total population of the UK.
total_population = 0
for elem in united_kingdom:
    total_population += elem["population"]
print(total_population)