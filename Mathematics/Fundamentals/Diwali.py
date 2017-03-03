'''
On the eve of Diwali, Hari is decorating his house with a serial light bulb set. The serial light bulb set has N bulbs placed sequentially on a string which is programmed to change patterns every second. If at least one bulb in the set is on at any given instant of time, how many different patterns of light can the serial light bulb set produce?

Note: Lighting two bulbs *-* is different from **-

Input Format 
The first line contains the number of test cases T, T lines follow. 
Each line contains an integer N, the number of bulbs in the serial light bulb set.

Output Format 
Print the total number of patterns modulo 105
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    print (2**n -1 ) % 100000
