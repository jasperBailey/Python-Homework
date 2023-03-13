users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jon_twitter_handle = users["Jonathan"]["twitter"]
print(jon_twitter_handle)

# 2. Get Erik's hometown
erik_hometown = users["Erik"]["home_town"]
print(erik_hometown)

# 3. Get the list of Erik's lottery numbers
erik_lottery_numbers = users["Erik"]["lottery_numbers"]
print(erik_lottery_numbers)

# 4. Get the species of Avril's pet Monty
avril_pet_species = users["Avril"]["pets"][0]["species"]
print(avril_pet_species)

# 5. Get the smallest of Erik's lottery numbers
erik_smallest_lottery_number = min(erik_lottery_numbers)
print(erik_smallest_lottery_number)

# 6. Return an list of Avril's lottery numbers that are even
avril_even_lottery_numbers = []
for num in users["Avril"]["lottery_numbers"]:
    if num % 2 == 0:
        avril_even_lottery_numbers.append(num)
print(avril_even_lottery_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
erik_lottery_numbers.append(7)
#works because this variable points to the same List object as I didn't make it a copy!
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append(
    {
        "name": "fluffy",
        "species": "dog"
    }
)

print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
users["Jasper"] = {
    "twitter": "jabba_jb",
    "home_town" : "Edinburgh",
    "lottery_numbers": [3, 13, 14, 26, 43, 49],
    "pets": [
        {
            "name": "macy",
            "species": "cat"
        },
        {
            "name": "kit",
            "species": "cat"
        }
    ]
}

print(users["Jasper"])