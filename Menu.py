dificuldade = ""
def titulo():
    print("-"*30)
    print("     ESCAPE DO LABIRINTO       ")
    print(f"-"*30,"\n")
    return 
titulo()

def inicio():
    global dificuldade
    print("-"*30)
    dificuldade=input("Selecione a Dificuldade (Fácil/Médio/Difícil): ").upper()
    print("-"*30)
    return
inicio()






