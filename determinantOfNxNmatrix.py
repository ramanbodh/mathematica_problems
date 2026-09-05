#finding the determinant of n x n  matrices

def determinant(arrayX):
    if len(arrayX[0])==2:
        sum=((arrayX[0][0]*arrayX[1][1])-(arrayX[1][0]*arrayX[0][1]))
        return sum
    newarry=[]
    mul=0
    result=0
    for i in range(len(arrayX)):
        q=0

        mul=arrayX[i][0]
        for t in range(len(arrayX)):
            p=0
            for j in range(len(arrayX)):
                if j==0 or i==t:
                     continue 
                newarry[q][p]=arrayX[t][j]
                p+=1
            q+1
        result+=(determinant(newarry))*mul

    return result

arraya=[[1,3,2],[-3,-1,-3],[2,3,1]]
result=determinant(arraya)
print(result)
        
            
                
            
            
    