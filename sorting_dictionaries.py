def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    max_count_enemy = None
    if len(enemies_dict) == 0:
        return None
    for enemies_name in enemies_dict:
        if enemies_dict[enemies_name] > max_so_far:
            max_so_far = enemies_dict[enemies_name]
            max_count_enemy = enemies_name
    return max_count_enemy
