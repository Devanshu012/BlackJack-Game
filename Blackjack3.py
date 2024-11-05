import random
from blackjack_art import logo, loose, won, game_over, draw

# want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)
cards = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'K': 10, 'J': 10, 'Q': 10}

def draw_cards(how_many):
    drawn_cards = []
    for _ in range(how_many):
        drawn_cards.append(random.choice(list(cards.keys())))
    return drawn_cards

def calculate_score(inv_cards):
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

def compair(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return f'''You Went Over 21, \n {loose}'''

    elif user_score > 21:
        return f'''You Went Over 21, \n {loose}'''

    elif computer_score > 21:
        return f"Computer went over 21 , \n{won}"

    elif user_score > computer_score:
        return f'{won}'

    elif user_score < computer_score:
        return f'{loose}'

    elif user_score == computer_score:
        return f'{draw}'

play = input("\t\tWould you like to play a game of Blackjack? (Y/N)\n\t\t\t\t").lower() == "y"
while play:
    user_cards = []
    computer_cards = []

    user_cards.extend(draw_cards(2))
    computer_cards.extend(draw_cards(2))

    user_sum = calculate_score(user_cards)
    computer_sum = calculate_score(computer_cards)

    print(f"you have {user_cards} cards :::: and it's sum is = {calculate_score(user_cards)}")
    print(f"Computer has [{computer_cards[0]}] and one card is hidden :::: total sum is = {cards[computer_cards[0]]}")

    if user_sum == 21 and computer_sum != 21:
        print(f"It's Blackjack!!! \n {won}")
        play = False

    elif computer_sum == 21 and user_sum != 21:
        print(f"Computer got Blackjack!!! \n {loose}")
        play = False

    elif user_sum == 21 and computer_sum == 21:
        print(f"Both have Blackjack!!!  \n {draw}")
        play = False

    else:
        while user_sum < 21:
            hit_or_pass = input("Press 'H' to Hit (draw more cards) or 'P' to Pass (Stand): ").lower()
            if hit_or_pass == 'h':
                user_cards += draw_cards(1)
                user_sum = calculate_score(user_cards)
                print(f"You now have {user_cards} cards :::: and their sum is - {user_sum}")
            elif hit_or_pass == 'p':
                break
            else:
                print("Invalid input, please type 'H' or 'P'.")


        print(f"Computer Reveals 2nd card, now total cards are {computer_cards} ::::  total sum is - {calculate_score(computer_cards)}")

        nd = 3
        while computer_sum < 17:
            computer_cards += draw_cards(1)
            nd += 1
            print(f"Computer Reveals another card, now total cards are {computer_cards} ::::  total sum is - {calculate_score(computer_cards)}")
            computer_sum = calculate_score(computer_cards)

        result = compair(user_sum, computer_sum)

        print(result)
        play = False

    play = to_play_again = input('''\t\t\t\t\t\t\t\t\tWould you like to play again?
                                    press 'Y' to play again
                                    press any other to exit
                                    \n
                                          ''').lower() == "y"
    if play == True:
        print("\n"*100)


print(game_over)
