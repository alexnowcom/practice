import threading
import time

times = 101

def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, times)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)