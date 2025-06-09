def filter_messages(messages):
    filtered_list = []
    counter_for_removed_words = []

    for w in messages:
        non_bad_words = []
        removed = 0
        words = w.split()
        for u in words:
            if u == "dang" or u == "Dang":
                removed += 1
            else:
                non_bad_words.append(u)
        clean_sentence = " ".join(non_bad_words)
        filtered_list.append(clean_sentence)
        counter_for_removed_words.append(removed)

    return filtered_list, counter_for_removed_words
