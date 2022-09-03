# At the beginning of the game all two players has an empty list of cards at each turn if he hit then we generate
# a card with a random type (an int between 0 and 12) and a random suit (an int between 0 and 3)
# Then we add it to the list of card of the player 
# For the suits 0: for heart, 1: for diamond, 2: for spade, 3: for club
# For types is contains in ['A', 1-10, 'K', 'Q', 'J']
from random import choice
from player import HumanPlayer, Bank
import time

class Card:
    def __init__(self, suit, type, state='faceup'):
        self.suit = suit
        # self.suits = [chr(9829), chr(9830), chr(9824), chr(9827)]  Respectively '♥', '♦', '♠', '♣'
        # self.types = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J']
        self.type = type
        self.state = state
        if type in range(2,11):
            self.value = type
        elif type == 'A':
            self.value = 1
        else:
            self.value = 10

    def display_cards(self):
        row = ['', '', '', '']
        if self.state == 'facedown':
            row[0] = ' ___'
            row[1] = '|## |'
            row[2] = '|###|'
            row[3] = '|_##|'
        else:
            row[0] = ' ___'
            row[1] = '|{}  |'.format(self.type)
            row[2] = '| {} |'.format(self.suit)
            row[3] = '|__{}|'.format(self.type)

        return row

# Have to get the first row of every card
def print_cards(player):
    rows0 = [player.cards[i].display_cards()[0] for i in range(len(player.cards))]
    rows1 = [player.cards[i].display_cards()[1] for i in range(len(player.cards))]
    rows2 = [player.cards[i].display_cards()[2] for i in range(len(player.cards))]
    rows3 = [player.cards[i].display_cards()[3] for i in range(len(player.cards))]
    print('  '.join(rows0))
    print('  '.join(rows1))
    print('  '.join(rows2))
    print('  '.join(rows3))


def play(bank, player):
    suits = [chr(9829), chr(9830), chr(9824), chr(9827)]
    types = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J']
    c1_bank = Card(choice(suits), choice(types), state='facedown')
    c2_bank = Card(choice(suits), choice(types), state='faceup')
    bank.cards.append(c1_bank)
    bank.cards.append(c2_bank)
    c1_human = Card(choice(suits), choice(types), state='faceup')
    c2_human = Card(choice(suits), choice(types), state='faceup')
    player.cards.append(c1_human)
    player.cards.append(c2_human)
    while player.stop == False:
        print(f'{bank.label} :\n Total cards value: {bank.get_total_cards_value()}')
        print_cards(bank)
        print('')
        print(f'{player.label} :\n Total cards value: {player.get_total_cards_value()}')
        print_cards(player)
        print('')
        move = ''
        while move not in ['hit', 'h', 'H','stand', 's', 'S']:
            move = player.get_move()
        if move in ['hit', 'h', 'H']:
            rand_card = Card(choice(suits), choice(types), state='faceup')
            player.cards.append(rand_card)
            if player.get_total_cards_value() > 21:
                break

    c1_bank.state = 'faceup'
    if player.get_total_cards_value() > 21:
        print(f"{bank.label}:\nTotal cards value: {bank.get_total_cards_value()}")
        print_cards(bank)
        print('')
        print(f'{player.label}:\nTotal cards value: {player.get_total_cards_value()}')
        print_cards(player)
        print('')
        print(f"{player.label} you have lost")
        return bank.label
    elif player.get_total_cards_value() == 21:
        print(f"{bank.label}:\nTotal cards value: {bank.get_total_cards_value()}")
        print_cards(bank)
        print('')
        print(f'{player.label}:\nTotal cards value: {player.get_total_cards_value()}')
        print_cards(player)
        print('')
        print('Blackjack!!! {player.label} has won')
        return player.label


    while bank.stop == False:
        time.sleep(.8)
        print(f'{bank.label} :\n Total cards value: {bank.get_total_cards_value()}')
        print_cards(bank)
        print('')
        print(f'{player.label} :\n Total cards value: {player.get_total_cards_value()}')
        print_cards(player)
        move = ''
        while move not in ['hit', 'h', 'H','stand', 's', 'S']:
            move = bank.get_move()
        if move in ['hit', 'h', 'H']:
            rand_card = Card(choice(suits), choice(types), state='faceup')
            bank.cards.append(rand_card)   

    if bank.get_total_cards_value() > 21:
        print(f"{bank.label}:\nTotal cards value: {bank.get_total_cards_value()}")
        print_cards(bank)
        print('')
        print(f'{player.label}:\nTotal cards value: {player.get_total_cards_value()}')
        print_cards(player)
        print('')
        print(f'{bank.label} busted, {player.label} has won')
        return player.label
    elif bank.get_total_cards_value() == 21:
        print(f"{bank.label}:\nTotal cards value: {bank.get_total_cards_value()}")
        print_cards(bank)
        print('')
        print(f'{player.label}:\nTotal cards value: {player.get_total_cards_value()}')
        print_cards(player)
        print('')
        print(f'Blackjack!! {bank.label} has won')
        return bank.label
    elif bank.get_total_cards_value() > player.get_total_cards_value():
        print(f"{bank.label}:\nTotal cards value: {bank.get_total_cards_value()}")
        print_cards(bank)
        print('')
        print(f'{player.label}:\nTotal cards value: {player.get_total_cards_value()}')
        print_cards(player)
        print('')
        print(f'{bank.label} won !!')
        return bank.label
    elif bank.get_total_cards_value() < player.get_total_cards_value():
        print(f"{bank.label}:\nTotal cards value: {bank.get_total_cards_value()}")
        print_cards(bank)
        print('')
        print(f'{player.label}:\nTotal cards value: {player.get_total_cards_value()}')
        print_cards(player)
        print('')
        print(f'{player.label} has won!!')
        return player.label
    else:
        print(f"{bank.label}:\nTotal cards value: {bank.get_total_cards_value()}")
        print_cards(bank)
        print('')
        print(f'{player.label}:\nTotal cards value: {player.get_total_cards_value()}')
        print_cards(player)
        print('')
        print("It's a tie!!!")
        return 0

def main():
    response = 'yes'
    while response == 'yes':
        player = HumanPlayer('human')
        computer = Bank('bank')
        play(computer,player)
        response = input('Do you wanna play again (yes/no): ')

    print("Goodbye!!")


if __name__ == '__main__':
    main()