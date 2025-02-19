from collections import deque

class Processo:
    def __init__(self, nome, tempo_execucao, chegada=0):
        self.nome = nome
        self.tempo_execucao = tempo_execucao
        self.chegada = chegada

fila_processos = deque([
    Processo("P1", 3, 0),
    Processo("P2", 5, 1),
    Processo("P3", 2, 2),
])

tempo_atual = 0
tempo_espera_total = 0
tempo_retorno_total = 0
tempo_resposta_total = 0
processos_finalizados = []

print("Escalonamento FCFS:")
while fila_processos:
    processo = fila_processos.popleft()
    tempo_espera = max(0, tempo_atual - processo.chegada)
    tempo_resposta = tempo_espera
    tempo_atual += processo.tempo_execucao
    tempo_termino = tempo_atual  
    tempo_retorno = tempo_termino - processo.chegada

    tempo_espera_total += tempo_espera
    tempo_retorno_total += tempo_retorno
    tempo_resposta_total += tempo_resposta

    processos_finalizados.append(processo)

    print(f"{processo.nome}: Espera = {tempo_espera}, Término = {tempo_termino}")

n = len(processos_finalizados)
tempo_medio_espera = tempo_espera_total / n
tempo_medio_retorno = tempo_retorno_total / n
tempo_medio_resposta = tempo_resposta_total / n
utilizacao_cpu = (tempo_atual / tempo_termino) * 100

print("\nMétricas do Escalonamento FCFS:")
print(f"Tempo médio de espera: {tempo_medio_espera:.2f}")
print(f"Tempo médio de retorno: {tempo_medio_retorno:.2f}")
print(f"Tempo médio de resposta: {tempo_medio_resposta:.2f}")
print(f"Utilização da CPU: {utilizacao_cpu:.2f}%")
