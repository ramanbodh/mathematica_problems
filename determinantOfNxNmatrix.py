#finding the determinant of n x n  matrices

def determinant(arrayX):
    if len(arrayX[0])==2:
        sum=((arrayX[0][0]*arrayX[1][1])-(arrayX[1][0]*arrayX[0][1]))
        return sum
    newarry=[[0 for _ in range(len(arrayX)-1)] for _ in range(len(arrayX)-1)]
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
                print(f"new array[{q}][{p}]={newarry[q][p]}")
                p+=1
            if t==i:
                continue
            q+=1
        print("--------------\n")
        if (i+1)%2==0:
            result-=(determinant(newarry))*mul
        else:
            result+=(determinant(newarry))*mul
        print(f"mul={mul} result={result}")

    return result

arraya=[[1,3,2],[-3,-1,-3],[2,3,1]]
result=determinant(arraya)
print(result)
        
            
                
            
            
    