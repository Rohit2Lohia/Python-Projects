# coding: utf-8
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
print(data.head(n=30))

# As our data is not numeric but it can be seen from the data that this non-numeric data can be assigned with some respectively
# constants that corrosponds to some weight. So, to do that sk can help us with that
# modifying persons data i.e 'more' converted to 3, 2->1, 4->2
for d in range(len(data)):
    if(data["persons"][d]=='more'):
        data["persons"][d]='3'
    elif(data["persons"][d]=='2'):
        data["persons"][d]='1'
    elif(data["persons"][d]=='4'):
        data["persons"][d]='2'
    else:
        data["persons"][d]='0'

le= preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
persons = list(data["persons"])
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))
# print(buying)

predict = "class"
X=list(zip(buying,maint,door, persons, lug_boot, safety))
y=list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.1)

#print(x_train,y_test)
# Preparing model
model = KNeighborsClassifier(n_neighbors=8)
# Normally we should take the value of n_neighbors to be odd (preferbly Prime) as it doesn't create a equal voting conditions

model.fit(x_train, y_train)
acc= model.score(x_test,y_test)
print(acc)

# Saving the model with highest accuracy
import pickle
with open("cardekho.pickle",mode="wb") as f:
    pickle.dump(model, f)

predicted = model.predict(x_test)
names= ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    # Now we will we see the neighbors of each point in our testing data
    n = model.kneighbors([x_test[x]], 8, True)
    # 'n' will return a 2*8 matix in which
    # First row give us the distance of each node its 8 nearest neighbors
    # Second row give us the column no. of respective nearest neighbors
    print("N: ", n)
