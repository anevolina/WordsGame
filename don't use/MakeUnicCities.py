citiesF = open("cities.txt", "r", encoding = "utf8")
cities = list(set(map(lambda s: s.strip(), citiesF.readlines())))
cities.sort()

citiesF.close()

citiesF = open("cities.txt", "w", encoding = "utf8")
for city in cities:
    citiesF.write(city + "\n")

citiesF.close()