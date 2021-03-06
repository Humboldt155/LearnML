import numpy as np


class Perceptron (object):

    """ Классификатор на основе персептрона.
    Параметры
    ---------
    eta : float
        Темп обучения (между 0.0 и 1.0)
    n_iter : int
        Проходы по тренировочному набору данных, количество эпох

    Атрибуты
    --------
    w_ : 1-мерный массив
        Весовые коэффициенты после подгонки.
        Равен количеству характеристик + 1 дополнительный bias unit (порог)
    errors_ : список
        Число случаев ошибочной классификации в каждой эпохе.

    """
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """ Выполнить подгонку модели под тренировочные данные.

        Параметры
        ---------
        X : {массивоподобный}, форма = [n_samples, n_features]
            тренировочные векторы, где
            n_samples - число образов и
            n_features - число признаков.
        y : массивоподобный, форма = [n_samples]

            Целевые значения.

        Возвращает
        ----------
        self : object

        """

        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += update != 0.0
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """ Рассчитать чистый вход """
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """ Вернуть метку класса после единичного скачка """
        return np.where(self.net_input(X) >= 0.0, 1, -1)


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
df = df[df.Age >= 0]

print(df.shape)

y = df.iloc[1:700, 1].values

y = np.where(y == 0, -1, 1)

X = df.iloc[1:700, [2, 5]].values

# plt.scatter(X[:400, 0], X[:400, 1],
#             color='red', marker='o', label='survived')
#
# plt.scatter(X[400:800, 0], X[400:800, 1],
#             color='blue', marker='x', label='not_survived')
#
# plt.xlabel('sex')
# plt.xlabel('class')
# plt.legend(loc='upper left')
# plt.show()

ppn = Perceptron(eta=0.1, n_iter=100)
X.astype(int)
y.astype(int)
ppn.fit(X,y)
plt.plot(range(1, len(ppn.errors_) + 1),
         ppn.errors_, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Number of updates')
plt.show()
