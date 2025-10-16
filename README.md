# Escape-the-maze

Um mini game de console desenvolvido em **Python**, como projeto da disciplina de **Matemática Aplicada à Computação**.  
O objetivo do jogo é escapar de um labirinto representado por uma **matriz**, você deve usar portais, pegar chaves e abrir portas. 
O jogador deve encontrar a saída **antes de esgotar o limite de passos**.

Se o limite de passos for atingido, o jogador perde a partida. 

---

## Funcionalidades

- Portais(0) te levam de um ponto a outro do labirinto(Somente uma vez).
- Portas(/) estão trancadas, é preciso pegar as chaves(f) para abrir.  
- Limitador de passos que define quantos movimentos o jogador pode fazer.  
- Condição de vitória (chegar na saída dentro da margem de passos).  
- Condição de derrota (usar todos os passos sem sair do labirinto).  
- Interface via console (modo texto).  

---

## Tecnologias Utilizadas

- **Python 3.10+**  

---

## Como Executar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/escape-do-labirinto.git
2. Acesse o diretório do projeto:
   ```bash
   cd escape-do-labirinto 
3. Execute o jogo:
   ```bash
   python main.py

---

## Estrutura do Projeto

  ```bash
  escape-do-labirinto/
  ├── main.py           # Arquivo principal, inicia o jogo
  ├── labirintos.py     # Conjunto de matrizes dos labirintos (pré-definidos)
  ├── menu.py           # Funções do menu inicial
  ├── util.py          # Funções auxiliares (limitador de passos)
  └── README.md         # Documentação do projeto
  ```

---

## Autores

**[Artur Peres dos Santos](https://github.com/Artur-Peres)**

[Jonatham Alves Araujo](https://github.com/JonathamAraujo)

[Ana Beatriz Ferreira Cavalcante](https://github.com/Anab-Cavalcante)

