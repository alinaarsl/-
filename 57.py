queue =class Queue:
    def __init__(self):
        self.queue = []
    
    def size(self):
        size = len(self.queue)
        return size
    def push(self,n):
        self.queue.append(n)
        print('ok')
   
    def pop(self,n):
        return self.queue.pop()
    def front(self):
        return self.queue[0]
    def clear(self):
        self.queue.clear()
        print('ok')
    def exit(self):
        print('bye')
