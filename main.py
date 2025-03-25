# open text file and read content
def open_text(file_path):
    with open (file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content

# split text into words
def split_text(text):
        word_count = len(text.split())
        return word_count


def main():
    text = open_text('books/frankenstein.txt')
    word_count = split_text(text)
    print(f'{word_count} words found in the document')


main()
