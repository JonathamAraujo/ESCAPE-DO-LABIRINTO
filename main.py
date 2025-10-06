from labirintos import maze, maze1, maze2, screen, move, posPlayer, mazePosAvatar
from Menu import inicio, dificuldade 
print(dificuldade)
def play(MAZE):
    mazePosAvatar()
    while True:
        screen(MAZE)
        if posPlayer==MAZE[-1][7]:
           print("Parabéns, você venceu o labirinto de nível [dificuldade]!")
           break
        
        command = input("Comando: ").strip().lower()

        if command=="q":
           print("Saindo do jogo...")
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

if dificuldade=="FACIL":
   play(maze)
elif dificuldade=="MEDIO":
   play(maze1)
elif dificuldade=="DIFICIL":
   play(maze2)