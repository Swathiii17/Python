class Queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return len(self.queue)==0
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
def is_palindrome(s):
    q=Queue()
    for char in s:
        q.enqueue(char)
    while q.size()>1:
        if q.dequeue()!=q.queue[-1]:
            return False
        q.queue.pop()
    return True
test=input("enter ")
if is_palindrome(test):
    print(f'"{test}" is a palindrome.')
else:
    print(f'"{test}" is not a palindrome.')
