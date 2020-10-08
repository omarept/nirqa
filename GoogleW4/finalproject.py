import wordcloud



text = "esto es una prueba de contar! palabras, por ejemplo, podriamos poner un texto importante que haga esto. veamos que pasa mas adelante, pero esto"


def word_no_punct(word):
    new_word = ""
    for letter in word:
        if letter.isalpha():
            new_word += letter
    return new_word


def txt_normalized(text):
    new_text = []
    txt_split = text.split()
    for word in txt_split:
        new_word = word_no_punct(word)
        new_text.append(new_word)
    return new_text


def frequency(txt_normalized):
    dyct = {}
    words_no_relevant = ["es", "de"]
    for word in txt_normalized:
        if word not in words_no_relevant:
            if word not in dyct:
                dyct[word] = 1
            else:
                dyct[word] += 1
    return dyct




new_text = txt_normalized(text)
dyct = frequency(new_text)

print(dyct)




cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(dyct)
cloud.to_file("myfile.jpg")