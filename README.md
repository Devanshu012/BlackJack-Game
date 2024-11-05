# BlackJack-Game

This is a simple command-line Blackjack game implemented in Python. Players can interactively play against the computer, with options to draw cards or stand based on their current hand.

Features:-
--> Simulates a Blackjack game between the player and computer.
--> Handles Ace values dynamically (Ace can be 1 or 11 depending on the total score).
--> Game includes win/loss/draw conditions based on standard Blackjack rules.
--> User-friendly interface with prompts to hit or pass, and computer logic to draw cards until its score is at least 17.

Getting Started
--> Prerequisites
      -> To run the game, ensure you have Python installed on your system.
          1.) Clone this repository:
          2.) Ensure you have the necessary files:
                  blackjack_art.py (contains the ASCII art for the game)
                  blackjack.py (the main game logic)

--> Rules
      --> The goal of Blackjack is to have a hand value as close to 21 as possible, without going over.
      --> Face cards (King, Queen, Jack) are worth 10 points. The Ace can be worth either 1 or 11 points.
      --> Players can draw cards (Hit) or stand with their current hand (Pass).
      --> The computer will keep drawing cards until it reaches a hand value of at least 17.
      --> If either the player or computer exceeds 21, they lose.
