def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def get_character_report(char_counts):
    # convert dict to list of dicts
    char_list = [{"char": char, "count": count}
                 for char, count in char_counts.items()]
    # sort by count, descending (hence the reverse=True)
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list
