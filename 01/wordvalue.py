from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    file = open("dictionary.txt", "r")
    words = [line.strip("\n") for line in file]
    file.close()
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = sum(
        [
            LETTER_SCORES[letter.upper()]
            for letter in word
            if letter.upper() in LETTER_SCORES.keys()
        ]
    )
    return score


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scored_words = [calc_word_value(word) for word in words]
    max_value = max([(calc_word_value(word)) for word in words])
    max_word = words[scored_words.index(max_value)]
    return max_word


if __name__ == "__main__":
    pass  # run unittests to validate
