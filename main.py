from stats import get_num_chars
from stats import get_num_words
from stats import get_sorted_dict
import sys

def wrapper(path_name, func):
    with open(path_name) as f:
        return func(f.read())

def print_report(path_name):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path_name + "...")
    print("----------- Word Count ----------")
    print(wrapper(path_name, get_num_words))
    print("--------- Character Count -------")
    list_dicts = wrapper(path_name, get_num_chars)
    for list_elem in list_dicts:
        print(list_elem["char"] +  ":", list_elem["numb"])
    print("============= END ===============")

def check_user_input():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_user_input()
    char_dict = print_report(sys.argv[1])

main()