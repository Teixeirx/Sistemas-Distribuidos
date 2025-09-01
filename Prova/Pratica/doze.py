#12. Threads com atraso: 
# Implemente em Python um programa que crie três threads. Cada thread deve imprimir seu nome ("Thread 1", "Thread 2", "Thread 3") com intervalos de tempo diferentes (ex.: 1s, 2s, 3s).

import threading
import time

def imprime_nome(nome, atraso):
    for _ in range(5):
        print(nome)
        time.sleep(atraso)

# Criando threads
t1 = threading.Thread(target=imprime_nome, args=("Thread 1", 1))
t2 = threading.Thread(target=imprime_nome, args=("Thread 2", 2))
t3 = threading.Thread(target=imprime_nome, args=("Thread 3", 3))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
