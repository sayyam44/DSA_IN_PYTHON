# https://www.geeksforgeeks.org/find-the-first-repeated-character-in-a-string/

def find_repeated(str):
    h={}
    for ch in str:
        if ch in h:
            return ch
        else:
            h[ch]=0
    return -1