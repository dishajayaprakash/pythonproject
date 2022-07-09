# 4x4 Matrix multiplication

A = ([0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0])

B = ([0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0])

C = ([0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0])


print('Enter A matrix contents')
for i in range(0,4):
    for j in range(0,4):
        A[i][j] = int(input())
        
print('Enter B matrix contents')
for i in range(0,4):
    for j in range(0,4):
        B[i][j] = int(input())

for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            C[i][j] += A[i][j] * B[i][k]
print(C)