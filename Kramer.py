from numpy import linalg

A = [[3, -2, 5], [7, 4, -8], [5, -3, -4]]
B = [7, 3, -12]
C = [[3, -2, 5], [7, 4, -8], [5, -3, -4]]
X = []
for i in range(0, len(B)):
    for j in range(0, len(B)):
        C[j][i] = B[j]
        if i > 0:
            C[j][i - 1] = A[j][i - 1]

    print(A, C)
    X.append(round(linalg.det(C) / linalg.det(A), 1))

print('w=%s' % X[0], 'x=%s' % X[1], 'y=%s' % X[2])

