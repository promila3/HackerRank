class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        
        if len(self.second) > 0:
            top = self.second.pop()
            self.second.append(top)
            return top
        else :
            while len(self.first) > 1 :
                self.second.append(self.first.pop())
            top = self.first.pop()
            self.second.append(top)
            return top
        #print 'peek', self.first, self.second
        
    def pop(self):
        #print self.first, self.second
        if len(self.second) > 0 :
            self.second.pop()
        else : 
            while len(self.first) > 0 :
                self.second.append(self.first.pop())
            if (len(self.second) >0 ):
                self.second.pop()
        #print 'pop', self.first, self.second
    def push(self, value):
        #print self.first, self.second
        self.first.append(value)
        #print self.first, self.second

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.push(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
