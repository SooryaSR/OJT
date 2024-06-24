from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    'RandomForest': RandomForestClassifier(),
    'SVM': SVC(),
    'KNN': KNeighborsClassifier()
}

# Define hyperparameters to tune for each model
params = {
    'RandomForest': {'n_estimators': [50, 100, 200], 'max_depth': [None, 5, 10]},
    'SVM': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']},
    'KNN': {'n_neighbors': [3, 5, 7], 'weights': ['uniform', 'distance']}
}

best_model = None
best_accuracy = 0
# Hyperparameter tuning using GridSearchCV
for name, model in models.items():
    grid_search = GridSearchCV(estimator=model, param_grid=params[name], cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    accuracy = grid_search.best_score_
    print(f"{name}: Best Accuracy - {accuracy}, Best Parameters - {grid_search.best_params_}")
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = grid_search.best_estimator_

print(f"The best model is: {best_model}")
print(f"Best accuracy is: {best_accuracy}")

# Evaluate the best model on the test set
y_pred = best_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy of Best Model:", test_accuracy)


