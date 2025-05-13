#  read the contents of a file named 'frankenstein.txt' located in a 'books' directory and print it to the console.
from stats import word_count

def get_book_text(path):
    return open(path).read()


def main():
    print(f"{word_count(get_book_text('books/frankenstein.txt'))} words found in the document")

main()