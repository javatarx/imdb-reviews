import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

df = pd.read_csv('cristian.csv', index_col=0)
#df.info()
#df.head()
#df.count()
print ("------------- Rating promedio (" , (df["rating"].mean()) , ")-------------")
filtered_reviews = []
tokened_reviews = []
reviews = []
for review in df["title"]:
  reviews.append(review.rstrip().lower())
  stop_words = set(stopwords.words('english'))

for review in reviews:
    word_tokens = word_tokenize(review)
    tokened_reviews.append(word_tokens)
    filtered_review = [w for w in word_tokens if not w in stop_words]
    filtered_review = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_review.append(w)
    filtered_reviews.append(filtered_review)
# print ("\n------------- Reviews -------------")
# for review in reviews:
#   print (review)
sum_tokened_reviews = 0
sum_filtered_reviews = 0

print ("\n------------- Tokened Reviews -------------")
for tokened_review in tokened_reviews:
  print (tokened_review)
  sum_tokened_reviews = sum_tokened_reviews + len(tokened_review)

print ("\n------------- Filtered Reviews -------------")
for filtered_review in filtered_reviews:
  print (filtered_review)
  sum_filtered_reviews = sum_filtered_reviews + len(filtered_review)

print ("\n------------- Cantidad promedio de palabras por comentario: -------------")
print (sum_tokened_reviews/len(tokened_reviews))

print ("\n------------- Cantidad promedio de palabras filtradas por comentario: -------------")
print (sum_filtered_reviews/len(filtered_reviews))

#reviews[:10]
#filtered_reviews[:10]