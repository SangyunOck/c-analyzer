class Stack:
    stack = []
    
    def pop(self, length):
        before_len = len(self.stack)
        self.stack = self.stack[:before_len - length]

    def peek(self):
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)