import random
import pyxel

import utils
import buttons as bt
from card import Card

class Game:
    def __init__(self):
        pyxel.init(utils.WIDTH, utils.HEIGHT, caption="DP Card Game", fps=30)
        pyxel.mouse(True)      
        pyxel.load("my_resource.pyxres") 
        self.gamestate = "menu"

        self.timer = 0
        self.num_cards = 7
        self.max_weight = 0
        self.cards = []

        self.sorted_cards = []
        self.knap_table = []

        self.player_sum = 0
        self.player_weight = 0   
        
        self.bt_minus = bt.PushButton(utils.WIDTH/2-15, utils.HEIGHT/2+73, "-", 5)
        self.bt_plus  = bt.PushButton(utils.WIDTH/2+14, utils.HEIGHT/2+73, "+", 5)

        self.b_start = bt.CircleButton(utils.WIDTH/2, utils.HEIGHT/2, "JOGAR!", 20)
        self.b_submit = bt.RectButton(utils.WIDTH-40, 20, "CONFIRMAR", 50, 12)
        self.b_end = bt.CircleButton(utils.WIDTH/2, utils.HEIGHT/2+92, "MENU", 20)

        pyxel.run(self.update, self.draw)

    def update(self):

        if self.gamestate == "menu":
            if self.bt_minus.update():
                if self.num_cards > 5:
                    self.num_cards -=1
            if self.bt_plus.update():
                if self.num_cards < 21:
                    self.num_cards +=1

            self.b_start.update()
            if self.b_start.is_on:
                self.b_start.is_on = False

                # cleaning variables
                self.timer = 0
                # self.num_cards = 0
                self.max_weight = 0
                self.solution = -1
                self.cards = []
                self.sorted_cards = []
                self.knap_table = []
                self.player_sum = 0
                self.player_weight = 0

                # filling variables
                # self.num_cards = 21#random.randint(7, 14)

                deck = utils.fill_deck(self.num_cards)
                self.max_weight = utils.get_max_weight(deck)

                for i in range(self.num_cards):
                    self.cards.append(Card(deck[i][0],deck[i][1], 14+33*(i%7), 32+55*(i//7)))

                self.sorted_cards = deck.copy()
                self.sorted_cards.sort(key=lambda x: (x[0], x[1]))   

                self.player_sum = 0
                self.player_weight = 0

                # reset submit button
                self.b_submit.is_on = False
                self.b_submit.text = "CONFIRMAR"

                self.gamestate = "game"


        elif self.gamestate == "game":

            if self.player_weight > self.max_weight:
                self.gamestate = "overflow"

            if not self.b_submit.is_on:
                self.b_submit.update()

                if pyxel.frame_count % 30 == 0:
                    self.timer += 1

                for card in self.cards:
                    if card.update() == 1:
                        self.player_sum += card.value
                        self.player_weight += card.face
            else:
                if self.knap_table == []:
                    self.b_submit.text = "CONFIRMADO"
                    w_list = []
                    v_list = []
                    for card in self.sorted_cards:
                        w_list.append(card[0])
                        v_list.append(int((card[0]**1.5)+card[1]))

                    self.knap_table = utils.knapsack(self.max_weight, w_list, v_list, self.num_cards)
                    self.solution = self.knap_table[self.num_cards][self.max_weight]
                    cards_ans = utils.solution_knapsack(self.knap_table, w_list, self.num_cards, self.max_weight)

                    for card in self.cards:
                        for ans_card in cards_ans:
                            if card.face == self.sorted_cards[ans_card][0] and card.suit == self.sorted_cards[ans_card][1] :
                                # print(f"FACE: {card.face}, SUIT: {card.suit}")
                                if card.card_color == 6:
                                    card.card_color = 10
                                else:
                                    card.card_color = 11
                                break

                            if ans_card == cards_ans[-1]:
                                if card.card_color == 6:
                                    card.card_color = 14

                    # RESPOSTA:
                    # print(f"SOLUTION: {self.solution}")
                    # for card in cards_ans:
                    #     print(self.sorted_cards[card])

                self.b_end.update()
                if self.b_end.is_on:
                    self.b_end.is_on = False
                    
                    self.gamestate = "menu"

        elif self.gamestate == "overflow":
            self.b_end.update()

            if self.b_end.is_on:
                self.b_end.is_on = False
                
                self.gamestate = "menu"

    def draw(self):
        pyxel.cls(0)

        if self.gamestate == "menu":
            Card(7, 2, 10, 20).draw()
            
            text_1 = """- O OBJETIVO do jogo e escolher cartas para obter\no maior valor possivel sem ultrapassar o limite\nde peso"""
            text_2 = "- Valor da carta: numero abaixo do naipe calculado\n com base no peso e acrescido um bonus do naipe"
            text_3 = "- Peso da carta: numero da carta"

            pyxel.text(50, 20, text_1, 7)
            pyxel.text(50, 43, text_2, 12)
            pyxel.text(50, 60, text_3, 8)

            pyxel.text(utils.WIDTH/2+55, utils.HEIGHT/2 +30,  "PESO DAS CARTAS:", 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +40,  "  A = 1" , 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +50,  "  2 = 2" , 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +60,  "  3 = 3" , 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +68,  "    ."   , 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +73,  "    ."   , 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +78,  "    ."   , 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +90,  "  J = 11", 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +100, "  Q = 12", 7)
            pyxel.text(utils.WIDTH/2+65, utils.HEIGHT/2 +110, "  K = 13", 7)

            pyxel.text( 5, utils.HEIGHT/2 +30, "BONUS DO NAIPE:", 7)
            pyxel.blt( 15, utils.HEIGHT/2 +40, 0, 0*16, 0, 16, 16, 2)
            pyxel.text(30, utils.HEIGHT/2 +45, " = +0", 7)
            pyxel.blt( 15, utils.HEIGHT/2 +60, 0, 1*16, 0, 16, 16, 2)
            pyxel.text(30, utils.HEIGHT/2 +65, " = +1", 7)
            pyxel.blt( 15, utils.HEIGHT/2 +80, 0, 2*16, 0, 16, 16, 2)
            pyxel.text(30, utils.HEIGHT/2 +85, " = +2", 7)
            pyxel.blt( 15, utils.HEIGHT/2 +100, 0, 3*16, 0, 16, 16, 2)
            pyxel.text(30, utils.HEIGHT/2 +105," = +3", 7)

            self.b_start.draw()

            self.bt_minus.draw()
            self.bt_plus.draw()

            posx = utils.align_text(utils.WIDTH/2, "CARTAS")
            pyxel.text(posx, utils.HEIGHT/2 + 55, "CARTAS", 7)
            posx = utils.align_text(utils.WIDTH/2, f"{self.num_cards}")
            pyxel.text(posx, utils.HEIGHT/2 + 70, f"{self.num_cards}", 7)

        elif self.gamestate == "game":

            pyxel.line(-10, 28, utils.WIDTH+10, 28, 4)
            pyxel.line(-10, 29, utils.WIDTH+10, 29, 4)

            pyxel.rect(0, 30, utils.WIDTH, utils.HEIGHT-64-30, 3)

            pyxel.line(-10, 192, utils.WIDTH+10, 192, 4)
            pyxel.line(-10, 193, utils.WIDTH+10, 193, 4)


            for card in self.cards:
                card.draw()

            # UI
            self.b_submit.draw()
            xpos = utils.align_text(utils.WIDTH/2, f"Pontos: {self.player_sum}")
            pyxel.text(xpos, 16, f"PONTOS: {self.player_sum}", 7)

            pyxel.text(19, 5,  f"TEMPO: {(self.timer//60):02d}:{(self.timer%60):02d}", 7)
            pyxel.text(20, 16, f"PESO: {self.player_weight}/{self.max_weight}", 7)


            if self.b_submit.is_on:
                self.b_end.draw()

                ans = f"RESPOSTA: {self.solution}"
                xpos = utils.align_text(utils.WIDTH/2, ans)
                pyxel.text(xpos, 5, ans, 10)

                if self.player_sum == self.solution:
                    pyxel.text(utils.align_text(utils.WIDTH/2, "PARABENS! VOCE VENCEU!"), utils.HEIGHT-10, "PARABENS! VOCE VENCEU!", 7)
                    xpos = utils.align_text(utils.WIDTH/2, f"Pontos: {self.player_sum}")
                    pyxel.text(xpos, 16, f"PONTOS: {self.player_sum}", 10)
                elif self.player_sum == 0:
                    pyxel.text(utils.align_text(utils.WIDTH/2, "TENTE CLICAR NAS CARTAS DA PROXIMA VEZ"), utils.HEIGHT-10, "TENTE CLICAR NAS CARTAS DA PROXIMA VEZ", 7)
                else:
                    pyxel.text(utils.align_text(utils.WIDTH/2, "QUEM SABE NA PROXIMA..."), utils.HEIGHT-10, "QUEM SABE NA PROXIMA...", 7)


        elif self.gamestate == "overflow":
            pyxel.text(utils.align_text(utils.WIDTH/2, "TOME CUIDADO COM O PESO DA PROXIMA VEZ!"), utils.HEIGHT-10, "TOME CUIDADO COM O PESO DA PROXIMA VEZ!", 7)
            self.b_end.draw()

            pyxel.blt(utils.WIDTH/2-32, 0, 0, 0, 64, 64, 90, 0)
            pyxel.blt(utils.WIDTH/2-32, 50, 0, 0, 16, 64, 48, 0)
        
Game()