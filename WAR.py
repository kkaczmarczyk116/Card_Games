import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value =values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
        
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()
    
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return('Player {} has {len(self.all_cards)} cards'.format(self.name))
    
p1 = Player("One")
p2 = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    p1.add_cards(new_deck.deal_one())
    p2.add_cards(new_deck.deal_one())
     
game_on = True

round_num = 0

#game_on = True

round_num = 0
while game_on:
    round_num += 1
    print("It is round {}".format(round_num))



    if len(p1.all_cards) == 0:
        
        print("Player Two Wins")
        game_on = False
    if len(p2.all_cards) == 0:
        print("Player One Wins")
        game_on = False

    try:

        p1_cards =[]
        p1_cards.append(p1.remove_one())
        p2_cards = []
        p2_cards.append(p2.remove_one())
    except:
        continue

    
    
    war_on = True
    while war_on:
        if p1_cards[-1].value > p2_cards[-1].value:
            p1.add_cards(p1_cards)
            p1.add_cards(p2_cards)
            print("Player 1 takes cards")

            war_on = False
            break
            

        elif p1_cards[-1].value < p2_cards[-1].value:
            p2.add_cards(p1_cards)
            p2.add_cards(p2_cards)
            print("Player 2 takes cards")
            war_on =False
            break
            
        else:
            print("WAR")
            if len(p1.all_cards) < 5:
                print("Player One does not have enough cards")
                print("Player Two Wins")
                game_on = False
                break 
            elif len(p2.all_cards) < 5:
                print("Player Two does not have enough cards")
                print("Player One Wins")
                game_on = False
                break 
            else:
                for num in range(5):
                    p1_cards.append(p1.remove_one())
                    p2_cards.append(p2.remove_one())            

