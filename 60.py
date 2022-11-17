class Deque:
    def __init__(self):
        self.deque = []
        
    def size(self):
        return len(self.deque)
        
    def push_front(self,n):
        self.deque.insert(0, n) 
        print ('ok')
    
    def push_back(self,n):
        self.deque.append(n)
        print('ok')
        
    def pop_front(self):
        return self.deque.pop(0)
    def pop_back(self):
        return self.deque.pop(-1)
    
    def front(self):
        return self.deque[0]
    def back(self):
        return self.deque[-1]
    
    def clear(self):
        self.queue.clear()
        print('ok')
    def exit(self):
        print('bye')
