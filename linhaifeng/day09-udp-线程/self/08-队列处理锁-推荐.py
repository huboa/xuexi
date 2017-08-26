from multiprocessing import Queue
q=Queue(3)
q.put('first')
print(q.get())
q.put('second')
q.put('third')
q.put('fourth')

print(q.get())
print(q.get())
print(q.get())