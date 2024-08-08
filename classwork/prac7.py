"""Module to demonstrate the use of list comprehensions and dictionary comprehensions."""

prods = []
N = 1

while N < 6:
    p = ("product-" + str(N), 2, "6-1-2-23", 5.99)
    prods.append(p)
    N = N+1

item, quantity, date, price = prods[-1]
print(item)

exams = ['SAP', 'DBS', 'MLS', 'DAS', 'DOP', 'PAS', 'ANS', 'CLF']
scores = [969, 838, 815, 806, 922, 806, 765, 988]

# results = exam: score for exam, score in zip(exams, scores)   # This is a dictionary comprehension
results = dict(zip(exams, scores))
print(results)

products = [
    {'Name': 'Widget A', 'SKU': 'ABC', 'Price': 49, 'Shipping': 3.50},
    {'Name': 'Widget B', 'SKU': 'DEF', 'Price': 19, 'Shipping': 2.50},
    {'Name': 'Widget C', 'SKU': 'GHI', 'Price': 75, 'Shipping': 4.00},
    {'Name': 'Widget D', 'SKU': 'JKL', 'Price': 54, 'Shipping': 5.00},
    {'Name': 'Widget E', 'SKU': 'MNO', 'Price': 14, 'Shipping': 3.50},
    {'Name': 'Widget F', 'SKU': 'PQR', 'Price': 11, 'Shipping': 4.50},
    {'Name': 'Widget G', 'SKU': 'STU', 'Price': 39, 'Shipping': 5.50},
]

newprod = [product.update({'Shipping': 0.00}) for product in products if product['Price'] > 20]

newprod1 = [product['Shipping'] == 0.00 for p, product in enumerate(products) if product['Price'] > 20]

newprod2 = [p.update({'Shipping': 0.00}) for p in products if p.get('Price') > 20]

print(list(newprod))
print(list(newprod1))
print(products)

courses = {
    '101': {
        'name': 'Python I',
        'quarter': 1,
        'instructor': 'Richard Roe',
        'level': 100
    },
    '102': {
        'name': 'Python II',
        'quarter': 2,
        'instructor': 'Jane Doe',
        'level': 200
    },
    '103': {
        'name': 'Python III',
        'quarter': 3,
        'instructor': 'John Smith',
        'level': 300
    },
}

print("--------")
print(courses['102']['instructor'])


print(courses.get('102').get('instructor'))

car_colors = {
    'silver': '5',
    'black': '4',
    'gray': '3',
    'white': '2',
    'black': '1',
    'gold': '6'
}

print(car_colors.pop('silver'))

cars ={'s90', 'x3', '911', 'cx-90', '528i', 'a4'}


#print(cars.pop())
cars.discard('a4')
print(cars)
