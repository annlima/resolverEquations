import numpy as np
def newton(f, Df, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print("Found solution after n iterations")
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print("Zero derivate. No solution found")
            return None
        xn = xn - fxn / Dfxn
    print("Exceeded maximum iterations. No solution found")
    return None


        