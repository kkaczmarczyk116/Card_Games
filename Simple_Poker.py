import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

playing = True
class Card:
    def __init__(self,rank,suit):
        self.rank =rank
        self.suit = suit
        self.value =values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit 

class Hand:
    def __init__(self):
         self.cards = []
         self.value = 0
         self.aces = 0
    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces +=1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Deck:
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank,suit))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
    def __str__(self):
        comp = ""
        for card in self.deck:
            comp += '\n' + card.__str__()
        return "Deck has " + comp

class Chips:
    def __init__(self,amount):
        self.amount = amount
        self.bet = 0
    def win_bet(self):
        self.amount += self.bet
    
    def lost_bet(self):
        self.amount -= self.bet
    #def add_chips(self,more):
        #self.amount += more


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(" How many Chips would you like to bet "))
            print("\n")
        except:
            print("sorry, please provide number")
        else:
            if chips.bet > chips.amount:
                print("not enough. You have {} ".format(chips.amount))
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()

def hit_or_stay(deck,hand):
    global playing

    while True:
        x = input("Hit or Stay: Press H or S ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stays")
            playing = False
        else:
            print("Please Press H or S") 
            continue
        break

def show_some(player,dealer):
    print("Dealer's hand : \n")
    print("One Card Hidden")
    print(dealer.cards[1])
    print('\n')
    print("Player's hand :")
    print('\n')
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("Dealer's Hand :")
    
    for card in dealer.cards:
        print(card)
    #print("\n")
    print("Player's Cards: ")
    for card in player.cards:
        print(card)


def player_bust(player,dealer,chips):
    print("Player Busts")
    chips.lost_bet()
def player_wins(player,dealer,chips):
    print("player Wins")
    chips.win_bet()
def dealer_bust(player,dealer,chips):
    print("Dealer Busts")
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("Dealer Wins")
    chips.lost_bet()
def push(player,dealer):
    print("It's a Tie")


print("Welcome to Simple BlackJack"+ "\n" + "You have 1,000 chips. Use them wisely")
player_chips = Chips(1000)
while True:
    

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #player_chips = Chips(100)
    take_bet(player_chips)
    show_some(player_hand,dealer_hand)
 
    while playing:
        
        hit_or_stay(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_bust(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_bust(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    #player_chips.add_chips(player_chips.amount)
    print("\n Player total chips at {} ".format(player_chips.amount))
    if (player_chips.amount == 0):
        print("Sorry, no more money")
        break
    new_game = input("Would you want to play another hand? : y/n ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing")
        break


        


    
#test_deck = Deck()
#test_deck.shuffle()
#print(test_deck)
#p1 = Hand()
#sample_card = test_deck.deal()
#print(sample_card)
#p1.add_card(sample_card)
#print(p1.value)




