from sklearn.feature_extraction.text import CountVectorizer

sentences = ['Jim and Pam travelled by the bus:',
             'The train was late',
             'The flight was full. Travelling by flight is expensive' ]

# Create an object:
cv = CountVectorizer()

# Generating output for bag of words:
BOW = cv.fit_transform(sentences).toarray()

# Total worrds with their index in model:
print(cv.vocabulary_)
print('\n')

# Features:
print(cv.get_feature_names())
print('\n')

# Show the output
print(BOW)