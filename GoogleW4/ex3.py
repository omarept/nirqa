def frequency(txt):
    dyct = {}
    for letter in txt:
        if letter.isalpha():
            if letter.lower() not in dyct:
                dyct[letter.lower()]=1
            else:
                dyct[letter.lower()] += 1
    return dyct
            

print(frequency("esto! Es una prueba@ #234T"))