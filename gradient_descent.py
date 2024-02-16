import numpy as np

true_w = np.array([12, 156, 1058, 9191, 1245])
d = len(true_w)
points = []

for i in range(50_000):
    x = np.random.random(d)
    y = true_w.dot(x) + np.random.randn()
    points.append((x, y))

def F(w):
    return sum((w.dot(x) - y)**2 for x, y in points) / len(points)

def dF(w):
    return sum(2 * (w.dot(x) - y) * x for x, y in points) / len(points)


# Gradient descent
w = np.zeros(d)
for t in range(10000):
    gradient = dF(w)
    w = w - 0.1 * gradient
    print(f"iteration {t}: w = {w}, F(w) = {F(w)}")
