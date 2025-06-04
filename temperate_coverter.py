def celcius_to_fahrenheit(celcius, fahrenheit):
    celc_to_fahren = (celcius * 9 / 5) + 32
    total_f = f"The fahrenheit temperature is {celc_to_fahren}"
    fahrenheit_to_celc = (fahrenheit - 32) * 5 / 9
    total_c = f"The celcius temperature is {fahrenheit_to_celc}"

    return total_f, total_c


c = celcius_to_fahrenheit(100, 32)
d = celcius_to_fahrenheit(10, 73)

print(c)
print(d)
