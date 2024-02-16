import numpy as np

true_w = np.array([12, 156, 1058, 9191, 1245])
d = len(true_w)
points = []

for i in range(50_000):
    x = np.random.random(d)
    y = true_w.dot(x) + np.random.randn()
    points.append((x, y))

def sF(w, i):
    x, y = points[i]
    return (w.dot(x) - y)**2

def sdF(w, i):
    x, y = points[i]
    return 2 * (w.dot(x) - y) * x


# Gradient descent
w = np.zeros(d)
for t in range(100):
    for numUpdates, i in enumerate(range(len(points))):
        value = sF(w, i)
        gradient = sdF(w, i)
        eta = 1 / (numUpdates + 1)
        w = w - eta * gradient
    print(f"iteration {t}: w = {w}, F(w) = {value}")
