def count_words(raw_book):
    word_list = raw_book.split()
    words = len(word_list)
    #print(f"{words} words found in the document")
    return words

def count_characters(car_book):
    #print("started")
    character_count = {}
    for car in car_book: 
        #print(car)
        car_lower = car.lower()
        character_count[car_lower] = character_count.get(car_lower, 0) + 1
        #print(character_count)
    return character_count

def sort_character_counts(char_counts_dict):
    """
    Converts a character count dictionary into a sorted list of dictionaries.
    Each dictionary in the list will have "char" and "num" keys.
    Non-alphabetic characters are skipped.
    The list is sorted by 'num' (count) in descending order.
    """
    sorted_list = []
    for char, count in char_counts_dict.items():
        if char.isalpha(): # Only include alphabetical characters
            sorted_list.append({"char": char, "num": count})

    # Sort the list of dictionaries by the 'num' value in reverse (descending) order
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list