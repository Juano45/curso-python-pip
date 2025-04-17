squares = [x**2 for x in range(1,11)]
print(squares)

celsius_temperature = [0, 10, 25, 32, 36, 37, 38, 100]
fahrenheit_temperature = [((9/5) * c + 32) for c in celsius_temperature]
print("Celsius Temperature: ", celsius_temperature)
print("Fahrenheit Temperature: ", fahrenheit_temperature)