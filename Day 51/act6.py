
# Import necessary libarries
from gensim.models import FastText
from nltk.tokenize import word_tokenize
from nltk import download
# Download required NLTK data
download('punkt')


# Example sentences
sentences = [
    "Natural Language Processing is fun.",
    "Language models are improving every day."
]

# Tokenize sentences
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Train the FastText model
model = FastText(sentences=tokenized_sentences, vector_size=5, window=5, min_count=1, workers=4, sg=1)

# Get word vectors
word_vectors = model.wv
print("Word Vector for 'language':", word_vectors['language'])

# Get vector for an OOV word
print("Word Vector for 'NLPfun':", word_vectors['nlpfun'])
