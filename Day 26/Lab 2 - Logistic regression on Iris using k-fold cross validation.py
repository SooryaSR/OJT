# Import necessary library
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, KFold

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Initialize logistic regression model
log_reg = LogisticRegression(max_iter=1000)  # Increase max_iter for convergence

# Define k-fold cross-validation
k_fold = KFold(n_splits=5, shuffle=True, random_state=42)  # 5-fold CV, shuffling data

# Perform cross-validation
scores = cross_val_score(log_reg, X, y, cv=k_fold)
# Print the accuracy for each fold
print("Accuracy for each fold:", scores)

# Print the mean accuracy and standard deviation
print("Mean Accuracy:", scores.mean())
print("Standard Deviation:", scores.std())

# Define scoring metrics
scoring = {'accuracy': 'accuracy',
           'precision': 'precision_macro',
           'recall': 'recall_macro',
           'f1': 'f1_macro'}

# Perform cross-validation for each metric
for metric, score_func in scoring.items():
    scores = cross_val_score(log_reg, X, y, cv=k_fold, scoring=score_func)
    print(f"{metric.capitalize()} for each fold:", scores)
    print(f"Mean {metric.capitalize()}: {scores.mean()}")
    print(f"Standard Deviation: {scores.std()}")
    print()