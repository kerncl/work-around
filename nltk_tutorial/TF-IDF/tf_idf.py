from sklearn.feature_extraction.text import TfidfVectorizer

sentences = ['This is the first document',
             'This is the second document']

# Create an object
vectorizier = TfidfVectorizer(norm=None)

# Generating output for IF_IDF
X = vectorizier.fit_transform(sentences).toarray()


# Total words with their index in model:
print(vectorizier.vocabulary_)
print('\n')

# Features:
print(vectorizier.get_feature_names())
print('\n')

# Show the output:
print(X)