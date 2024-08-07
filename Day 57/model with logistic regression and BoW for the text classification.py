#create a model with logistic regression and bow for the text classification
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#creating sample data
reviews=[
    "I love the movie, it was good",
    "the movie was boring",
    "excellent movie, actord done well",
    "It was a normal movie"]
#positive label=1,negative label=0, neutral=2
labels=[1,0,1,2]

#create vectorization

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)
y=np.array(labels)
#split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
# create a logistic regression model
model = LogisticRegression()
#train the model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy= accuracy_score(y_test, y_pred)
print(f"Accuracy:{accuracy*100:.2f}%")
new_review =["i really enjoyed the movie"]