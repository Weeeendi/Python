import time
from invert_squences import invert
#将两个二进制数相加
start = time.time()
A = "0100010"
B = "1100100"
C = []
carry = 0 #进位符
i = len(A)-1
while i>=0 :
    c = int(A[i]) + int(B[i]) + carry
    if c == 2:
        carry = 1
        c = 0
    elif c == 3:
        carry = 1
        c = 1
    else:
        carry = 0    
    i = i - 1 
    C.append(c)
if carry == 1:
    C.append(carry)
C = invert(C)    
print(C)
end = time.time()
print(str(end-start)+'s')