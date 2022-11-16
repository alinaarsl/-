queue = []
def size():
    size = len(queue)
    return size
def push(queue,n):
    queue.append(n)
    print('ok')
def pop(queue,n):
    return queue.pop(0)
def front(queue):
    return queue[0]
def clear():
    queue.clear()
    print('ok')
def exit():
    print('bye')
