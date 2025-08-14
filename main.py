from stats import get_word_count
from stats import get_character_count
from stats import sort_characters

# converts the content of frankenstein.txt as a string.
def get_book_text():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        return text

def main():
    text = get_book_text()
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    get_word_count(text)
    character_count = get_character_count(text)
    print(f"--------- Character Count -------")
    sort_characters(character_count)
    print(f"============= END ===============")

main()