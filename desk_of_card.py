import random 


class Cards: 
    def __init__(self, shape, val):
        self.shape = shape
        self.val = val
        self.shapes = {1:"Club", 2:"Diamond", 3:"Heart", 4:"Spade" }
        self.pip = {1: "Ace", 2: "Two", 3: "Three", 4:"Four", 5:"Five",6:"Six", 7: "Seven", 8: "Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
    
    
    def __str__(self):
        card = f"{self.pip[self.val]} {self.shapes[self.shape]}"
        return card

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()


    def create_deck (self):
        for s in range(1, 5):
            for c in range(1, 14):
                self.cards.append(Cards(s, c))


    def shuffle(self):
        random.shuffle(cards)
        
    
    def print_value(self): 
        for i in self.cards:
            print(i)



player1 = Deck()

player1.print_value()



