# python3 threads_io.py
import threading, time, queue
q=queue.Queue()
def io_task(i):
    time.sleep(0.5)  # pretend network/file wait
    q.put(f"done {i}")

threads=[threading.Thread(target=io_task,args=(i,)) for i in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]
while not q.empty(): print(q.get())
