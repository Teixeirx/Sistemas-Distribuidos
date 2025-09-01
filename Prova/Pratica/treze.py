#13. Uso de memória compartilhada (contador): 
# Implemente em Python um programa com duas threads que incrementam uma mesma variável global (contador). Mostre como ocorre a condição de corrida sem o uso de locks.

import threading

contador = 0

def incrementa():
    global contador
    for _ in range(100000):
        contador += 1

t1 = threading.Thread(target=incrementa)
t2 = threading.Thread(target=incrementa)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Valor final do contador (condição de corrida): {contador}")
