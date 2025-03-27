from stats import count_words
from stats import count_characters

# open text file and read content
def open_text(file_path):
    with open (file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

# call and print word count and counts per character
def main():
    text = open_text('books/frankenstein.txt')
    word_count = count_words(text)
    print(f'{word_count} words found in the document')
    character_count = count_characters(text)
    for char, count in character_count.items():
        print(f"'{char}': {count}")


main()
