def celsius_to_fahrenheit(current):
    temp_in_fahrenheit = ((9 * current) + 160) / 5
    return temp_in_fahrenheit


def fahrenheit_to_celsius(current):
    temp_in_celsius = (((5 * current) - 160) / 9)
    return temp_in_celsius


current_temperature = input("Please enter current temperature. C/c or F/f accepted: ")
truncated_temperature = int(current_temperature[0:2])
temp_type = current_temperature[-1:]
print()
print()

if temp_type == "C" or temp_type == "c":
    converted_temp = (celsius_to_fahrenheit(truncated_temperature))
    print(f"The current temperature is {converted_temp}f.")

if temp_type == "F" or temp_type == "f":
    converted_temp = (fahrenheit_to_celsius(truncated_temperature))
    print(f"The current temperature is {converted_temp}c.")
