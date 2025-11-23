from stats import get_num_words
from stats import get_sorted_dict
import sys

def print_report(book_text, path_name):
    """Print analysis report for the book."""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_name} ...")

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")

    print("--------- Character Count -------")
    list_dicts = get_sorted_dict(book_text)
    for list_elem in list_dicts:
        print(list_elem["char"] +  ":", list_elem["numb"])
    
    print("============= END ===============")

def check_user_input():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_user_input()
    try:
        with open(sys.argv[1]) as f:
            book_text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found")
        sys.exit(1)
    print_report(book_text, sys.argv[1])

main()