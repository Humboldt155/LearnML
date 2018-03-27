
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_breast_cancer
canser = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(canser['data'], canser['target'], random_state=0)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=3)

clf.fit(X_train, y_train)
