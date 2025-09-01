# 16. Simulação de relógio lógico: 
# Implemente em Python um programa com duas threads que representam dois processos. Cada thread gera eventos locais e envia mensagens à outra. Utilize um contador lógico simples (Lamport) para marcar os eventos.

import threading
import time

lamport1 = 0
lamport2 = 0

def processo1():
    global lamport1, lamport2
    for i in range(3):
        lamport1 += 1
        print(f"Processo 1 evento local {i+1}, Lamport={lamport1}")
        time.sleep(1)
        lamport2 = max(lamport1, lamport2) + 1
        print(f"Processo 1 envia mensagem para Processo 2, Lamport Processo2={lamport2}")

def processo2():
    global lamport1, lamport2
    for i in range(3):
        lamport2 += 1
        print(f"Processo 2 evento local {i+1}, Lamport={lamport2}")
        time.sleep(1)

t1 = threading.Thread(target=processo1)
t2 = threading.Thread(target=processo2)

t1.start()
t2.start()
t1.join()
t2.join()
