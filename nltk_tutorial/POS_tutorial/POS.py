from nltk import pos_tag, word_tokenize
import nltk

tag = pos_tag(['Studying', 'Study'])
print(tag)

sentences = 'A very beautiful young lady is walking on the beach'
words = word_tokenize(sentences)
tagged_words = pos_tag(words)
print(tagged_words)


grammer = "NP : {<DT>?<JJ>*<NN>} "
parser = nltk.RegexpParser(grammer)
output = parser.parse(tagged_words)
print(output)
output.draw()

grammer2 = r""" NP : {<.*>+}
                }<JJ>+{"""
parser2 = nltk.RegexpParser(grammer2)
output2 = parser2.parse((tagged_words))
print(output2)
output2.draw()
