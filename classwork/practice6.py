cars =['s90', 'x3', '911', 'cx-90, 528i', 'a4']
cars2 =['s90', 'x3', '911']
print(cars)
new_cars = ['s500', 'XF', 'Cheyenne']

menu_items = {'pizza', 'pasta', 'salad', 'soup', 'bread'}
#menu_items = menu_items.pop()

list1 = ['pizza', 'pasta', 'salad', 'soup', 'bread']
list2 = [1, 2, 3, 4, 5]
print(menu_items)

zipped_list = list(zip(list1, list2))
zipped_dict = dict(zipped_list)

print(dict(zipped_list))
print(zipped_dict)
print(zipped_list)

utensils = ('fork', 'knife', 'spoon')
print(type(utensils))

needed_items = menu_items.union(utensils)
print(needed_items)

shirts1 = {'S', 'M', 'L', 'XL', 'XXL'}
sizes2 = {'XS','S', 'M', 'L', 'XL', 'XXL', 'XXXL'}

print(shirts1.issubset(sizes2))

grades = ('A', 'C', 'C', 'D', 'A', 'C', 'A', 'D', 'F')
A_grades = grades.count('A')
print(A_grades)

prices = (2, 5, 10, 50)
print(prices*2)

prods = []
n = 1

while n < 6:
    p = ("product-" + str(n), 2, "6-1-2-23", 5.99)
    prods.append(p)
    n = n+1

item, quantity, date, price = prods[-1]
print(item)