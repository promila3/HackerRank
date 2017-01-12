def array_left(a,n):
    temp = a[0]
    for i in range(n-1):
        a[i] = a[(i+1) % n]
        #temp, a[(i-1) % n] = a[(i-k) % n] , temp
    a[n-1] = temp
    #print a  
    return a

def array_left_rotation(a, n, k):
    
    #for i in range(k):
       # a = array_left(a,n)
    #temp = a[0]
    b = []
    for i in range(n):
        #temp1 = a[i]
        #a[i] = a[(i+k) % n]
        b.append(a[(i+k) % n])
        #temp, a[(i-1) % n] = a[(i-k) % n] , temp
    #a[n-1-k] = temp
    return b

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
