# 17. Thread com parâmetro: 
# Implemente em Python um programa que crie uma thread responsável por calcular a soma de uma lista de números inteiros passada como parâmetro. A thread deve retornar o resultado.

import threading

def soma_lista(lista, resultado):
    resultado.append(sum(lista))

numeros = [1, 2, 3, 4, 5]
resultado = []

t = threading.Thread(target=soma_lista, args=(numeros, resultado))
t.start()
t.join()

print(f"Soma da lista: {resultado[0]}")
