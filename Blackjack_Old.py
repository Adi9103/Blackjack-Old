from random import shuffle 
import sys
import time

your_money =100
deck_of_cards = []
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
for x in range(4):
    deck_of_cards+=cards
shuffle(deck_of_cards)    
    
def next_card():
    card = deck_of_cards[0]
    deck_of_cards.pop(0)
    return card
    
def blackjack():
    global your_money
    deck_of_cards.pop(0)
    launch = str(input("Welcome to Blackjack. You have {} dollars. Press ENTER to play ".format(your_money)))
    bet = (input("How much do you want to bet? "))
    bet =int(bet)
    if bet<=your_money:
        print ("You have {} dollars. You bet {}.".format(your_money-bet, bet))
    elif bet>your_money:
        print ("You don't have enough money to bet that much") 
        bet = (input("How much do you want to bet?"))
        bet =int(bet)
    your_cards=[]
    your_cards.append(next_card())
    dealer_cards=[]
    dealer_cards.append(next_card())
    your_cards.append(next_card())
    dealer_cards.append(next_card())
    print (str(your_cards) + " For a total of " + str(sum(your_cards)) + ". The dealer has a " + str(dealer_cards[1]))
    decision=input("If you want to take another card, enter A. If you want to stay, enter B. If you want to end the game, enter C")
    while decision == "A":
        your_cards.append(next_card())
        print ("You have " + str(your_cards) + ". For a total of " + str(sum(your_cards)) + ". The dealer has a " + str(dealer_cards[1]))
        if sum(your_cards)>21:
            break
        decision=input("If you want to take another card, enter A. If you want to stay, enter B. If you want to end the game, enter C")
    print ("Dealer's Turn!")
    while sum(dealer_cards)<17:
        yourWords = "Thinking..."
        for char in yourWords:
            sys.stdout.write(char)
        time.sleep(0.1)
        dealer_cards.append(next_card())
        print ("You have " + str(your_cards) + ". For a total of " + str(sum(your_cards)) + ". The dealer has " + str(dealer_cards[1]) + " and " + str(dealer_cards[2]) + ".")
    if sum(your_cards) > 21:
            print ("Bust! Dealer wins.")
            print ("Dealer's Cards: " + str(dealer_cards) + ". Total = " + str(sum(dealer_cards)))
            print ("Your Cards: " + str(your_cards) + ". Total = " + str(sum(your_cards)))
            print ("You have " + str(your_money) + " dollars. " + "You lost " + str(bet) + " dollars.")
            your_money-=bet
    else: 
        if sum(dealer_cards) > 21:			   
            print ("Dealer busts. You win!")
            print ("Dealer's Cards: " + str(dealer_cards) + ". Total = " + str(sum(dealer_cards)))
            print ("Your Cards: " + str(your_cards) + ". Total = " + str(sum(your_cards)))
            print ("You have " + str(your_money) + " dollars. " + "You won " + str(bet) + " dollars.")
            your_money+=bet   
        else:
            if (sum(your_cards) > sum(dealer_cards)):
                print ("Congratulations. Your score is higher than the dealer. You win")
                print ("Dealer's Cards: " + str(dealer_cards) + ". Total = " + str(sum(dealer_cards)))
                print ("Your Cards: " + str(your_cards) + ". Total = " + str(sum(your_cards)))
                print ("You have " + str(your_money) + " dollars. " + "You won " + str(bet) + " dollars.") 
                your_money+=bet
            if sum(your_cards) < sum(dealer_cards):
                print ("Sorry. Your score isn't higher than the dealer. You lose.")
                print ("Dealer's Cards: " + str(dealer_cards) + ". Total = " + str(sum(dealer_cards)))
                print ("Your Cards: " + str(your_cards) + ". Total = " + str(sum(your_cards)))
                print ("You have " + str(your_money) + " dollars. " + "You lost " + str(bet) + " dollars.")
            your_money-=bet
            if sum(dealer_cards) == 21:
                print ("Sorry, the dealer won.")
                print ("Dealer's Cards: " + str(dealer_cards) + ". Total = " + str(sum(dealer_cards)))
                print ("Your Cards: " + str(your_cards) + ". Total = " + str(sum(your_cards)))
                print ("You have " + str(your_money) + " dollars. " + "You lost " + str(bet) + " dollars.")
                your_money+=bet
    if decision == "B":
        pass
    if decision == "C":
        sys.exit()
    newgame=input('Do you want to play again? Enter "Yes" or "No"')
    if newgame == "Yes":
        blackjack()
    elif decision == "No":
        sys.exit()

blackjack()
