########################################################################
##
## CS 101 Lab
## Program 5
## Daylan Quinn
## drq9q7@mail.umkc.edu
##
## PROBLEM : Fix functions to pass unit testing
##
## ALGORITHM : 
##      1. fix functions one by one
##      2. Get information for slot game
##      3. Use information to allow slot game to run
## 
## ERROR HANDLING:
##      None. Should be handled.
##
## OTHER COMMENTS:
##      NONE
##
########################################################################

import random


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''

    #LOOPS UNTIL PROPER INPUT
    play = input("Do you want to play again? --> ").upper()
    while True:
            
        if (play == 'Y') or (play == "YES"):
            return True
        if (play == 'N') or (play == "NO"):
            return False
            
        else:
            print("You must enter Y/YES/N/NO to continue. Please try again")
            play = input("Do you want to play again? --> ").upper()

     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''

    #LOOPS UNTIL PROPER WAGER INPUT
    chips = int(input("How many chips would you like to wager? --> "))

    while True:

        if (chips < 0):
            print("Try again. Must be greater than 0.")
            chips = int(input("How many chips would you like to wager? --> "))

        if (chips > bank):
            print("Try again. Must be less than or equal to the bank")
            chips = int(input("How many chips would you like to wager? --> "))

        if (chips > 0) and (chips <= bank):
            return chips
        

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''

    #USES RANDOM TO GET 3 RANDOM INTEGERS AND PLACE IN TUPLE
    num_1 = random.randint(0, 11)
    num_2 = random.randint(0, 11)
    num_3 = random.randint(0, 11)

    numbers = (num_1, num_2, num_3)

    return numbers


def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

    #CHECKS FOR NUMBER OF MATCHES
    total = 0
    if (reela == reelb) or (reela == reelc) or (reelb == reelc):
        total = 2
    if (reela == reelb) and (reelb == reelc):
        total = 3

    return total


def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''

    #LOOPS UNTIL TOLERABLE BANK INPUT
    bank = int(input("How many chips would you like to start with? --> "))

    while True:

        if (bank < 0):
            print("Try again. Must be greater than 0.")
            chips = int(input("How many chips would you like to start with? --> "))

        if (bank >= 101):
            print("Try again. Must be less than 101")
            chips = int(input("How many chips would you like to start with? --> "))

        if (bank > 0) and (bank < 101):
            return bank


def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 5 times the wager if 2 match, and negative wager if 0 match '''

    #GETS CORRESPONDING PAYOUT FOR WAGER AND NUMBER OF MATCHES
    if (matches == 3):
        wager = (wager * 10) - wager  
    if (matches == 2):
        wager = (wager * 3) - wager  
    if (matches == 0):
        wager = wager * -1
        
    return wager     



if __name__ == "__main__":

    count = 0
    playing = True
    while playing:
        count += 1
        bank = get_bank()

        if bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", bank, "in", count, "spins")
        print("The most chips you had was", bank)
        playing = play_again()
