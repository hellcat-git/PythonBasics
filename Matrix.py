m = [[5, 10], [7, 12], [11.3, 5], [25, 30]]
m1 = []
m2 = []
res = []

for i in m:
    m1.append([el * 7 for el in i])
    m2.append([el * 2 for el in i])
print(m2)

for i in range(0, 4):
    loc = []
    for y in range(0, 2):
        loc.append(m1[i][y]+m2[i][y])
    res.append(loc)

print(res)