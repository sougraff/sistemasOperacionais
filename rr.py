from collections import deque


class Processo:
    def __init__(self, nome, tempo_execucao, chegada=0):
        self.nome = nome
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.chegada = chegada
        self.tempo_inicio = None
        self.tempo_fim = None


fila_processos = deque([
    Processo("P1", 10, 0),
    Processo("P2", 4, 1),
    Processo("P3", 6, 2)
])

quantum = 3 
tempo_atual = 0
tempo_espera_total = 0
tempo_retorno_total = 0
tempo_resposta_total = 0
processos_finalizados = []

print("Escalonamento Round Robin:")
while fila_processos:
    processo = fila_processos.popleft() 

    if processo.tempo_inicio is None:  
        processo.tempo_inicio = tempo_atual 

    if processo.tempo_restante > quantum:
        print(f"{processo.nome} executou por {quantum} unidades de tempo.")
        tempo_atual += quantum
        processo.tempo_restante -= quantum
        fila_processos.append(processo)  
    else:
        print(f"{processo.nome} finalizado após {processo.tempo_restante} unidades de tempo.")
        tempo_atual += processo.tempo_restante
        processo.tempo_restante = 0
        processo.tempo_fim = tempo_atual 
        processos_finalizados.append(processo)


for processo in processos_finalizados:
    tempo_retorno = processo.tempo_fim - processo.chegada
    tempo_espera = tempo_retorno - processo.tempo_execucao
    tempo_resposta = processo.tempo_inicio - processo.chegada

    tempo_espera_total += tempo_espera
    tempo_retorno_total += tempo_retorno
    tempo_resposta_total += tempo_resposta

n = len(processos_finalizados)
tempo_medio_espera = tempo_espera_total / n
tempo_medio_retorno = tempo_retorno_total / n
tempo_medio_resposta = tempo_resposta_total / n
utilizacao_cpu = (tempo_atual / tempo_atual) * 100 

print("\nMétricas do Escalonamento Round Robin:")
print(f"Tempo médio de espera: {tempo_medio_espera:.2f}")
print(f"Tempo médio de retorno: {tempo_medio_retorno:.2f}")
print(f"Tempo médio de resposta: {tempo_medio_resposta:.2f}")
print(f"Utilização da CPU: {utilizacao_cpu:.2f}%")
