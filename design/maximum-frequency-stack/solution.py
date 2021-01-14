class FreqStack(object):

    def __init__(self):
        self.freq_stack = []
        self.counts = defaultdict(int)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.counts[x] += 1
        if self.counts[x] > len(self.freq_stack):
            self.freq_stack.append([x])
        else:
            self.freq_stack[self.counts[x] - 1].append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        most_freq = self.freq_stack[-1].pop()
        if not self.freq_stack[-1]:
            self.freq_stack.pop()
            
        self.counts[most_freq] -= 1
        return most_freq


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()