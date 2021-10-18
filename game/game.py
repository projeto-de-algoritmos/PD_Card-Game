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
        self.cards.append(Card(1, 1, 200, 40))
        self.cards.append(Card(2, 13, 40, 150))
        self.cards.append(Card(3, 8, 200, 150))

        # self.bstart = bt.CircleButton(130, 130, "start", 20)

        pyxel.run(self.update, self.draw)

    def update(self):

        if self.gamestate == "game":
            for card in self.cards:
                card.draw()

    def draw(self):
        pyxel.cls(0)

        if self.gamestate == "game":
            for card in self.cards:
                card.draw()
        
Game()