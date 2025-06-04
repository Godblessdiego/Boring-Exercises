def create_character(name, class_type="Adventurer", health=100, mana=50):
    if name is None:
        raise ValueError("Name cannot be None")
    if health < 0 or mana < 0:
        raise ValueError("Health and Mana must be non-negative")
    if name == "":
        raise ValueError("Name cannot be empty")
    return {"name": name, "class_type": class_type, "health": health, "mana": mana}


print(create_character("Mira"))
print(create_character("Zed", class_type="Assassin", health=80))
print(create_character("Null", health=10))
# print(create_character("", class_type="Mage"))
# print(create_character("Elio", mana="a lot"))
print(create_character("Elio", mana=100))
