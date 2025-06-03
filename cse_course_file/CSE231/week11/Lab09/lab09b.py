import cards_B as cards  # Import the cards_B.py module so that you can use it in your code

# Create the deck of cards
the_deck = cards.Deck()
the_deck.shuffle()

# Initialize player hands
player1_list = []
player2_list = []

# Deal 5 cards to each player
for _ in range(5):
    player1_list.append(the_deck.deal())
    player2_list.append(the_deck.deal())

# Display starting hands
print("Starting Hands")
print("Hand1:", player1_list)
print("Hand2:", player2_list)

# Main game loop
first_round = True
while player1_list and player2_list:
    # Display prompt to continue or stop
    if not first_round:
        p = input("\n:~Keep Going: (Nn) to stop~:")
        if p.lower() == "n":
            print("Player 2 wins!!!")
            break
    else:
        first_round = False

    # Draw the top card from each player's hand
    player1_card = player1_list.pop(0)
    player2_card = player2_list.pop(0)

    # Compare the ranks of the cards
    if player1_card.rank() > player2_card.rank():
        print("Battle was 1: {}, 2: {}. Player 1 wins battle.".format(player1_card, player2_card))
        player1_list.extend([player1_card, player2_card])  # Player 1 wins the cards
    elif player1_card.rank() < player2_card.rank():
        print("Battle was 1: {}, 2: {}. Player 2 wins battle.".format(player1_card, player2_card))
        player2_list.extend([player2_card, player1_card])  # Player 2 wins the cards
    else:
        print("Battle was 1: {}, 2: {}. Battle was a draw.".format(player1_card, player2_card))
        player1_list.append(player1_card)  # Each player takes back their card
        player2_list.append(player2_card)

    # Display the current hands
    print("hand1:", player1_list)
    print("hand2:", player2_list)

# Determine the winner
if not player1_list:
    print("Player 2 wins!!!")
elif not player2_list:
    print("Player 1 wins!!!")
