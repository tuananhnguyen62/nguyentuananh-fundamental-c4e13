from haversine import haversine
hanoi = {
    'city': 'Hà Nội',
    'lat' : 21,
    'long': 105
}
paris = {
    'city': 'Paris',
    'lat' : 48.86,
    'long': 2.35
}
lyon = {
    'city': 'Lyon',
    'lat' : 45.76,
    'long': 4.84
}
cities = [
    {
        'city': 'Hà Nội',
        'lat' : 21,
        'long': 105
    },
    {
        'city': 'Paris',
        'lat' : 48.86,
        'long': 2.35
    },
    {
        'city': 'Lyon',
        'lat' : 45.76,
        'long': 4.84
    }
]
n = len(cities)
for i in range(0, n -1):
    for j in range(i +1, n):
        city1 = cities[i]
        city2 = cities[j]

        cord1 = [city1['lat'],city1['long']]
        cord2 = [city2['lat'],city2['long']]


        distance = haversine(cord1, cord2)
        print("Khoang cach tu {0} den {1} la {2} km".format(city1['city'], city2['city'],distance))
