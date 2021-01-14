class MinStack(object):

    def __init__(self):
        self.stack = [(0, float('inf'))]

    def push(self, x):
        self.stack.append((x, min(x, self.stack[-1][1])))
        
    def pop(self):
        return self.stack.pop()
        
    def top(self):
        return self.stack[-1][0]
        
    def getMin(self):
        return self.stack[-1][1]