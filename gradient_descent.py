points = [(2, 4), (4, 2)]

def F(w):
    return sum((w * x - y)**2 for x, y in points)

def dF(w):
    return sum(2 * (w * x - y) * x for x, y in points)


# Gradient descent
w = 0
for t in range(100):
    gradient = dF(w)
    w = w - 0.01 * gradient
    print(f"iteration {t}: w = {w}, F(w) = {F(w)}")
