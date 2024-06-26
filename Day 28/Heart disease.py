#Do the prediction of heart attack from the above sample dataset with logistic regression methods and find the confusion Metrix, accuracy, precision, recall and f1score of the above
 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,f1_score

data=pd.read_csv("dataset.csv")
# print(data.head())
df=pd.DataFrame(data)

df['gender']=df['gender'].map({'male':0,'female':1})
df['smoking']=df['smoking'].map({'yes':1,'no':0})
df['diabetes']=df['diabetes'].map({'yes':1,'no':0})
df['exercise']=df['exercise'].map({'yes':1,'no':0})

x=df.drop('heart_attack',axis=1)
y=df['heart_attack']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=42)

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred= model.predict(x_test)

confus_matrix = confusion_matrix(y_test,y_pred)
print("confusion metrix",confus_matrix)

accuracy=accuracy_score(y_test,y_pred)
print("accuracy:",accuracy)

precision =precision_score(y_test,y_pred)
print("precision:",precision)

recall =recall_score(y_test,y_pred)
print("recall:",recall)

f1score=f1_score(y_test,y_pred)
print("f1score:",f1score)