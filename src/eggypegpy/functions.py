from string import punctuation

VOWELS = "aeiou"


def translate_word(word):
    """Translate an English word to Eggy Peggy.

    Args:
        word (string): The English word to translate.

    Returns:
        [string]: The translated word in Eggy Peggy.
    """
    # strip word and remove punctuation
    new_word = word.lower().strip(punctuation)
    # if word is not all letters, return word as is
    if not new_word.isalpha():
        return word

    translation = ""

    # if word is of length 1
    if len(new_word) == 1:
        # if it is a vowel, add "egg"
        if new_word in VOWELS:
            translation = "egg" + new_word

    # if translation is empty
    if not translation:
        # add "egg" before all starting vowel groups, not including "y" as a consonant
        for index, letter in enumerate(new_word):
            if letter in VOWELS and new_word[index - 1] not in VOWELS:
                if letter == "e" and index == len(new_word) - 1:
                    translation += letter
                else:
                    translation += "egg" + letter
            else:
                if letter == "y" and not index == 0:
                    translation += "egg" + letter
                translation += letter

    # if word is all uppercase, return the translation that way
    if word.strip(punctuation).isupper() and not len(word) == 1:
        return translation.upper()

    # if word is capitalized, return the translation that way
    if word.strip(punctuation)[0].isupper():
        return translation.capitalize()

    return translation
