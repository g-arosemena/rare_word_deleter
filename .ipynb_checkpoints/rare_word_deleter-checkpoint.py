from numba import jit


@jit
def RareWordDeleter(document, wordlist):
    words = [x.lower() for x in wordlist]
    string_list = document.split(" ")
    string_list = [x.lower() for x in string_list]
    sl_set = set(string_list)
    words_set = set(words)
    inter = sl_set.intersection(words_set)
    res = [x.lower() for x in string_list if x.lower() in inter]
    res = " ".join(res)
    return res
