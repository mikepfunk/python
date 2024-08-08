marys_catch = [
{"id": 1, "length": 17.0, "weight": 18.2},
{"id": 2, "length": 22.0, "weight": 27.1},
{"id": 3, "length": 20.25, "weight": 21.9},
{"id": 4, "length": 12.5, "weight": 11.5},
{"id": 5, "length": 25.75, "weight": 33.4},
]

marthas_catch = [
{"id": 1, "length": 24.75, "weight": 29.3},
{"id": 2, "length": 9.25, "weight": 6.0},
{"id": 3, "length": 12.0, "weight": 16.8},
{"id": 4, "length": 22.5, "weight": 28.6},
{"id": 5, "length": 23.0, "weight": 29.7},
]

print(marys_catch[0]["length"])
print(marthas_catch[0]["weight"])

print(marys_catch[0].fromkeys)

certs = ['sas', 'sae', 'add', 'wew', 'asa', 'pol', 'jfs', 'asw', 'dgc', 'hes', 'awf']
print(certs[-1])
print(len(certs[-1]))
print(certs[len(certs)-1])


language = {"python", "java", "c++", "Go"}
print(type(language))

dims = [10, 8, 14, 36]
cubed_dims = [d**3 for d in dims]
print(cubed_dims)

cars = [
    {"make": "Volvo", "model": "s90", "color": "silver"},
    {"make": "BMW", "model": "X3", "color": "black"},
    {"make": "Porsche", "model": "911", "color": "gray"},
    {"make": "Mazda", "model": "CX-90", "color": "white"},
    {"make": "BMW", "model": "528i", "color": "black"},
    {"make": "Audi", "model": "a4", "color": "gold"}
    ]
    
BMWs = [car['make'] for car in cars].count("BMW")
print(BMWs)

BMWs2 = cars.count({"make":"BMW"})
print(BMWs2)

for car in cars:
    if car['make'] == "BMW":
        print(car)
        
BMWs3 = len([car for car in cars if car['make'] == "BMW"])
print(BMWs3)

