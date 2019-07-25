r = int(input("Enter rows"))
c = int(input("enter columns"))
matrix = []
for i in range(r):
    d=[]
    for j in range(c):
        d.append(int(input()))
    matrix.append(d)

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = "")
    print()

r_start, c_start, r_end, c_end = 0,0,r,c
ret = 1
row = 0
for r in range(r_end):
    row = r
    for c in range(ret):
        if row >= 0:
            print(matrix[row][c])
            row -= 1

    ret += 1
