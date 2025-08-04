import threading

def tarefa():
    for i in range(100):
        print (i)

t = threading.Thread(target=tarefa)
t.start()

t2 = threading.Thread(target=tarefa)
t2.start()