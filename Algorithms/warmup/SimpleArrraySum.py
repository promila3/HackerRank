n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

sumarr = 0

iter = len(arr)
for i in range(0,iter):
    sumarr += arr[i]
    
    

print sumarr
