def sillycase(s):
    half = len(s)//2
    s_1 = s[:half].lower()
    s_2 = s[half:].upper()
    return s_1 + s_2
