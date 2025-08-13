from stats import get_word_count
from stats import get_character_count

# converts the content of frankenstein.txt as a string.
def get_book_text():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        return text

def main():
    text = get_book_text()
    get_word_count(text)
    character_count = get_character_count(text)

main()