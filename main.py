#  read the contents of a file named 'frankenstein.txt' located in a 'books' directory and print it to the console.

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def word_count(text):
    words = text.split()
    return len(words)

def main():
    print(f"{word_count(get_book_text('books/frankenstein.txt'))} words found in the document")

main()