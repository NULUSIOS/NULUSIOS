programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary["Loop"])

empty_dictionary = {}

programming_dictionary["Bug"] = "A moth inside the computer."
print(programming_dictionary["Bug"])

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

capital = {
  "France": "Paris",
  "Germany": "Berlin",
}

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stutgart"], "total_visits": 5},
}

travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stutgart"],
    "total_visits": 5,
  }
]

