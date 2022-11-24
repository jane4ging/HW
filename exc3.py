postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"

}
postcards["Oleg"] = "Sydney"
postcards["Petra"] = "Paris"
postcards["Ivan"] = "Moscow"
print(postcards)

cities = set(postcards.values())
print(cities)

print(len(cities))

# 8 cities

print(*cities)

# London Calgary Paris Murmansk Krakow Milan Moscow Sydney