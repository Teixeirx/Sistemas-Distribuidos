# 18. Barrier (sincronização de threads): 
# Implemente em Python um programa que crie quatro threads. Todas devem executar uma parte de uma tarefa, mas só podem prosseguir para a próxima etapa quando todas as threads terminarem a primeira parte (use threading.Barrier).

import threading
import time

barreira = threading.Barrier(4)

def tarefa(id):
    print(f"Thread {id} executando primeira parte")
    time.sleep(id)  # simula trabalho
    print(f"Thread {id} esperando na barreira")
    barreira.wait()
    print(f"Thread {id} iniciando segunda parte")

threads = [threading.Thread(target=tarefa, args=(i,)) for i in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join()
