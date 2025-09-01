# 15. Produtor-Consumidor com Queue: 
# Implemente um programa em Python que utilize threads para simular o problema Produtor-Consumidor. Use queue.Queue para comunicação entre threads.

import threading
import queue
import time
import random

q = queue.Queue()

def produtor():
    for i in range(10):
        item = f"Item-{i}"
        q.put(item)
        print(f"Produziu {item}")
        time.sleep(random.random())

def consumidor():
    for _ in range(10):
        item = q.get()
        print(f"Consumiu {item}")
        time.sleep(random.random())
        q.task_done()

t_produtor = threading.Thread(target=produtor)
t_consumidor = threading.Thread(target=consumidor)

t_produtor.start()
t_consumidor.start()

t_produtor.join()
t_consumidor.join()
