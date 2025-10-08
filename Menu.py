dificuldade = " "
def titulo():
    print("-"*30)
    print("     ESCAPE DO LABIRINTO       ")
    print(f"-"*30, "\n")
    
titulo()

def inicio():
    global dificuldade
    print("-"*30)
    dificuldade=input("     Dificuldade : ").upper()
    print(f"-"*30, "\n")
   
    
inicio()

def instrucoes():
    print("-"*30)
    print ("     MOVIMENTAÇAO: \n", "      (WASD) Para Andar \n", "      (Q) Para Sair do Jogo\n", "      (F) Para Interagir")
    print("-"*30)

instrucoes()






