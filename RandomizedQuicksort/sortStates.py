from random import randint

#Formula for Randomized-Partition
def ranodmizedPartition(A,start,end):
    pivot=randint(start,end)
    temp=A[end]
    A[end]=A[pivot]
    A[pivot]=temp
    newPivotIndex=start-1
    for index in range(start,end):
        if A[index]<A[end]:#check if current val is less than pivot value
            newPivotIndex=newPivotIndex+1
            temp=A[newPivotIndex]
            A[newPivotIndex]=A[index]
            A[index]=temp
    temp=A[newPivotIndex+1]
    A[newPivotIndex+1]=A[end]
    A[end]=temp
    return newPivotIndex+1

#Formula for Randomized-Quicksort
def randomizedQuickSort(A,start,end):
    if start<end:
        pivot=randint(start,end)
        temp=A[end]
        A[end]=A[pivot]
        A[pivot]=temp
        p=ranodmizedPartition(A,start,end)
        randomizedQuickSort(A,start,p-1)
        randomizedQuickSort(A,p+1,end)
    
#Creates matrix based on user inputs 
def alphabeticalMatrix(pop, state):
    i = 0
    for pop in X:
        Matrix[0][i] = pop
        i += 1
    r = 0
    for state in S:
        Matrix[1][r] = state
        r += 1
#Takes user inputs, calls randomized quicksort alogothim and outputs ordered by largest integer value first      
def sortedStates(pop, stateMatrix):
    
    for pop in X:
        for t in range(0, 50):
            if pop == Matrix[0][t]:
                Output.append(Matrix[1][t])
            
X=[4849377, 736732, 6731484, 2966369, 38802500, 5355866, 3596677, 935614, 19893297, 10097343, 1419561, 1634464, 12880580,
6596855, 3107126, 2904021, 4413457, 4649676, 1330089, 5976407, 6745408, 9909877, 5457173, 2994179, 6063589, 1023579, 1881503,
2839099, 1326813, 8938175, 2085572, 19746227, 9943964, 739482, 11594163, 3878051, 3970239, 12787209, 1055173, 4832482, 853175,
6549352, 26956958, 2942902, 626630, 8326289, 7061530, 1850326, 5757564, 584153]

S=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

Output = []

Matrix = [[0 for x in range(51)] for x in range(2)]

alphabeticalMatrix(X, S)
randomizedQuickSort(X,0,len(X)-1)
sortedStates(X, Matrix)

#Print results in descending order
for p in reversed(range(0, 50)):
    print(Output[p])


