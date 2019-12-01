import sys
sys.path.append("../ElGamal")
from math import sqrt
from utils import expMod

# https://www.geeksforgeeks.org/discrete-logarithm-find-integer-k-ak-congruent-modulo-b/
def discreteLogarithm(a, b, m):
    n = int(sqrt(m) + 1)

    value = [0] * m

    # Store all values of a^(n*i) of LHS
    for i in range(n, 0, -1):
        value[expMod(a, i * n, m)] = i

    for j in range(n):

        # Calculate (a ^ j) * b and check
        # for collision
        cur = (expMod(a, j, m) * b) % m

        # If collision occurs i.e., LHS = RHS
        if (value[cur]):
            ans = value[cur] * n - j

            # Check whether ans lies below m or not
            if (ans < m):
                return ans

    return -1
