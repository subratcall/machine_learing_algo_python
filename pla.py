import numpy as np
import metrics

class Pla:
    def fit(self, X, y, learning_rate):
        data_number, feature_number = X.shape

        self.__W = np.zeros((feature_number, 1))
        self.__b = 0
        
        while True:
            for i in range(data_number):
                h = self.predict(X[i])
                if y[i] * h <= 0:
                    self.__W += learning_rate * y[i] * X[i].reshape(self.__W.shape)
                    self.__b += learning_rate * y[i]

            h = self.predict(X)
            if metrics.accuracy(y, h) == 1:
                break

    def predict(self, X):
        return np.sign(X.dot(self.__W) + self.__b)
