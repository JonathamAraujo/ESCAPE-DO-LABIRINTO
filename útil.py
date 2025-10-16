def calcular_limite_passos(maze):
    linhas = len(maze)
    colunas = len(maze[0])
    total_posicoes = linhas * colunas
    passos_minimos = total_posicoes // 15
    limite = int(passos_minimos * 2)
    
    return limite


def verificar_passos_restantes(passos_feitos, limite):
    passos_restantes = limite - passos_feitos
    if passos_restantes > 0:
        print(f"Você ainda tem {passos_restantes} movimentos restantes.")
        return True
    else:
        print("\nVocê perdeu! Acabaram seus movimentos.")
        print("Jogo encerrado.")
        return False
