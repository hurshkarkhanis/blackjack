import random
import time

class BlackjackClass():

    def __init__(self):
        self.DECK = []
        self.dealer_hand = []
        self.player_hand = []
        
    def create_suit(self,suit_name):
        #make ace
        self.DECK.append(('ACE', suit_name)) #false = flipped down true = open
        #make 2-10
        for val in range(2, 11):
            self.DECK.append((val, suit_name))
        #make face cards
        self.DECK.append(('JACK', suit_name))
        self.DECK.append(('QUEEN', suit_name))
        self.DECK.append(('KING', suit_name))
        
    def create_deck(self):
        self.create_suit('♠')
        self.create_suit('♣')
        self.create_suit('♥')
        self.create_suit('♦')
    
    def shuffle(self):

        random.shuffle(self.DECK)

    def first_deal(self):
        self.dealer_hand.append(self.DECK.pop(0))
        self.dealer_hand.append('FACE DOWN')

        self.player_hand.append(self.DECK.pop(0))
        self.player_hand.append(self.DECK.pop(0))

    def show_hands(self):
        dealer_score = self.score(self.dealer_hand)
        player_score = self.score(self.player_hand)
        print()
        print('DEALER HAND: ', self.dealer_hand, 'SCORE: ', dealer_score)
        print('PLAYER HAND: ', self.player_hand, 'SCORE: ', player_score)
        print()

    def score(self, hand):
        current_score = 0
        for card in hand:
            #face
            if card[0] == 'JACK' or card[0] == 'QUEEN' or card[0] == 'KING':
               current_score += 10
            #ace
            elif card[0] == 'ACE':
                    if (current_score + 11) > 21:
                       current_score += 1
                    else:
                       current_score += 11
            elif card == 'FACE DOWN':
                pass
            #numbers
            else:
               current_score += card[0]
            if current_score < 21 and 'ACE' in hand:
                current_score -= 10
        return current_score

    def hit(self, who):
        if who == 'player':
            self.player_hand.append(self.DECK.pop())
            self.show_hands()
        elif who == 'dealer':
            self.dealer_hand.append(self.DECK.pop())
            self.show_hands()

    def play_game(self):
        game_on = True
        while game_on:
            action = input('press ENTER to hit or x to stand: ')
            if action == "":
                time.sleep(2)
                self.hit('player')
                if self.score(self.player_hand) > 21:
                    print('BUST! DEALER WINS')
                    game_on = False
            elif action == "x":
                del self.dealer_hand[-1]
                time.sleep(2)
                while self.score(self.dealer_hand) < self.score(self.player_hand):
                    self.hit('dealer')
                    if self.score(self.dealer_hand) == self.score(self.player_hand) and self.score(self.player_hand) == 21 :
                        time.sleep(1)
                        print("PUSH. GAME TIED")
                        game_on = False
                    if self.score(self.dealer_hand) == self.score(self.player_hand):
                        time.sleep(1)
                        print("PUSH. GAME TIED")
                        game_on = False
                    if self.score(self.dealer_hand) == 21 and self.score(self.player_hand) != 21:
                        time.sleep(1)        
                        print('**BLACKJACK** DEALER WINS')
                        game_on = False
                    if self.score(self.dealer_hand) <=self.score(self.player_hand):
                        time.sleep(1)
                        self.hit('dealer')
                    if self.score(self.dealer_hand) >self.score(self.player_hand) and self.score(self.dealer_hand) < 21:
                        time.sleep(1) 
                        print('DEALER WINS')
                        game_on = False
                    if self.score(self.dealer_hand) > self.score(self.player_hand) and self.score(self.dealer_hand) > 21:
                        time.sleep(1)
                        print('BUST! PLAYER WINS')
                        game_on = False
                    if self.score(self.dealer_hand) > self.score(self.player_hand) and self.score(self.dealer_hand) == 21:
                        time.sleep(1)
                        print('**BLACKJACK** DEALER WINS')
                        game_on = False
                    
                    '''
                    DEALER HIT
                    IF DEALER BLACK JACK AND PLAYER BLACK JACK
                        PUSH
                    IF DEALER BLACK JACK AND PLAYER NOT BLACK JACK
                        DEALER WIN - BLACKJACK   
                    IF DEALER BELOW OR EQUAL TO PLAYER
                        DEALER HIT
                    IF DEALER ABOVE PLAYER AND UNDER 21
                        DEALER WIN
                    IF: DEALER ABOVE PLAYER AND OVER 21:
                        DEALER LOSE
                    IF: DEALER ABOVE PLAYER AND EQUAL TO 21
                        DEALER WIN - BLACKJACK   

                    '''



            



            
