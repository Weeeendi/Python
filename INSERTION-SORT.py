A = [5,1,7,2,4,3]
print(A[0])
for j in range(1, len(A)):
    key = A[j]
    #insert A[j] into the sorted sequence A[0..j-1]
    i = j - 1
    while i >= 0 and A[i] < key:
        A[i + 1] = A[i]
        i = i - 1
        
    A[i + 1] = key
print(A)    
