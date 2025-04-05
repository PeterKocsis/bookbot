def get_word_count(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in.
    :return: Number of words in the text.
    """
    
    # Split the text into words and count them
    word_count = len(text.split())
    return word_count

def get_character_count(text):
    charater_stats = {}

    for char in text.lower():
        if char in charater_stats:
            charater_stats[char] += 1
        else:
            charater_stats[char] = 1
    return charater_stats

def sort_character_by_count(character_stats, descending=False):
    sorted_list = []
    for item in list(character_stats.items()):
        sorted_list.append({ "char": item[0],  "count": item[1]})
    sorted_list.sort(key=lambda x: x["count"], reverse= descending)
    return sorted_list

