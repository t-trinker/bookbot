from stats import get_word_count
from stats import get_book_text
from stats import get_letter_count
from stats import get_sorted_letter_dict
import sys

def create_book_report(filepath: str) -> None:
    booktext = get_book_text(filepath)
    num_words = get_word_count(booktext)
    num_letters = get_letter_count(booktext)
    sorted_letters = get_sorted_letter_dict(num_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    create_book_report(sys.argv[1])
    
main()