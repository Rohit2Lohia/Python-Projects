
# coding: utf-8

# In[13]:


import sklearn
from sklearn import datasets
from sklearn import svm,metrics
from sklearn.neighbors import KNeighborsClassifier #I have imported this to make kind of a comperison between the two  


# In[12]:


# Loading the data (This time we will be working with datasets provided by sklearn by default)
cancer = datasets.load_breast_cancer()
# print(cancer)
print(cancer.feature_names,"\n")
print(cancer.target_names)


# In[23]:


X=cancer.data
y=cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)


# In[11]:


print("Features: ", x_train[:5],"\nLabels: ",y_train[:5])
classes = ['malignant', 'benign'] 


# In[19]:


clf = svm.SVC()
clf.fit(x_train,y_train)


# In[21]:


y_pred = clf.predict(x_test) # Predic for the test data
acc = metrics.accuracy_score(y_test, y_pred) # Check for the accuracy
print (acc)


# In[25]:


# As we can see that our accuracy is preety low so according to the theory of 
# SVM we must use Kernel to make the model more accurate
clf2 = svm.SVC(kernel="linear", C=2) # Here C is the soft margin so by varying this accuracy may vary
clf2.fit(x_train,y_train)
y_pred2 = clf2.predict(x_test)
acc2 = metrics.accuracy_score(y_test, y_pred2)
print (acc2)


# In[26]:


# Now let's make a comparison of this model with KNN
clf3 = KNeighborsClassifier(n_neighbors=11) # Here C is the soft margin so by varying this accuracy may vary
clf3.fit(x_train,y_train)
y_pred3 = clf3.predict(x_test)
acc3 = metrics.accuracy_score(y_test, y_pred3)
print (acc3)


# In[28]:


# Store all our three models
import pickle
with open("cancer_model.pickle", mode="wb") as f:
    pickle.dump([clf,clf2,clf3],f)

