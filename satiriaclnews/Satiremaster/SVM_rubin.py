from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer 
from scipy.sparse.csr import csr_matrix
import numpy as np

text = ['I like NLP','dog shit is dog shit']
text1 = ['We like NLP']
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(text1)

tf = TfidfVectorizer()
tfidf = tf.fit_transform(text1) 
print (tfidf,type(tfidf))

feature_names = tf.get_feature_names()
doc = 0
feature_index = tfidf[doc,:].nonzero()[1]
tfidf_scores = zip(feature_index, [tfidf[doc, x] for x in feature_index])
for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
    print(w, s)