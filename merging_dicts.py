def merge(dict1, dict2):
    new_dict = {}
    for element1 in dict1:
        new_dict[element1] = dict1[element1]
    for element2 in dict2:
        new_dict[element2] = dict2[element2]
    return new_dict
