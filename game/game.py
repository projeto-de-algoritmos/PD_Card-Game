import pyxel

import utils
import buttons as bt
from card import Card

class Game:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="DP Card Game", fps=30)
        pyxel.mouse(True)      
        pyxel.load("my_resource.pyxres") 

        self.gamestate = "game"
        self.cards = []
        self.cards.append(Card(0, 10, 40, 40))
        self.cards.append(Card(1, 10, 200, 40))
        self.cards.append(Card(2, 10, 40, 150))
        self.cards.append(Card(3, 10, 200, 150))
        self.bstart = bt.CircleButton(130, 130, "mito cria, o lixo copia", 20)

        pyxel.run(self.update, self.draw)

    def update(self):

        # self.bstart.update()

        if self.gamestate == "game":
            for card in self.cards:
                card.draw()


    def draw(self):
        pyxel.cls(0)

        # self.bstart.draw()

        if self.gamestate == "game":
            for card in self.cards:
                card.draw()
        
Game()