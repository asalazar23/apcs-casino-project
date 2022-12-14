def blackjack():
  import random 
  import math
  print("----------")
  print("Welcome to Blackjack! Payout is 3:2. Dealer must stand on 17.")
  #will tell the player whats in their hand
  def hand(args):


  #this will be the dealers hand
    def dealer_hand():
      cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      dealer_card1 = random.choice(cards)
      dealer_card2 = random.choice(cards)
      print(f"{dealer_card1} + {dealer_card2}")
  #deal first 2 cards
  def blk_deal_cards():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    pick_card1 = random.choice(cards)
    pick_card2 = random.choice(cards)
    print(f"You have been dealt {str(pick_card1)} and {str(pick_card2)}")
    


  #this will ask the player what they want to do for their turn
  def blk_turn():
    
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hit = random.choice(cards)
    decision = input("Would you like to hit, stand, or fold?")
    if decision == "Hit" or "hit":
      print(f"Your new card is {hit}. Your hand contains {hand}")
    elif decision == "Stand" or "stand":
      # print(f"You stood on {hand}. The dealer had {dealer_hand()}.")
  # def payout():
  #   if player_hand > dealer_hand and =< 21:
  #     blk_winnings = blk_bet * 1.5
  #     print(f"You have won {blk_winnings}")
  #   elif player_hand
  def blk_gameplay():
    blk_bet = int(input("Please place your bet: $"))
    blk_deal_cards()
    blk_turn()
    
  blk_gameplay()
    
    
    
    
