def factorial(num):
    if num == 0:
        total_multiplication = 1
        return total_multiplication

    total_product = 1
    for n in range(num, 0, -1):
        total_product *= n

    return total_product

def main():
    print(factorial(5))

main()
