from nltk import word_tokenize
import nltk

sentence = 'Mr. Ali made a deal on a beach of Switzerland near WHO'
tokenized_words = word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokenized_words)
# print(tagged_words)
NER = nltk.ne_chunk(tagged_words, binary=False)
print(NER)
NER.draw()