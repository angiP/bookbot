from collections import defaultdict

def get_num_words(book_text):
    num_words = len(book_text.split())
    print("Found", num_words, "total words")

def get_num_chars(book_text):
    
    new_text = book_text.lower()
    char_dict = defaultdict(int)

    for char in new_text:
        char_dict[char] = char_dict[char] + 1
    
    # print(char_dict)
    return get_sorted_dict(char_dict)

def get_sorted_dict(char_dict):
    sorted_list_of_dict = []

    for key, val in char_dict.items():
        if key.isalpha():
            sorted_list_of_dict.append({"char": key, "numb": val})
    # print(sorted_list_of_dict)

    return sorted(sorted_list_of_dict, key=lambda x: x['numb'], reverse = True)

