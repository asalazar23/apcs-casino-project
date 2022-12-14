from blackjack_code import *
def introduction():
  pick_a_game = input("Hello! Welcome to the -- Casino! Please select a game from the following list: Blackjack, Roullette, Craps. To return to this menu, type 'home.'")
  if pick_a_game == "Blackjack" or "blackjack":
    blackjack()