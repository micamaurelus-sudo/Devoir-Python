matrice = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matrice)):
    for j in range(i+1,len(matrice)):
        print("m[",i,"][",j,"]=",matrice[i][j])