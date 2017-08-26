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
q.put('fourth',block=False)
q.put('fourth',timeout=3)
q.put_nowait('first')