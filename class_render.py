
import random
from tkinter import SEL
suits = ('\u2665', '\u2666', '\u2660', '\u2663')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':[1,11]}
import turtle
wn = turtle.Screen()
wn.bgcolor("green")
wn.setup(800, 600)
wn.title("Play Board")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

class Card:
    #Creating cards
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        self.values= values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
    #Rendering cards
    def render(self, x, y, pen):
        pen.penup()
        pen.goto(x, y)
        pen.color("black")
        pen.goto(x-100, y+250)
        pen.pendown()
        pen.goto(x-50, y+250)
        pen.goto(x-50, y+175)
        pen.goto(x-100, y+175)
        pen.goto(x-100, y+250)
        pen.penup()
        #Draw rank in the top corner
        pen.color("white")
        pen.goto(x-96, y+232)
        pen.pendown()
        pen.write(self.rank, False, font =("Courier New", 13, "normal"))
        pen.penup()
        pen.goto(x-96, y+218)
        pen.pendown()
        pen.write(self.suit, False, font =("Courier New", 13, "normal"))
        pen.penup()
        #Draw suit in the middle
        pen.goto(x-82, y+195)
        pen.pendown()
        pen.write(self.suit, False, font =("Courier New", 25, "normal"))
        pen.penup()

class PlayBoard:
    def __init__(self):
        self.card_positions = {
            "Player": (-200, -200),  
            "Dealer": (-200, 200),  
        }
        self.hand_positions = {
            "Player": (+46, -438),  
            "Dealer": (-0, 0),  
        }
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

    def render_card(self, player_name, card):
        position = self.hand_positions[player_name]
        x, y = position[0], position[1]
        card.render(x, y, self.pen)
        self.hand_positions[player_name] = (x + 55, y)  

    def render_hand(self, player_name, hand):
        position = self.card_positions[player_name]
        x, y = position[0], position[1]
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.write(f"{player_name}'s hand:", False, font=("Courier New", 13, "normal"))
        self.pen.penup()
        y -= 30
        for card in hand:
            self.pen.goto(x, y)
            self.pen.pendown()
            self.pen.write(str(card), False, font=("Courier New", 13, "normal"))
            self.pen.penup()
            y -= 20
            
class Deck:
    #Creating deck
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    #Deck shuffle
    def shuffle(self):
        random.shuffle(self.all_cards)
    #Grabbing one card
    def deal_one(self):
        return self.all_cards.pop()


class Player:
    #Creating Player
    def __init__(self, name,play_board):
        self.name = name
        self.hand  = []
        self.play_board = play_board

    def add_card(self, card):
        self.hand.append(card)
        self.play_board.render_card(self.name, card) #working
        #self.hand.render_card(self.name, card)

    def show_hand(self):
        self.play_board.render_hand(self.name, self.hand)
        print(f"{self.name}'s hand value {self.calculate_hand_value()}:")
        for card in self.hand:
            print(f"{card}, card value: {card.values}")
        #self.play_board.render_card(self.name, card)

    def calculate_hand_value(self):
        hand_value = 0
        num_aces = 0

        for card in self.hand:
            if card.rank == 'Ace':
                num_aces += 1
            else:
                hand_value += card.values

        for _ in range(num_aces):
            if hand_value + values['Ace'][1] <= 21:
                hand_value += values['Ace'][1]
            else:
                hand_value += values['Ace'][0]

        return hand_value

    def has_lost(self):
        return self.calculate_hand_value() > 21

class Dealer:
    #Creating dealer
    def __init__(self, name, play_board):
        self.name = name
        self.hand = []
        self.play_board = play_board

    def add_card(self, card):
        self.hand.append(card)
        self.play_board.render_card(self.name, card)

    def show_hand(self,):
        #self.play_board.render_card(self.name, card)
        self.play_board.render_hand(self.name, self.hand)
        print(f"Dealer's hand value {self.calculate_hand_value()}:")
        for card in self.hand:
            print(f"{card}, card value: {card.values}")

    def calculate_hand_value(self):
        hand_value = 0
        num_aces = 0

        for card in self.hand:
            if card.rank == 'Ace':
                num_aces += 1
            else:
                hand_value += card.values

        for _ in range(num_aces):
            if hand_value + values['Ace'][1] <= 21:
                hand_value += values['Ace'][1]
            else:
                hand_value += values['Ace'][0]

        return hand_value

    def has_lost(self):
        return self.calculate_hand_value() > 21









