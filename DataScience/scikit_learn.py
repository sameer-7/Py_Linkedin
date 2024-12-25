# Scikit-Learn is a machine learning library that provides simple and efficient tools for data mining and data analysis. It offers a variety of algorithms for classification, regression, clustering, and more.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Load the iris dataset
iris = load_iris()
x = iris.data
y=iris.target

#split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#train a random forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

#make prediction
y_pred = clf.predict(X_test)

#calculate accuracy
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy : ",accuracy)