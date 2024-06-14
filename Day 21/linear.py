import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#data
#dataset
height = np.array([150,160,164,165,173]).reshape(-1,1)
weight = np.array([50,65,63,68,72])
#create an linear regression model for the above data set
model = LinearRegression()
#lets fit the model with appropriate model
model.fit(height,weight)
predicted_weight = model.predict(height)
print(f"intercept: {model.intercept_}")
print(f"coefficients:{model.coef_[0]}")

plt.scatter(height,weight,color='green')
plt.plot(height,predicted_weight,color='pink')
plt.xlabel('height')
plt.ylabel('weight')
plt.title("Linear Regresison")
plt.show()