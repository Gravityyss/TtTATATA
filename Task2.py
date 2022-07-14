#input = ['C','G','G', 'A','C','C', 'C','A','G',  'A', 'C', 'U',  'U', 'U','C']
input = ['G','G','G','A','A','A','U','C','C']

length = len(input)

matrix = [[0 for i in range(length)] for j in range(length)]
traceMatrix = [['N' for i in range(length)] for j in range(length)]

def fillMatrix(matrix,input,traceMatrix):
    for i, j in zip(range(0, length), range(0, length)):
        traceMatrix[i][j]='S'

    for k in range(length):
        for i,j in zip(range(0, length), range(k+1,length)): #Moves diagonally by looping from the first row each time (i=0), while j increments (1,2,3)
            matrix[i][j] = findMax(i,j,matrix,input,traceMatrix)
        print("")


def findMax(i,j,matrix, input,traceMatrix):
    nuc1 = input[i]
    nuc2 = input[j]
    print(i, j, " : ", nuc1, nuc2)

    diagonal=0  #remains 0 if no match is found
    flag = False
    #flagWobble= False
    if(nuc1=='A' and nuc2=='U'):
        diagonal = matrix[i+1][j-1] + 1
        flag= True
    elif(nuc1=='U' and nuc2=='A'):
        diagonal = matrix[i + 1][j - 1] + 1
        flag = True
    elif(nuc1=='G' and nuc2 == 'C'):
        diagonal = matrix[i + 1][j - 1] + 1
        flag = True
    elif (nuc1 == 'C' and nuc2 == 'G'):
        diagonal = matrix[i + 1][j - 1] + 1
        flag = True
    elif (nuc1 == 'G' and nuc2 == 'U'):
        diagonal = matrix[i + 1][j - 1] + 1
        flag = True
        #flagWobble = True
    elif (nuc1 == 'U' and nuc2 == 'G'):
        diagonal = matrix[i + 1][j - 1] + 1
        flag = True
        #flagWobble = True

    left=matrix[i][j - 1]
    down=matrix[i + 1][j]
    bif=bifurcation(i,j,matrix)

    maxList = [diagonal, left, down, bif[0]]
    max_value = max(maxList)
    max_index = maxList.index(max_value)

    
    if(max_index==0 and flag):
        #if(flagWobble):
         #   traceMatrix[i][j] = 'W'  # Cross/Diagonal
        #else:
        traceMatrix[i][j]= 'C' #Cross/Diagonal
    elif(max_index==1): #Equal L when Down and Left are equal
        traceMatrix[i][j] = 'L' #Left
    elif (max_index == 2):
        traceMatrix[i][j] = 'D' #Down
    elif (max_index == 3):
        traceMatrix[i][j] = ['B', bif[1]] #Bifurcation, adds K to traceMatrix

    return max_value

def bifurcation(i,j, matrix):
    max=0
    temp=0
    for k in range(i+1, j):
        #print("k: ", k)
        s = matrix[i][k] + matrix[k + 1][j]
        #print("s: ",s)
        if(s>max):
            max=s
            temp=k

    values=[max,temp]
    return values

fillMatrix(matrix,input,traceMatrix)
print("")
for row in matrix:
    print(row)
print("")

for row in traceMatrix:
    print(row)
print("")

#example
x = traceMatrix[0][0]
#x = traceMatrix[1][13]
#x = traceMatrix[0][14]
print(x)

if(x[0]=='B'):
    k = x[1]
    print("k: ", k)
else:
    print(x[0])
