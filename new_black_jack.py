from class_render import Deck
from class_render import Card
from class_render import Player
from class_render import Dealer
from class_render import PlayBoard
import turtle
#wn = turtle.Screen()
#wn.bgcolor("green")
#wn.setup(800, 600)
#wn.title("Play Board")


deck = Deck()
deck.shuffle()
play_board = PlayBoard()
dealer = Dealer("Dealer", play_board)
player = Player("Player", play_board)
player.add_card(deck.deal_one())
player.add_card(deck.deal_one())
dealer.add_card(deck.deal_one())
dealer.add_card(deck.deal_one())

while not player.has_lost():
    player.show_hand()
    choice = input("Do you want to hit? (y/n): ")

    if choice == 'y':
        player.add_card(deck.deal_one())
    else:
        break

if player.has_lost():
    print(f"Player got over 21 and lost!")
else:
   dealer.show_hand()
   while dealer.calculate_hand_value() <= player.calculate_hand_value():
        dealer.add_card(deck.deal_one())
        dealer.show_hand()
        print("Hello")
   if dealer.calculate_hand_value() == 21:
        print("Dealer got Black Jack!")
   elif dealer.calculate_hand_value() > 21:
        print(f"Dealer got {dealer.calculate_hand_value()} and lost!")
   else:
        if dealer.calculate_hand_value() > player.calculate_hand_value() and dealer.calculate_hand_value() <= 21:
            print(f"{dealer.calculate_hand_value()} > {player.calculate_hand_value()} dealer wins!")
        elif player.calculate_hand_value() > dealer.calculate_hand_value() and player.calculate_hand_value() <= 21:
            print(f"{player.calculate_hand_value()} > {dealer.calculate_hand_value()} player wins!")


