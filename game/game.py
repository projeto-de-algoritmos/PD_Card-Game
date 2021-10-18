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
        self.b_end = bt.CircleButton(utils.WIDTH/2, utils.HEIGHT/2+50, "MENU", 20)

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
                self.num_cards = random.randint(7, 14)

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
                self.gamestate = "game_over"



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

                    print(w_list)
                    print(v_list)

                    self.knap_table = utils.knapsack(self.max_weight, w_list, v_list, self.num_cards)
                    self.solution = self.knap_table[self.num_cards][self.max_weight]
                    cards_ans = utils.solution_knapsack(self.knap_table, w_list, self.num_cards, self.max_weight)
                    print(self.solution)
                    for card in cards_ans:
                        print(self.sorted_cards[card])

                self.b_end.update()
                if self.b_end.is_on:
                    self.b_end.is_on = False
                    
                    self.gamestate = "menu"

        elif self.gamestate == "game_over":
            self.b_end.update()

            if self.b_end.is_on:
                self.b_end.is_on = False
                
                self.gamestate = "menu"

    def draw(self):
        pyxel.cls(0)

        if self.gamestate == "menu":
            self.b_start.draw()

        elif self.gamestate == "game":

            for card in self.cards:
                card.draw()

            # UI
            self.b_submit.draw()
            pyxel.text(20, 16, f"Pontos: {self.player_sum}", 7)
            pyxel.text(108, 16, f"Peso: {self.player_weight}/{self.max_weight}", 7)

            if self.b_submit.is_on:
                self.b_end.draw()

                print(self.player_sum)
                print(self.solution)

                if self.player_sum == self.solution:
                    print("AAAAAAAAAAAA")
                    pyxel.text(utils.align_text(utils.WIDTH/2, "PARABENS! VOCE VENCEU!"), utils.HEIGHT-20, "PARABENS! VOCE VENCEU!", 7)
                elif self.player_sum == 0:
                    pyxel.text(utils.align_text(utils.WIDTH/2, "TENTE CLICAR NAS CARTAS DA PROXIMA VEZ"), utils.HEIGHT-20, "TENTE CLICAR NAS CARTAS DA PROXIMA VEZ", 7)
                else:
                    pyxel.text(utils.align_text(utils.WIDTH/2, "QUEM SABE NA PROXIMA..."), utils.HEIGHT-20, "QUEM SABE NA PROXIMA...", 7)


        elif self.gamestate == "game_over":
            self.b_end.draw()
        
Game()