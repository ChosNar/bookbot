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
def sort_on(item):
    return item["num"]
def sorter(count):
    lst = []
    for char, num in count.items():
        lst.append({"char": char, "num": num})
    lst.sort(reverse = True, key = sort_on)
    return lst