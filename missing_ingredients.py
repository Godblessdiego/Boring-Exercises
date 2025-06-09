def check_ingredient_match(recipe, ingredients):
    match_counter = 0
    missing_ingredients = []

    for i in recipe:
        if i in ingredients:
            match_counter += 1
        else:
            missing_ingredients.append(i)
    percentage = (match_counter / len(recipe)) * 100
    return percentage, missing_ingredients
