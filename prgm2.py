import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x = pd.read_csv('Salary_Data.csv')
a = x.iloc[:, :-1].values
b = x.iloc[:, 1].values

a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.3, random_state=42)
m = LinearRegression()
m.fit(a_train, b_train)
c = m.predict(a_test)

# plotting training data
plt.scatter(a_train, b_train, color='red')
plt.plot(a_train, b_train, m.predict(a_test), color='blue')

# plotting testing data
plt.scatter(a_test, b_test, color='red')
plt.plot(a_train, b_train, m.predict(a_test), color='blue')

plt.title('salary based on year of Experience')
plt.xlabel('Years Experience')
plt.ylabel('salary')
plt.show()
