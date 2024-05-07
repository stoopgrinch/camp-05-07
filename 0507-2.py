S = "m" + input()
x = 0

T = "drmfslc"
B = []

for i in range(len(S)):
    A = (int(T.find(S[i])))
    B.append(A)

for i in range(len(S) - 1):
    x += (abs(B[i+1] - B[i]) + 1)

print(x)
