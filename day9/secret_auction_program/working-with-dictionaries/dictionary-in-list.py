travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visted , times_visited, cities_visted):
   new_country = {}
   new_country["country"] = country_visted
   new_country["visits"] = times_visited
   new_country["cities"] = cities_visted
   travel_log.append(new_country)               #remember .append adds to the end of list


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)