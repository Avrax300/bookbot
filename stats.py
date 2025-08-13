# counts the number of words in the file.
def get_word_count(text):
    nb_words = len(text.split())
    print(f"{nb_words} words found in the document")

# lists and counts the number of characters used in the book.
def get_character_count (text):
    characters = {}
    lowercase_text = text.lower()
    words = lowercase_text.split()
    # loops through the entire text word by word and splits them into characters
    for word in words:
        for char in word:
            if char not in characters:
                characters[char] = 1
            else:
                pass
    print (characters)