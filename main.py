import sys

from stats import count_words
from stats import count_characters
from stats import sort_characters

# open text file and read content
def open_text(file_path):
    with open (file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

# call and print word count and counts per character
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = open_text(path)
    word_count = count_words(text)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {path}")
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    character_count = count_characters(text)
    sorted_characters = sort_characters(character_count)
    for item in sorted_characters:
        print(f"{item['char']}: {item['count']}")
    print('============= END ===============')


main()
