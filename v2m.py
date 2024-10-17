#-*- coding:utf-8 -*-

import requests
import json
import os
import time
 
url = 'http://127.0.0.1:8080/inference'
 
files = {
    'file': open('/home/nvidia/wav/goforward1.wav', 'rb'),
    'response-format': (None, 'json'),
}
 
response = requests.post(url, files=files)
result = json.loads(response.text)["text"]

print(result)

smdstr = result[0:4]
print(smdstr)

text1 = smdstr
text2 = "앞으로"

import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Convert the texts into TF-IDF vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([text1, text2])

# Calculate the cosine similarity between the vectors
similarity = cosine_similarity(vectors)
print(similarity)


import fasttext

# Load the FastText model
model = fasttext.load_model('cc.en.300.bin')

# Preprocess the text
text1 = 'This is a piece of text'
text2 = 'This is another piece of text'
tokens1 = fasttext.tokenize(text1)
tokens2 = fasttext.tokenize(text2)
tokens1 = [token.lower() for token in tokens1]
tokens2 = [token.lower() for token in tokens2]

# Generate word vectors for each piece of text
vector1 = model.get_sentence_vector(tokens1)
vector2 = model.get_sentence_vector(tokens2)

# Calculate the similarity between the vectors using cosine similarity
from scipy.spatial.distance import cosine
similarity = 1 - cosine(vector1, vector2)
print('Similarity:', similarity)

simarr = [[1.,1.],[1.,1.]]
if(set(similarity) == set(simarr)):
    print("same arr")

res = text_similarity(smdstr, "앞으로")
print(res)

if(smdstr == "앞으로"):
    print("go")
    os.system('cansend can0 001#56.00.00.00.56.00.00.00')
    time.sleep(3)
    os.system('cansend can0 001#64.00.00.01.64.00.00.01')
    time.sleep(3)
else:
    print("don't")


