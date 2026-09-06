#finding the determinant of n x n  matrices

def determinant(arrayX):
    #this is base condition of 2x2 matrix
    if len(arrayX[0])==2:
        sum=((arrayX[0][0]*arrayX[1][1])-(arrayX[1][0]*arrayX[0][1]))
        return sum
    #base condition if the array is 1x1 matrix
    if len(arrayX)==1:
        return arrayX[0][0] #returning the elemant
    newarry=[[0 for _ in range(len(arrayX)-1)] for _ in range(len(arrayX)-1)]#new array where the subarray are saved
    mul=0#multiplier 
    result=0
    #now we are creating the sub array in following using recurssion 
    for i in range(len(arrayX)):#keep track of outer layer
        q=0

        mul=arrayX[i][0]#multiplier will be column first of chosen row
        for t in range(len(arrayX)):
            p=0
            for j in range(len(arrayX)):
                if j==0 or i==t:#not including the first column and selected row
                     continue 
                newarry[q][p]=arrayX[t][j]#every thing else is saved in newarry
                print(f"new array[{q}][{p}]={newarry[q][p]}")
                p+=1
            if t==i:
                continue#to skip the incrementation of the q counter for  selected row
            q+=1
        print("--------------\n")
        if (i+1)%2==0:#it is column first of +-+-
            result-=(determinant(newarry))*mul#-
        else:
            result+=(determinant(newarry))*mul#+
        print(f"mul={mul} result={result}")

    return result

#test array
arraya=[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
result=determinant(arraya)
print(result)

#test for  1X1 matrix determinant
a=[[5]]
print(determinant(a))
        
            
                
            
            
    