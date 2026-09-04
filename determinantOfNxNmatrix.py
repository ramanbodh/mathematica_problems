#finding the determinant of n x n  matrices

def determinant(arrayX,sum=0,mul=1):
    if len(arrayX[0])==2:
        sum=((arrayX[0][0]*arrayX[1][1])-(arrayX[1][0]*arrayX[0][1]))*mul
        return sum
    newarry=[]
    mul=0
    for i in len(arrayX):
        for j in len(arrayX):
            if i==j:
                mul=arrayX[i][j]
                continue
            if j==0:
                continue
            if 
            newarry=arrayX[i][j]
    sum+=determinant(arrayX,sum,mul)
    retun sum
            
                
            
            
    