import time

def iniciar_tempo():
    return time.time()

def tempo_restante(inicio, duracao):
    restante = duracao - (time.time() - inicio)
    if restante < 0:
        restante = 0
    return int(restante)

def avisos_tempo(inicio, duracao):
    while True:
        restante = tempo_restante(inicio, duracao)
        if restante == 0:
            print("Tempo esgotado!")
            break
        if restante % 10 == 0:
            print(f"Tempo restante: {restante} segundos!")
        time.sleep(1)
        
     
