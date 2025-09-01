import threading
import random
import statistics

# parâmetros do problema
TOTAL_NUMEROS = 100000
TOTAL_LISTAS = 10
VALOR_MIN = 1000
VALOR_MAX = 100000

# cada lista será armazenada dentro desta estrutura
colecao_listas = [[] for _ in range(TOTAL_LISTAS)]

# função que será executada em cada thread
def preencher_lista(destino, qtd):
    for _ in range(qtd):
        destino.append(random.randint(VALOR_MIN, VALOR_MAX))

def main():
    threads = []
    numeros_por_lista = TOTAL_NUMEROS // TOTAL_LISTAS

    # cria e inicia todas as threads
    for idx in range(TOTAL_LISTAS):
        th = threading.Thread(target=preencher_lista, args=(colecao_listas[idx], numeros_por_lista))
        threads.append(th)
        th.start()

    # espera a finalização de todas as threads
    for th in threads:
        th.join()

    # junta todos os números em uma única lista
    conjunto_total = []
    for bloco in colecao_listas:
        conjunto_total.extend(bloco)

    # média
    media_geral = statistics.mean(conjunto_total)

    # exibe informações
    print("=" * 40)
    print(f"Listas geradas: {TOTAL_LISTAS}")
    print(f"Números por lista: {numeros_por_lista}")
    print(f"Quantidade final de elementos: {len(conjunto_total)}")
    print(f"Média dos valores: {media_geral:.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
