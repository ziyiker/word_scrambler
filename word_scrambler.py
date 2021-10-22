from random import shuffle
from string import punctuation


def check_middle_only_one_unique_ch(middle_string):
    unique_ch = []
    for ch in middle_string:
        if ch not in unique_ch:
            unique_ch.append(ch)
    if len(unique_ch) == 1:
        return True
    return False
    
    
def isolate_punctuations(input_string):
    new_string = ""
    for ch in input_string:
        if ch not in punctuation:
            new_string += ch
        else:
            new_string += " " + ch
    return new_string


def scramble_word(word):
    if len(word) <= 3:
        return word   
    middle_ch = word[1:-1]
    if check_middle_only_one_unique_ch(middle_ch):
        return word
    else:
        middle_ch = list(middle_ch)
    continue_scramble = True
    while continue_scramble:
        shuffle(middle_ch)
        scrambled_word = word[0] + "".join(middle_ch) + word[-1]
        if scrambled_word != word:
            continue_scramble = False
    return scrambled_word


def scramble(input_string):
    scrambled_string = ""
    new_string = isolate_punctuations(input_string)
    word_list = new_string.split()
    scrambled_word_list = []
    
    for word in word_list:
        scrambled_word = scramble_word(word)
        scrambled_word_list.append(scrambled_word)
    
    for scrambled_words in scrambled_word_list:
        if not scrambled_string:
            scrambled_string += scrambled_words

        else:
            if scrambled_words[0] in punctuation:
                scrambled_string += scrambled_words
            else:
                scrambled_string += " " + scrambled_words
                
    return scrambled_string

