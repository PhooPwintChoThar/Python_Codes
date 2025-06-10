def find_word_position(word, list_of_words):
    if len(list_of_words)==0:
        return []
    
    room=[]
    for x in range(len(list_of_words)):
        if list_of_words[x].lower()==word.lower():
            room.append(x)

    if len(room)==0:
        return 0
    return room

print(find_word_position("Python", ["python", "java", "c", "PYTHON", "prolog"]))
print(find_word_position("iOS", ["Window", "macOs", "Linux"]))