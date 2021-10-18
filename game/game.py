import pyxel

import utils
import buttons as bt
from card import Card

class Game:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="DP Card Game", fps=30)
        pyxel.mouse(True)      
        pyxel.load("my_resource.pyxres") 
        self.num_cards = 18
        self.gamestate = "game"

        self.weight = 0
        self.cards = []
        deck, self.weight = utils.fill_deck(self.num_cards)

        for i in range(self.num_cards):
            self.cards.append(Card(deck[i][0],deck[i][1], 14+33*(i%7), 14+55*(i//7)))
        
        self.bstart = bt.CircleButton(130, 130, "start", 20)

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