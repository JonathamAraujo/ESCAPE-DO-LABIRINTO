from labirintos import maze, screen, move
from Menu import inicio, titulo, instrucoes 
from útil import calcular_limite_passos, verificar_passos_restantes

def play(MAZE):
    titulo()
    inicio()
    instrucoes()
    passos_feitos = 0
    limite_passos = calcular_limite_passos(MAZE)
    print(f"\nO jogo começou! Você tem {limite_passos} movimentos para concluir o labirinto.\n")

    while True:
        screen(MAZE)

        if MAZE[-1][38] == "@":
            print(" Parabéns, você venceu o labirinto!")
            break

        command = input("Comando: ").strip().lower()

        if command == "q":
            print("Saindo do jogo labirinto...")
            break
        elif command in ["w", "a", "s", "d"]:
            passos_feitos += 1

            if not verificar_passos_restantes(passos_feitos, limite_passos):
                break

        if command=="q":
           print("Saindo do jogo labirinto...")     
           break
        elif command=="w":
          move(-1,0,MAZE)
               
        elif command=="s":
          move(1,0,MAZE)
               
        elif command=="a":
          move(0,-1,MAZE)
               
        elif command=="d":
          move(0,1,MAZE)
               
        else:
         print("ERRO! comando inválido!")
                     
play(maze)
