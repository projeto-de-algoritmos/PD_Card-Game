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
        self.sorted_cards = []
        deck, self.weight = utils.fill_deck(self.num_cards)

        self.player_sum = 0
        self.player_weight = 0

        for i in range(self.num_cards):
            self.cards.append(Card(deck[i][0],deck[i][1], 14+33*(i%7), 35+55*(i//7)))

        self.sorted_cards = deck.copy()
        self.sorted_cards.sort(key=lambda x: (x[0], x[1]))

        # print(self.cards)
        # print(" ")
        # print(self.sorted_cards)

        
        
        # self.bstart = bt.CircleButton(130, 130, "start", 20)
        self.bsubmit = bt.RectButton(utils.WIDTH-40, 20, "CONFIRMAR", 50, 12)

        pyxel.run(self.update, self.draw)

    def update(self):

        if self.gamestate == "game":
            for card in self.cards:
                if card.update() == 1:
                    self.player_sum += card.value
                    self.player_weight += card.face
            self.bsubmit.update()
            if self.bsubmit.is_on:

                w_list = []
                v_list = []
                for card in self.sorted_cards:
                    w_list.append(card[0])
                    v_list.append(int((card[0]**1.5)+card[1]))

                print(w_list)
                print(v_list)

                knap_table = utils.knapsack(self.weight, w_list, v_list, self.num_cards)
                answer = f"RESPOSTA: {knap_table[self.num_cards][self.weight]}"
                cards_ans = utils.solution_knapsack(knap_table, w_list, self.num_cards, self.weight)
                print(answer)
                for card in cards_ans:
                    print(self.sorted_cards[card])
                # print(cards_ans)
                self.bsubmit.is_on = False

    def draw(self):
        pyxel.cls(0)


        pyxel.text(20, 16, f"Pontos: {self.player_sum}", 7)
        pyxel.text(108, 16, f"Peso: {self.player_weight}/{self.weight}", 7)

        if self.gamestate == "game":
            self.bsubmit.draw()
            for card in self.cards:
                card.draw()
        
Game()