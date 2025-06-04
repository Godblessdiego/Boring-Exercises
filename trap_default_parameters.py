def filter_words(arr, keyword=None):
    if keyword is None:
        return arr
    filtered_elements = []
    for element in arr:
        if keyword in element:
            filtered_elements.append(element)
    return filtered_elements


test = filter_words(["hello", "world", "hero"], "he")
# → ["hello", "hero"]
print(test)
print(filter_words(["hello", "world", "hero"], "he"))  # ["hello", "hero"]
print(filter_words(["apple", "banana", "grape"], "ap"))  # ["apple", "grape"]
print(filter_words(["hi", "bye", "yes"], None))  # ?? What should this do?
