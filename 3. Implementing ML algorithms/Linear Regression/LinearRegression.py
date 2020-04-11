#import tensorflow
import sklearn
import numpy as np
import matplotlib as mp
import pandas as pd
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle

# read data
data = pd.read_csv("student-mat.csv", sep=";")

# Breaking data into useful and unuseful components
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
# print(data.head()) #Displaying first few data

# Preparing the data
predict = "G3"
X = np.array(data.drop([predict], 1)) # Features or training data
y = np.array(data[predict]) # Labels or output

# Seperating data to train and test
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)
# The test_size=0.1 divide the data in 90:10 ratio i.e 90% to train and 10% to test

# Running the ML model on the training data and checking its accuracy using test data
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc=linear.score(x_test,y_test)
print(acc)

# Checking the coefficients for the line eqn of 5-D space
print('Coeff: \n', linear.coef_) # Coeff for five differernt constants
print('Intercept: \n', linear.intercept_)

# Let's make a comparison of our model data and data that we have predicted
predictions=linear.predict(x_test)
for x in range(len(predictions)):
    print(x,': ',predictions[x], x_test[x], y_test[x])

# Let's save our best suited model using pickle and plot data to check comparison
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

with open("studentmodel.pickle",mode="wb") as f:
    pickle.dump(linear, f)

# Read pickle model to check our model
pickle_in = open("studentmodel.pickle","rb")
linear=pickle.load(pickle_in)

#plot the data
p='G1' # Vary the p tag to plot data for other types.
style.use("ggplot")
pyplot.scatter(data[p],data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("-Final Grade-")
pyplot.show()
