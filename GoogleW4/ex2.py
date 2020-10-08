def frequency(txt):
    dyct = {}
    special_character = [" ","!", '$', '#', '@']
    for letter in txt:
        if letter not in special_character:
            if letter.lower() not in dyct:
                dyct[letter.lower()]=1
            else:
                dyct[letter.lower()] += 1
    return dyct
            

print(frequency("esto! Es una prueba@ #"))