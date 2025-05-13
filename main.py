#  read the contents of a file named 'frankenstein.txt' located in a 'books' directory and print it to the console.
from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    BOOK = sys.argv[1]


def get_book_text(path):
    return open(path).read()


def main():
    #print(f"{word_count(get_book_text(BOOK))} words found in the document")
    #print(character_stats(get_book_text(BOOK)))
    #print(sorted_character_stats(character_stats(get_book_text(BOOK))))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {BOOK}")
    print("---------- Word Count -----------")
    print(f"Found {word_count(get_book_text(BOOK))} total words")
    print("------- Character Count ---------")
    for character in sorted_character_stats(character_stats(get_book_text(BOOK))):
        if character['character'].isalpha():
            print(f"{character['character']}: {character['count']}")
    print("============ END ===============")
main()