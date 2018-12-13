from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Betty', 'Barny', 'Wilma', 'Fred', 'Sonic', 'Alphabet', 'Fortune', 'Fortnight', 'Assume', 'Exhausted']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    if len(list_of_words) == 0:
        raise IndexError()
    return random.choice(list_of_words)

def _mask_word(word):
    if not word:
        raise InvalidWordException()
    result = ''
    for letter in word:
        result += '*'
    return result

#Given a word like 'Python', it returns it "masked" (replacing real characters with asterisks): '******'


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word or len(answer_word) == 0 or len(masked_word) == 0 or (len(masked_word) != len(answer_word)    ) :
        raise InvalidWordException()
    if len(character) > 1 or not character:
        raise InvalidGuessedLetterException()
        
    pass


def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
