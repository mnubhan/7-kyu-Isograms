def is_isogram(string):
    return len(string) == len(set(string.lower()))

def is_isogram(string):
    repeated_char = 0
    for i in string:
        repeated_char += 1 if string.lower().count(i) > 1 else 0
    return True if repeated_char < 1 else False
