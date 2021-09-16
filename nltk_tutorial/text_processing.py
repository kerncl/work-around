from nltk import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_file = open('text.txt')
text = text_file.read()

### Data Cleaning ###
# Text --> Words
sentences = sent_tokenize(text)
print(f"No. of sentences: {len(sentences)}\n "
      f"list of sentences: \n {chr(10).join(sentences)}")
words = word_tokenize(text)
print(f'No. of words: {len(words)}')
fdist = FreqDist(words)
fdist.plot(10, title='Most common 10 words')

# Remove punc
words_no_punc = [w.lower() for w in words if w.isalpha()]
print(f'No. of words without punc: {len(words_no_punc)}')
fdist_no_punc = FreqDist(words_no_punc)
fdist_no_punc.plot(10, title='Most common 10 words without punc')

# Remove stopwords
stopword = stopwords.words('english')
# print(stopword)
clean_words = [word for word in words_no_punc if word not in stopword]
print(f'No. of words without stopword: {len(clean_words)}')
fdist_clean_words = FreqDist(clean_words)
fdist_clean_words.plot(10, title='Most common 10 words without stopwords')


