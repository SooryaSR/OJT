import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV

#load data
data = pd.read_csv('data.csv')
#feature used in case
x = data[['loan_amount','interest_rate','term','income','credit_score','age','employment_length']]
y = data[['loan_repaid']]
#split to train test
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
#initiate model
model = DecisionTreeClassifier(random_state=42)
#train model
model.fit(x_train,y_train)
#predict
y_pred = model.predict(x_test)
#evaluate
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy:, {accuracy:.2f}")
print(classification_report)
print(classification_report(y_test,y_pred))
# print("confusion Metrix:")
# print(confussion_matrix(y_test,y_pred))