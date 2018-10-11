import numpy as np

class pocket:
    def fit(self, X, y, learning_rate, epochs):
        data_number, feature_number = X.shape

        self.__W = np.zeros((feature_number, 1))
        self.__b = 0

        accuracy = 0
        for _ in range(epochs):
            y_pred = np.sign(X.dot(self.__W) + self.__b)
            index = np.random.choice(np.where(y != y_pred)[0])

            W_tmp = self.__W + learning_rate * y[index] * X[index].reshape(self.__W.shape)
            b_tmp = self.__b + learning_rate * y[index]

            y_pred = np.sign(X.dot(W_tmp) + b_tmp)
            accuracy_tmp = np.mean(y == y_pred)
            if accuracy_tmp > accuracy:
                accuracy = accuracy_tmp
                self.__W = W_tmp
                self.__b = b_tmp

    def predict(self, X):
        return np.sign(X.dot(self.__W) + self.__b)