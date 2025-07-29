macierz = [[0,2,5,1],[1,-2,0,9],[1,3,5,-4],[-1,2,0,4]]
macierz_dic = {(0,1):2,(0,2):5,(0,3):1,(1,0):1,(1,1):-2,(1,3):9,(2,1):1,(2,2):3,(2,3):5,(2,4):-4,(3,1):-1,(3,2):2,(3,4):4}
for (row,column) in macierz_dic:
    if (row,column):
        element = macierz_dic[(row,column)]
    else:
        element = 0
    print(f"{(row,column)}: {element}")