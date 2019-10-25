# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import sys


ar = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   ar.append(arr_t)
    
maxsum = -64    
for i in range(6):
    for j in range(6):
         if(j+2 < 6 and i+2 < 6 ):
                sum = ar[i][j] + ar[i][j+1] + ar[i][j+2] + ar[i+1][j+1] + ar[i+2][j] + ar[i+2][j+1] + ar[i+2][j+2]
                if sum > maxsum :
                    maxsum = sum
print(maxsum)
