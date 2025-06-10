def count_vowels(text):
    total_vowels = 0
    vowels_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    unique_vowels = set()

    for char in text:
        if char in vowels_set:
            total_vowels += 1
            unique_vowels.add(char)
    return total_vowels, unique_vowels