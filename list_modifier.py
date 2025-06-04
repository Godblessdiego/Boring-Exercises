def multiply_elements(list, number):
    new_list = []
    for numbers in list:
        total_numbers = numbers * number
        new_list.append(total_numbers)
    return new_list


test = multiply_elements([1, 2, 3], 5)
print(test)
test2 = multiply_elements([], 3)
print(test2)
