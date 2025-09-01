# 19. Thread e deadlock: 
# Implemente um exemplo em Python onde duas threads tentam acessar dois recursos compartilhados, gerando um deadlock. Em seguida, explique como evitar o problema.

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print("Thread1: lock1 adquirido")
        time.sleep(1)
        with lock2:
            print("Thread1: lock2 adquirido")

def thread2():
    with lock2:
        print("Thread2: lock2 adquirido")
        time.sleep(1)
        with lock1:
            print("Thread2: lock1 adquirido")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

# Deadlock: Ocorre quando thread1 segura lock1 e espera lock2 enquanto thread2 segura lock2 e espera lock1.
# Como evitar: Sempre adquirir locks na mesma ordem em todas as threads ou usar threading.Lock().acquire(timeout=...).