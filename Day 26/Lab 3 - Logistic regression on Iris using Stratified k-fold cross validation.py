# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Initialize logistic regression model
log_reg = LogisticRegression(max_iter=1000)  # Increase max_iter for convergence

# Define stratified k-fold cross-validation
stratified_k_fold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)  # 5-fold CV, stratified

# Perform cross-validation
scores = cross_val_score(log_reg, X, y, cv=stratified_k_fold)

# Print the accuracy for each fold
print("Accuracy for each fold:", scores)

# Print the mean accuracy and standard deviation
print("Mean Accuracy:", scores.mean())
print("Standard Deviation:", scores.std())