def frequency(txt):
    dyct = {}
    txt_new = ""
    special_character = [" ","!"]
    for letter in txt:
        if letter not in special_character:
            txt_new += letter



    for letter in txt_new:
        if letter not in dyct:
            dyct[letter] = 1
        else:
            dyct[letter] += 1
    return dyct

print(frequency("esto! es una prueba"))
