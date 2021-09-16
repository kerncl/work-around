from nltk.corpus import wordnet

# List of meaning
for words in wordnet.synsets('enjoy'):
    for lemma in words.lemmas():
        print(lemma)
    print('\n')

# Details of word
word = wordnet.synsets('play')[0]
print(word.name())
print(word.definition())
print(word.examples())
print(word.hypernyms())


# Synonyms
synonyms = []
for words in wordnet.synsets('play'):
    for word in words.lemmas():
        synonyms.append(lemma.name())
print(synonyms)


# similarity between words
word1 = wordnet.synsets('ship','n')[0]
word2 = wordnet.synsets('boat', 'n')[0]
print(word1.wup_similarity(word2))
