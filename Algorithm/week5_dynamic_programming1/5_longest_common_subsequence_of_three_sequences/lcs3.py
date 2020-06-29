#Uses python3

import sys
input = sys.stdin.read()
data = list(map(int, input.split()))
an = data[0]
data = data[1:]
X = data[:an]
data = data[an:]
bn = data[0]
data = data[1:]
Y = data[:bn]
data = data[bn:]
cn = data[0]
data = data[1:]
Z = data[:cn]
m = len(X) - 1
n = len(Y) - 1
o = len(Z) - 1
l = max(m +1, n + 1, o + 1)
dp = [[[-1 for i in range(l)]
           for j in range(l)]
          for k in range(l)]
def lcs3(i, j, k):
    if (i == -1 or j == -1 or k == -1):
        return 0

    if (dp[i][j][k] != -1):
        return dp[i][j][k]

    if (X[i] == Y[j] and Y[j] == Z[k]):
        dp[i][j][k] = 1 + lcs3(i - 1,
                                 j - 1, k - 1)
        return dp[i][j][k]

    else:
        dp[i][j][k] = max(max(lcs3(i - 1, j, k),
                              lcs3(i, j - 1, k)),
                          lcs3(i, j, k - 1))

        return dp[i][j][k]

print(lcs3(m, n, o))






