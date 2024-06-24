import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score

# 1. Load the dataset 
df = pd.read_csv('data1.csv')
print(df.head())

#2. Summary statistics
summary = df.describe()
print(summary)

# Mean and SD of Sepal Length
mean_sepal_len = df['Sepal Length (cm)'].mean()
std_sepal_len = df['Sepal Length (cm)'].std()
print(f"Mean Sepal Length: {mean_sepal_len}")
print(f"Standard Deviation of Sepal Length: {std_sepal_len}")

#3. Missing value
missing_values = df.isnull().sum()
print("Missing values:")
print(missing_values)

#4. Converting species to numberical val
species_map = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC': 2}
df['Species'] = df['Species'].map(species_map)
print(df.head())

X = df.drop('Species', axis=1)
y = df['Species']

# 5. Split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
print(f"Shape of X_train: {X_train.shape}, Shape of X_test: {X_test.shape}")

#6.  TrAIN DECISION TREE CLASSIFIER

dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)

#7. VISUALIZE

plt.figure(figsize=(12, 8))
plot_tree(dt_classifier, filled=True, feature_names=X.columns, class_names=list(species_map.keys()))
plt.show()

#8. Commpute accuracy

y_pred = dt_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the decision tree classifier: {accuracy}")