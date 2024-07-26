# Import necessary Libraries
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk import download
download("punkt")

# Example sentences
sentences = [
    "Natural Language Processing is fun.",
    "Language models are improving every day."
]

# Tokenize sentences
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]
tokenized_sentences

# Train the Word2Vec model
model = Word2Vec(sentences=tokenized_sentences, vector_size=5, window=5, min_count=1, workers=4, sg=0)
# Here sg=0 means the model will use Continuous bag of words architecture and if sg=1 then it will use Skip-gram Model

# Get word vectors
word_vectors = model.wv
print("Word Vector for 'language':", word_vectors['language'])
