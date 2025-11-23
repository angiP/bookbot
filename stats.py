from collections import Counter

def get_num_words(book_text):
    return len(book_text.split())

def get_sorted_dict(book_text):
    
    char_dict = Counter(char.lower() for char in book_text if char.isalpha())
    return  [{"char": char, "numb": count} for char, count in char_dict.most_common()]
