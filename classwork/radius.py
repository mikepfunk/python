# Calculate the area of a circle and assign the value
# to a variable name of area_of_circle.

radius = int(input("Enter the radius of the circle: "))
area_of_circle = 3.14159 * radius ** 2
print(f"The radius is {radius} and the area of the circle is {area_of_circle}")

# take a user input for temp in Farenheit and convert it to Celsius.
# C = (F - 32) x 5/9

temp_f = int(input("Enter the temperature in Farenheit: "))
temp_c = (temp_f - 32) * 5/9
print(f"The temperature in Farenheit is {temp_f} and the temperature in Celsius is {temp_c}")
