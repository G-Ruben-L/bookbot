# split text into words and count words
def count_words(text):
        word_count = len(text.split())
        return word_count

# counting the occurrence of each character in text
def count_characters(text):
        character_count = {}
        for char in text.lower():
                if char not in character_count:
                        character_count.update({char: 1})
                else:
                        character_count[char] += 1

        return character_count
