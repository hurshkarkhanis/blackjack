from blackjack import BlackjackClass
import time

import pprint

pp = pprint.PrettyPrinter(indent=4)

game = BlackjackClass()

print()
game.create_deck()
print('shuffling deck...', '\n')
game.shuffle()
time.sleep(2)

print('ready to play.')

game.first_deal()
game.show_hands()

game.play_game()





    