import pyxel

import utils

class Card:
    # suit = naipe
    # 0 = ouros 
    # 1 = espadas
    # 2 = copas
    # 3 = paus
    def __init__(self, s, weight, x, y):
        self.suit = s
        self.face = weight
        self.pos_x = x
        self.pos_y = y
        self.color = self.suit_color()
        self.value = int((weight**1.5)+s)

    def update(self):
        ...


    def draw(self):
        pyxel.rect(self.pos_x, self.pos_y, 30, 45, 7)

        draw_face = self.draw_face()

        pyxel.text(self.pos_x+3, self.pos_y+3, draw_face, self.color)
        #value
        draw_x = utils.align_text(self.pos_x+25, draw_face)
        pyxel.text(draw_x, self.pos_y+37, draw_face, self.color)
        #Imagem do naipe
        pyxel.blt(self.pos_x+7, self.pos_y+16, 0, self.suit*16, 0, 16, 16, 7)


    def suit_color(self):
        if self.suit == 0 or self.suit == 2:
            return 8
        return 0
        
    def draw_face(self):
        if self.face == 1:
            return "A"
        elif self.face == 11:
            return "J"
        elif self.face == 12:
            return "Q"
        elif self.face == 13:
            return "K"
        else:
            return str(self.face)

        