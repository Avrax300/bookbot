# counts the number of words in the file.
def get_word_count(text):
    nb_words = len(text.split())
    print(f"{nb_words} words found in the document")

# lists and counts the number of characters used in the book.
def get_character_count (text):
    character_count = {}
    lowercase_text = text.lower()
    words = lowercase_text.split()
    # loops through the entire text word by word and splits them into characters
    for word in words:
        for char in word:
            # if the character does not exist yet, add it to the dictionary, else increase its count
            if char not in character_count:
                character_count[char] = 1
            else:
                character_count[char] += 1
    return character_count

def sort_characters(character_count):
    sorted_chars = []
    # creates individual dictionaries for each character and add them to a list
    for character in character_count:
        extracted_chars = {}
        extracted_chars["char"] = character
        extracted_chars["num"] = character_count[character]
        sorted_chars.append(extracted_chars)
    print(sorted_chars)

