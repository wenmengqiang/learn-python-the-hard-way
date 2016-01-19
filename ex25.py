#encoding:utf-8
def break_words(stuff):
    """This function will break words for us."""
    words=stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)
    
def print_first_word(words):
    """Print first word:"""
    word=words.pop(0)
    print word#这行函数是为了print_first_and_last()和print_first_and_last_sorted()能正常输出
    return word#是我自己搞错了，马虎啊，例子本来就是print word。
    
def print_last_word(words):
    """Print last word:"""
    word=words.pop(-1)
    print word
    return word
    
def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words."""
    words=break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence): #print该函数，提示为None。由于print_first_word()没有print函数，导致该函数在cmd没有输出
    """Prints the first and last words of the sentence."""
    words=break_words(sentence)
    #word=words.pop(0)
    #return word
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)