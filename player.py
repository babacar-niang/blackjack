import random

class Player:
    def __init__(self, label):
        self.label = label
        self.cards = []
        self.stop = False

    def get_move(self):
        pass

    def get_total_cards_value(self):
        total = 0
        for i in self.cards:
            if i.state == 'faceup':
                total += i.value
        return total # Just give the total value of thhe list of card

class HumanPlayer(Player):
    def __init__(self, label):
        super().__init__(label)

    def get_move(self):
        action = ['hit', 'stand']
        move = ''
        while move not in action:
            move = input('>')
        if move == 'stand':
            self.stop = True
        return move
    
    def get_total_cards_value(self):
        return super().get_total_cards_value()

class Bank(Player):
    def __init__(self, label):
        super().__init__(label)

    def get_move(self):
        if self.get_total_cards_value() >= 17:
            self.stop = True
            return 'stand'
        else:
            return 'hit'

    def get_total_cards_value(self):
        return super().get_total_cards_value()