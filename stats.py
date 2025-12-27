def get_num_words(text):
    words = len(text.split())
    print(f"Found {words} total words")

def get_num_characters(text):
    text = text.lower()
    text_dict = dict()
    list_text_dict = []

    for i in text:
        text_dict[i] = text_dict.get(i, 0) + 1
    
    for char, count in text_dict.items():
        list_text_dict.append({"char" : char, "num": count})
    
    return list_text_dict

def sort_on(list_text_dict):
    return list_text_dict["num"]

def sort_characters(list_text_dict):
   list_text_dict.sort(reverse=True, key=sort_on)
   return list_text_dict