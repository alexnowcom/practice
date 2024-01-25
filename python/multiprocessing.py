from multiprocess import Process
import time

times = 11

def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print('Finished process.')

results = {}
processes = [Process(target=longSquare, args=(n, results)) for n in range(0, times)]
[p.start() for p in processes]
[p.join() for p in processes]
