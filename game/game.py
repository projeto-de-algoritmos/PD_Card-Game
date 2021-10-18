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

        self.num_cards = 0
        self.max_weight = 0
        self.cards = []

        self.sorted_cards = []
        self.knap_table = []

        self.player_sum = 0
        self.player_weight = 0   
        
        self.b_start = bt.CircleButton(utils.WIDTH/2, utils.HEIGHT/2, "JOGAR!", 20)
        self.b_submit = bt.RectButton(utils.WIDTH-40, 20, "CONFIRMAR", 50, 12)
        self.b_end = bt.CircleButton(utils.WIDTH/2, utils.HEIGHT/2+92, "MENU", 20)

        pyxel.run(self.update, self.draw)

    def update(self):

        if self.gamestate == "menu":
            self.b_start.update()
            if self.b_start.is_on:
                self.b_start.is_on = False

                # cleaning variables
                self.num_cards = 0
                self.max_weight = 0
                self.solution = -1
                self.cards = []
                self.sorted_cards = []
                self.knap_table = []
                self.player_sum = 0
                self.player_weight = 0

                # filling variables
                self.num_cards = 21#random.randint(7, 14)

                deck = utils.fill_deck(self.num_cards)
                self.max_weight = utils.get_max_weight(deck)

                for i in range(self.num_cards):
                    self.cards.append(Card(deck[i][0],deck[i][1], 14+33*(i%7), 35+55*(i//7)))

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

                    # print(w_list)
                    # print(v_list)

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
            self.b_start.draw()

        elif self.gamestate == "game":

            pyxel.line(-10, 192, utils.WIDTH+10, 192, 7)

            for card in self.cards:
                card.draw()

            # UI
            self.b_submit.draw()
            xpos = utils.align_text(utils.WIDTH/2, f"Pontos: {self.player_sum}")
            pyxel.text(xpos, 16, f"PONTOS: {self.player_sum}", 7)
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
        
Game()