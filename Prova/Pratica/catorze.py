# 14. Uso de Lock para sincronização: 
# Modifique o programa da questão anterior utilizando threading.Lock para evitar a condição de corrida e garantir que o contador final seja consistente.

import threading

contador = 0
lock = threading.Lock()

def incrementa_com_lock():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

t1 = threading.Thread(target=incrementa_com_lock)
t2 = threading.Thread(target=incrementa_com_lock)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Valor final do contador (com Lock): {contador}")
