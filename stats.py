def number_of_words(book):
    words = book.split()
    return f"Found {len(words)} total words"

def char_count(text):
    characters = {}
    for c in text:
        if c.lower() in characters:
            characters[c.lower()] +=1 
        else:
            characters[c.lower()] = 1
    return characters

def sort_on(d):
    return d["num"]

def sort_dict(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char":c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
