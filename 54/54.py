class Stack:
    def __init__(self):
        self.stack = []
    
    def size(self):
        size = len(self.stack)
        return size
    def push(self,n):
        self.stack.append(n)
        print('ok')
   
    def pop(self,n):
        return self.stack.pop()
    def back(self):
        return self.stack[-1]
    def clear(self):
        self.stack.clear()
        print('ok')
    def exit(self):
        print('bye') 
