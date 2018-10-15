import numpy as np

class optimizer:
    def __init__(self, learning_rate=0):
        self.learning_rate = learning_rate

    def optimize(self, g_w, g_b):
        pass

class gradient_descent(optimizer):
    def __init__(self, learning_rate):
        super().__init__(learning_rate)

    def optimize(self, g_w, g_b):
        return self.learning_rate * g_w, self.learning_rate * g_b

class adam(optimizer):
    def __init__(self, learning_rate):
        super().__init__(learning_rate)

        self.__t = 0
        self.__alpha = 0.9
        self.__alpha2 = 0.999

        self.__s_w = 0
        self.__s_b = 0

        self.__first_run = True

    def optimize(self, g_w, g_b):
        if self.__first_run:
            self.__first_run = False
            self.__r_w = np.zeros_like(g_w)
            self.__r_b = np.zeros_like(g_b)

        self.__t += 1

        self.__s_w = self.__alpha * self.__s_w + (1 - self.__alpha) * g_w
        s_hat_w = self.__s_w / (1 - self.__alpha ** self.__t)
        self.__r_w = self.__alpha2 * self.__r_w + (1 - self.__alpha2) * np.power(g_w, 2)
        r_hat_w = self.__r_w / (1 - self.__alpha2 ** self.__t)
        v_w = s_hat_w / (1e-8 + np.sqrt(r_hat_w))

        self.__s_b = self.__alpha * self.__s_b + (1 - self.__alpha) * g_b
        s_hat_b = self.__s_b / (1 - self.__alpha ** self.__t)
        self.__r_b = self.__alpha2 * self.__r_b + (1 - self.__alpha2) * np.power(g_b, 2)
        r_hat_b = self.__r_b / (1 - self.__alpha2 ** self.__t)
        v_b = s_hat_b / (1e-8 + np.sqrt(r_hat_b))

        return self.learning_rate * v_w, self.learning_rate * v_b