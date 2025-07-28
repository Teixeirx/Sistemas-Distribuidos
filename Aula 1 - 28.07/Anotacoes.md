Criar pastas para cada aula para anotações, projetos, atividades, etc...

#Sistemas Distribuídos
Sistemas fracamente acoplados - grid computacional
    - Geograficamente distribuídos
    - Hardware e SO diferentes nas máquinas
    - Esquema de comunicação TCP/IP
    - Programação distribuída
    - Arquitetura de Sistemas:
        - cliente-servior
        - ponto a ponto
    - Comunicação -> Troca
        - String -> Mensagem
        - Objetos -> serialização
        - Sincronismo:
            - Relógio
            - Monitor ou Semáforo
            - ?
        - Tolerância a falhas

#Sistemas Paralelos
Sistemas fortemente acoplados - Cluster computacional
    - Mesma localização geografica
    - Hardware e SO iguais para todas as máquinas
    - Comunicação via Fibra
    - Sistema de NoBreak robusto
    - Sistema de backup.
    - Programação paralela

Plano de Ensino
    - Unidade 1: Fundamentos
        - comunicação
        - Procesos e threads
        - sincronização
    - Unidade 2: Comunicação
        - fundamentos
        - comunicação por troca de mensagens
        - sistemas distribuídos baseados em objetos
    - Unidade 3: Comunicação em grupo
        - fundamentos
        - multicast
        - comunicação confiável em grupoUnidade
    - Unidade 4: Sistemas de arquivos distribuídos e Memória compartilhada distribuída
        - fundamentos
        - modelo de consistência
        - estudo de casos
    - nota definida por: NF = [Nota 1(N1) + Nota 2(N2) + Nota 3(N3)] / 3


Aula 1 - Processos e Threads
    - Processo
        - Todos tem id e uma prioridade ao ser executado
        - Demanda Recurso
            - Hardware comuica com o(s)/a
                - processador
                - barramento
                - RAM + Cache
                - periféricos
    - Thread
        - "Mini processo"
        - Gestão
            - Status(Stop, sleep, ready, pause, resume)
            - Nome, id, prioridade
        - Sincronizar(Principal utilização dos Threads)
próxima aula será sobre threads(rever sobre isso durante a semana)