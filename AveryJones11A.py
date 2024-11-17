# A program that deals a poker hand of 5 cards then prompts the user to select cards to replace

import random

class Deck():

    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]

# Establish card ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

my_deck = Deck(52)
hand = [my_deck.deal() for _ in range(5)]

print('Initial Hand:')
for card in hand:
    r = card % 13
    s = card // 13
    print(ranks[r], 'of', suits[s])
print()

# Prompt user to select cards to replace
cards_to_replace = input("\nEnter the positions of the cards you want to replace (comma separated, e.g., 1, 3): ")

# Parse(analyze) the input
cards_to_replace = [int(x.strip()) - 1 for x in cards_to_replace.split(',')]  # Convert to 0-based index

# Replace the cards
for i in cards_to_replace:
    new_card = my_deck.deal()
    hand[i] = new_card

# Display the new hand after replacing cards
print("\nNew hand after drawing:")
for card in hand:
    r = card % 13
    s = card // 13
    print(ranks[r], 'of', suits[s])