def reverse_string(string):
    words = string.split()
    reversed_list = []
    for i in range(len(words) - 1, -1, -1):
        reversed_list.append(words[i])
    return " ".join(reversed_list)


test = reverse_string("Hello, World!")
print(test)
