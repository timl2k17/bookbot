def word_count(text):
    return len(text.split())

def character_stats(text):
    char_dict = {}
    
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sorted_character_stats(character_dict):
    character_list =[]
    for char in character_dict:
        character_list.append({
            'character': char,
            'count': character_dict[char]
        })
    character_list.sort(reverse=True, key=sort_on)
    return character_list