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

def sort_on(dict):
    return dict["count"]


def sort_characters(character_count):
        list_of_dicts = []
        for key in character_count:
                list_of_dicts.append({"char":key, "count": character_count[key]})
        list_of_dicts.sort(reverse=True, key=sort_on)

        return list_of_dicts


# # sorting character count
# def sort_characters(character_count):
#         return list(sorted(character_count.items(), key=lambda x: x[1], reverse=True))