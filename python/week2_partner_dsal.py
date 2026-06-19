import array as arr

A = arr.array("i", [16, 7, 2, -9, 5])
B = arr.array("i", [6, 14, 8, 1, 18])
C = arr.array("i", [5, 2, 15, 13, 60])
D = arr.array("i", [-6, -8, 4, 2, -5])
# Given the program snippet, display the values of the array variables after all the operations.
A[0] = B[2] * 2
B[1] = C[3] * D[3] + 2
D[0] = (B[4] - C[3]) * 3
C[2] = A[0] - C[1] + D[1]
if D[2] < C[4]:
    C[4] = True
else:
    C[4] = D[2] * C[2]
A[3] = (D[0] * C[0] + 2) // 2
D[1] = B[4] + D[2] - A[0]
C[3] = C[2] - C[3] + D[2]
#print(f"(({B[1]} + {C[4]}) * 2) - (({B[4]} * ({C[1] + D[1]})) - 6)")
#print(((B[1] + C[4]) * 2) - ((B[4] * (C[1] + D[1])) - 6))
B[4] = ((B[1] + C[4]) * 2) - ((B[4] * (C[1] + D[1])) - 6)
print(f"{A[3]} + ({C[0]} + ({D[3]} // 3*2 + {C[1]}))")
print(A[3] + (C[0] + (D[3]//3*2 + C[1])))
D[4] = A[3] + (C[0] + (D[3]//3*2 + C[1]))
if A[1] > B[0]:
    A[1] = A[1] + C[0]
else: 
    B[0] = B[0] * 2
if C[3] < D[3]:
    D[3] = True
else: 
    D[3] = C[2] - A[2]
if B[2] == D[2]:
    B[2] = True
else: 
    B[2] = B[2] + D[2]
if C[4] > A[4]:
    C[4] = C[4] // 2
if D[0] < 0:
    D[0] = abs(D[0])
if A[3] < C[3]:
    A[3] = A[3] + D[1]
if B[4] > 100:
    B[4] = B[4] - 50
if C[1] == D[1]:
    C[1] = True
else: 
    C[1] = D[1] + A[1]
print()
print(A[2])
print(B[2])
if A[2] <= B[2]:
    A[2] = A[2] * B[2]
if D[4] < 0:
    D[4] = D[4] + 10

print(A)
print(B)
print(C)
print(D)