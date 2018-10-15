import numpy as np
import matplotlib.pyplot as plt
import metrics

class logistic_regression_gradient_descent:
    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def fit(self, X, y, epochs, optimizer, regularizer=None):
        data_number, feature_number = X.shape

        self.__W = np.zeros((feature_number, 1))
        self.__b = 0

        accuracy = []
        loss = []
        for _ in range(epochs):
            h = self.__sigmoid(X.dot(self.__W) + self.__b)

            g_w = X.T.dot(h - y) / data_number + (regularizer != None and regularizer.regularize(self.__W))
            g_b = np.mean(h - y)
            g_w, g_b = optimizer.optimize(g_w, g_b)
            self.__W -= g_w
            self.__b -= g_b

            y_hat = self.__sigmoid(X.dot(self.__W) + self.__b)
            loss.append(np.mean(-y * np.log(y_hat) - (1 - y) * np.log(1 - y_hat)))
            accuracy.append(metrics.accuracy(y, y_hat > 0.5))

        _, ax_loss = plt.subplots()
        ax_loss.plot(loss, 'b')
        ax_accuracy = ax_loss.twinx()
        ax_accuracy.plot(accuracy, 'r')
        plt.show()

    def predict(self, X):
        return self.probability(X) > 0.5

    def probability(self, X):
        return self.__sigmoid(X.dot(self.__W) + self.__b)

class logistic_regression_newton:
    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def fit(self, X, y, epochs):
        data_number, feature_number = X.shape

        self.__W = np.zeros((feature_number, 1))
        self.__b = 0

        accuracy = []
        loss = []
        for _ in range(epochs):
            h = self.__sigmoid(X.dot(self.__W) + self.__b)

            w_g = X.T.dot(h - y)
            A = np.diag((h * (1 - h)).flatten())
            w_H = X.T.dot(A).dot(X)
            self.__W -= np.linalg.pinv(w_H).dot(w_g)
            
            b_g = np.sum(h - y)
            b_H = np.sum(h * (1 - h))
            self.__b -= b_g / b_H
            
            y_hat = self.__sigmoid(X.dot(self.__W) + self.__b)
            loss.append(np.mean(-y * np.log(y_hat) - (1 - y) * np.log(1 - y_hat)))
            accuracy.append(metrics.accuracy(y, y_hat > 0.5))

        _, ax_loss = plt.subplots()
        ax_loss.plot(loss, 'b')
        ax_accuracy = ax_loss.twinx()
        ax_accuracy.plot(accuracy, 'r')
        plt.show()

    def predict(self, X):
        return self.probability(X) > 0.5

    def probability(self, X):
        return self.__sigmoid(X.dot(self.__W) + self.__b)