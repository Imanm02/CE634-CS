import numpy as np

def r(y):
    return np.exp(-y**2 / 2) / np.sqrt(2 * np.pi)

def s(y):
    return 2 * r(y) if y >= 0 else 0

c = 1

accepted = False
while not accepted:
    Y = np.random.normal()

    U = np.random.uniform()

    if U <= s(Y) / (c * r(Y)):
        accepted = True

Y_accepted = Y
print(Y_accepted) # 1.575943198091014

