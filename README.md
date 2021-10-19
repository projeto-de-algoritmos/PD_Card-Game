# Card Game 

**Número da Lista**: 5<br>
**Conteúdo da Disciplina**: PD<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0113585  |  Hugo Ricardo Souza Bezerra |
| 18/0125770  |  Lucas Gabriel Bezerra      |

## Sobre 
O Card Game é um jogo de cartas que utiliza da lógica do problema da mochila (Knapsack).

O Objetivo do jogo é selecionar as cartas, a fim de conseguir o maior valor(definido por calculo sobre o número da carta e o naipe)
possível, respeitando o limite de peso. O peso de cada carta é dada pelo 
número da carta(para A, J, Q, K tem-se os valores, respectivamente, 1, 11, 12, 13).

Ao clicar em confirmar, o jogador submete a solução e o algoritmo de programação dinâmica(chamado de knapsack) é executado e retorna a melhor solução possível, destacando as cartas da seguinte maneira:

- Dourado: cartas que fazem parte da solução e foram escolhidas pelo jogador  
- Verde: cartas que fazem parte da solução e não foram escolhidas pelo jogador  
- Vermelho: cartas que foram escolhidas pelo jogador e não fazem parte da solução

## Screenshots

![](https://i.imgur.com/TE4fgdw.gif)

![](https://i.imgur.com/1D24AeD.png)
![](https://i.imgur.com/Q2Kg6Me.png)
![](https://i.imgur.com/ElusoUN.png)

## Vídeo

[![Video](https://img.youtube.com/vi/vUcLA1UKars/0.jpg)](https://www.youtube.com/watch?v=vUcLA1UKars)

> https://www.youtube.com/watch?v=vUcLA1UKars

## Instalação 
**Linguagem**: Python<br>
**Framework**: --- <br>

**Pré-requisitos** para rodar o Card Game:
* Instale o [Python](https://www.python.org/downloads/) (versão 3.8.5)
* Instale o [Pyxel](https://github.com/kitao/pyxel/blob/master/README.pt.md) (versão 1.4.3)

## Instalar e Executar (Sistema baseado em Debian)

    $ pip3 install pyxel 
    $ git clone https://github.com/projeto-de-algoritmos/PD_Card-Game.git
    $ cd PD_Card-Game/game
    $ python3 game.py

## Uso 

- Inicie a aplicação
- Escolha com quantas cartas deseja jogar
- Clique nas cartas que você acha que fazem parte da solução
- Quando estiver satisfeito com sua solução clique no botão confirmar
- Confira a solução e caso queira jogar novamente clique no botão menu