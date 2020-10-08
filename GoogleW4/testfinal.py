def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    dyct = {}
    file_split = file_contents.split()
    new_file = []
    
    for word in file_split:
        new_word = ""
        for letter in word:
            if letter not in punctuations:
                new_word += letter
        new_file.append(new_word)
    
    for word in new_file:
        if word not in uninteresting_words:
            if word.lower() not in dyct:
                dyct[word.lower()] = 1
            else:
                dyct[word.lower()] += 1
  
    return dyct

with open("63331-0.txt") as f:
        file_contents = f.read()
       

a = calculate_frequencies(file_contents)
print(a)
