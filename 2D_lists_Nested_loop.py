number_grid= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0])    #sloupec 0 radek 0 , column= sloupec, row= radek
for row in number_grid:             #pro radek ve funkci vem vse z radku a vytiskni
    for col in row:                 #for loop in for loop, da nam to konkretni cisla, da nam to samostatnou hodnotu
        print(col)