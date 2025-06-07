def calculate_experience_points(level):
    total_experience = 0
    for i in range(1, level):
        total_experience += i * 5
    return total_experience

test = calculate_experience_points(5)
print(test)
