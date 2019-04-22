def disemvowel(word):
    l = []
    for letter in word:
        c = letter.upper()
        if c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
            continue
        else:
            l.append(letter)
    s = "".join(l)
    return s
