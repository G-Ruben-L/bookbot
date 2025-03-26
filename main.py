from stats import count_words


# open text file and read content
def open_text(file_path):
    with open (file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content



def main():
    text = open_text('books/frankenstein.txt')
    word_count = count_words(text)
    print(f'{word_count} words found in the document')


main()
