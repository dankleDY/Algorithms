# Complexity and sorting

# We ask 3 questions about algorithms:
#     1. Is it correct?
#     2. How much time does it take?
#     3. Can we do better?

# We think of programs as Turing Machines to decide its complexity. (Scan through the string, O(n))
# O(n) is good, we prefer scanning a string several times to n times.

# Sorting
#     The bound of sorting is O(nlogn), usually it means recursively divide in half

"""
SelectionSort(HeapSort use min-heap to do the same thing)

1. Divide index k
2. Select the smallest in unsorted
3. Put it in its position(k)
Two loops, O(n^2)

"""

def SelectionSort(A):
for k in range (len(A)):
    minI=k
    for curr in range (k,len(A)):
        if(A[curr]<=A[minI]):
            minI=curr
    A[k],A[minI]=A[minI],A[k] 
return A

"""
InsertionSort

1. Divide index k
2. Insert element k+1 into sorted
3. To insert, compare and swap sorted elements right until the position is found

Best O(n), worst O(n^2)
"""
def InsertionSort(A):
    for k in range (1,len(A)):
        key=A[k]
        i=k-1
        while(i>=0 and key<A[i]):
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A

"""
BubbleSort

1. Bubble the biggest num to the end
2. Two loops, one scan, one bubble

O(n^2)
"""
def BubbleSort(A):
    
    for k in range (len(A)):
        for j in range (len(A)-k-1):
            if(A[j]>A[j+1]):
                A[j] ,A[j+1]=A[j+1],A[j]
    return A

"""
MergeSort

1. Recursively divide array in half
2. Base case S >= E index, then begin merge
3. To merge, compare and put back in order. Need 3 while loops

O(nlogn)
"""


def Merge(A, S, m,E):
    lengthL = m - S+1
    lengthR = E - m

    L = [0]*lengthL
    R =[0]*lengthR

    for i in range (0,lengthL):
        L[i]=A[S+i]
    for j in range (0,lengthR):
        R[j]=A[m+j+1]

    i=j=0
    k=S

    while(i<lengthL and j < lengthR):
        if(L[i]<=R[j]):
            A[k]=L[i]
            i +=1
        else:
            A[k]=R[j]
            j += 1
        k +=1

    while i<lengthL:
        A[k]=L[i]
        i +=1
        k+=1
    while j<lengthR:
        A[k]=R[j]
        j +=1
        k+=1
        
def MergeSortHelper(A,S,E):
    
    if(S>=E):
        return
    else:
        m = (S+E)//2
        MergeSortHelper(A,S,m)
        MergeSortHelper(A,m+1,E)
        Merge(A,S,m,E)
    
def MergeSort(A):
    MergeSortHelper(A,0,len(A)-1)
    print(A)
    return A

"""
QuickSort

1. Seperate array into two parts, left smaller than piv, right greater
2. Use double index to seperate, k scan, index mark pivot position, then swap pivot with index
3. Recursively call funtion to sort left and right

O(nlogn)
"""
def QuickSort(A, i, j):
    if (j-i)<=1 :
        return A
    piv=A[j-1]
    # print("piv is")
    # print(piv)
    ind=i
    for k in range(i,j-1):
        if A[k]<piv:
            # print("A[k] is")
            # print(A[k])
            # print(A[ind])
            A[ind],A[k]=A[k],A[ind]
            ind=ind+1
    A[ind],A[j-1]=A[kj-1],A[ind]
    # print("---")
    QuickSort(A,i,ind)
    QuickSort(A,ind+1,j)
    return A


# reference: 
#     Duke ece 590 - Eric Autry
