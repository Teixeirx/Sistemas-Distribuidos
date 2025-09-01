# 11. Thread básica: 
# Implemente em Python um programa que crie duas threads: uma imprime números pares de 0 a 20, e a outra imprime números ímpares de 1 a 19. As threads devem rodar em paralelo

import threading

def imprime_pares():
    for i in range(0, 21, 2):
        print(f"Par: {i}")

def imprime_impares():
    for i in range(1, 20, 2):
        print(f"Ímpar: {i}")

# Criando threads
thread_par = threading.Thread(target=imprime_pares)
thread_impar = threading.Thread(target=imprime_impares)

# Iniciando threads
thread_par.start()
thread_impar.start()

# Aguardando finalização
thread_par.join()
thread_impar.join()