def text_count(txt):
    words = txt.split()
    return len(words)

def char_count(txt):
    chars = txt.lower()
    count = {}
    for char in chars:
        if char in count:
            count[char] += 1
            
        else:
            count[char] = 1
    return count