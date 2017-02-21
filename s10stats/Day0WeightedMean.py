# Enter your code here. Read input from STDIN. Print output to STDOUT
N =int(raw_input())
x = map(int,raw_input().strip().split())
w = map(int,raw_input().strip().split())
sumw = sum(w)
nume = [ xi * wi for xi,wi in zip(x,w)]

mw = (sum(nume) * 1.0)/sumw
print "%.1f" % mw
