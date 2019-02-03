from data import *


def score_word(word):
    score = sum(
        [
            LETTER_SCORES[letter.upper()]
            for letter in word
            if letter.upper() in LETTER_SCORES.keys()
        ]
    )
    return score


file = open("dictionary.txt", "r")

words = [line.strip("\n") for line in file]

scored_words = [score_word(word) for word in words]
max_value = max([(score_word(word)) for word in words])
max_word = words[scored_words.index(max_value)]

print(max_word, max_value)
