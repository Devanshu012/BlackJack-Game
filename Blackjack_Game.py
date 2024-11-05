import random
from blackjack_art import logo

# want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)
cards = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'K': 10, 'J': 10, 'Q': 10}


def draw_cards(how_many):
    drawn_cards = []
    for i in range(how_many):
        drawn_cards.append(random.choice(list(cards.keys())))
    return drawn_cards

def sum_of_values(inv_cards):
    total_sum = 0
    ace_count = 0
    for i in inv_cards:
        total_sum += cards[i]
        if i == 'Ace':
            ace_count += 1

    while total_sum > 21 and ace_count > 0:
        total_sum -= 10
        ace_count -= 1
    return total_sum




play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n").lower() == 'y'
while play:
    player_cards = []
    computer_cards = []
    if len(player_cards) < 2 or len(computer_cards) < 2:
        player_cards += draw_cards(2)
        computer_cards += draw_cards(2)
        print(f"You have {player_cards} :::: Sum = {sum_of_values(player_cards)}")
        print(f"Computer have {computer_cards[0]} and a hidden card :::: Sum = {cards[computer_cards[0]]}")

        if sum_of_values(player_cards) == 21:
            print("BLACKJACK! YOU WON!")
            play = False
            break
        elif sum_of_values((computer_cards)) == 21:
            print(f"Computer has {computer_cards} : Sum = {sum_of_values(computer_cards)}")
            print("Computer got Blackjack. YOU LOSE!")
            play = False
            break

    player_sum = sum_of_values(player_cards)

    if player_sum > 21:
        if 'Ace' in player_cards:
            cards['Ace'] = 1
            player_sum = sum_of_values(player_cards)
            if player_sum > 21:
                print("YOU LOOSE")
    while player_sum <= 21:
        hit_or_pass = input("Type 'H' for hit and 'P' for pass:\n").lower()
        if hit_or_pass == 'h':
            player_cards += draw_cards(1)
            player_sum = sum_of_values(player_cards)
            print(f"You have {player_cards} : Sum = {player_sum}")
            if player_sum > 21:
                print("You went over 21! YOU LOSE!")
                play = False
                break
        elif hit_or_pass == 'p':
            break
        else:
            print("Please Type correctly")

    if not play:
            break

    # Computer's turn - reveal hidden card
    print(f"Computer reveals {computer_cards} : Sum = {sum_of_values(computer_cards)}")
    computer_sum = sum_of_values(computer_cards)

    while computer_sum < 17:
        computer_cards += draw_cards(1)
        computer_sum = sum_of_values(computer_cards)
        print(f"Computer draws a card: {computer_cards} : Sum = {computer_sum}")

    if computer_sum > 21:
        print("Computer went over 21! YOU WON!")
    elif player_sum > computer_sum:
        print("YOU WON")
    elif player_sum < computer_sum:
        print("YOU LOOSE")
    else:
        print("It's a DRAW!!")

    play_again = input("Play again? Type 'Y' for yes or any other key to exit: ").lower()
    if play_again == 'y':
        print("\n" * 100)
    else:
        play = False

print("Game Has Been Over!!")


