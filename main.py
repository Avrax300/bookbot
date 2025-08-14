from stats import get_word_count
from stats import get_character_count
from stats import sort_characters
import sys

# converts the content of frankenstein.txt as a string.
def get_book_text():
    with open(f"{sys.argv[1]}") as f:
        text = f.read()
        return text

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text()
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print(f"----------- Word Count ----------")
        get_word_count(text)
        character_count = get_character_count(text)
        print(f"--------- Character Count -------")
        sort_characters(character_count)
        print(f"============= END ===============")

main()