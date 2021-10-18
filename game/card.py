import pyxel

import utils

class Card:
    # suit = naipe
    # 0 = ouros 
    # 1 = espadas
    # 2 = copas
    # 3 = paus
    def __init__(self, weight, suit, x, y):
        self.suit = suit
        self.face = weight
        self.pos_x = x
        self.pos_y = y
        self.color = self.suit_color()
        self.card_color = 7
        self.value = int((weight**1.5)+suit)

    def update(self):
        if self.card_color == 7 and pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (self.pos_x+30>pyxel.mouse_x>self.pos_x-1) and (self.pos_y+45>pyxel.mouse_y>self.pos_y-1):
            self.card_color = 6
            return 1
        else:
            return 0

    def draw(self):
        pyxel.rect(self.pos_x, self.pos_y, 30, 45, self.card_color)

        # Face
        draw_face = self.draw_face()
        pyxel.text(self.pos_x+3, self.pos_y+3, draw_face, self.color)
        
        draw_x = utils.align_text(self.pos_x+25, draw_face)
        pyxel.text(draw_x, self.pos_y+37, draw_face, self.color)

        # Valor
        draw_x = utils.align_text(self.pos_x+16, f"{self.value}")
        pyxel.text(draw_x, self.pos_y+27, f"{self.value}", 5)

        # Imagem do naipe
        pyxel.blt(self.pos_x+7, self.pos_y+11, 0, self.suit*16, 0, 16, 16, 7)

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

        