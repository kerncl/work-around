from nltk.stem import PorterStemmer, WordNetLemmatizer


def print_porter(word_list):
    for word in word_list: print(porter.stem(word))
    print('\n')


def print_lemma(word_list, **kwargs):
    for word in word_list: print(lemma.lemmatize(word, **kwargs))
    print('\n')

word_list = ['study', 'studying', 'studies', 'studied']
word_list2 = ['study', 'leaves', 'decreases', 'plays']
word_list3 = ['am', 'is', 'are', 'was', 'were']

### Porterstemmer ###
porter = PorterStemmer()
print('Example for PorterStemmer')
print_porter(word_list)
print_porter(word_list2)
print_porter(word_list3)

### WordNetLemmatizer
lemma = WordNetLemmatizer()
# Part of speech
# 1. verb --> v
# 2. noun --> n
# 3. adjective --> a
# 4. adverb --> r
print('Example for Wordnet')
print_lemma(word_list, pos='v')
print_lemma(word_list2)     #default noun (n)
print_lemma(word_list3, pos='v')
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('studying', pos='v'))
print(lemmatizer.lemmatize('studying', pos='n'))
print(lemmatizer.lemmatize('studying', pos='a'))
print(lemmatizer.lemmatize('studying', pos='r'))

