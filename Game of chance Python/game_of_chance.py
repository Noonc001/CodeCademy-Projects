import random

money = 100

#check money
if money <= 0:
  print("You do not have enough funds to bet")


#Flip a coin game

def flip_a_coin(guess, bet):
  print("You guessed " + guess)
  print("..?")
  result = random.randint(1, 2)
  if result == 1:
    print("Heads")
  else: 
    print("Tails")
  

  if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
    print("you won " + str(bet))
    return bet
  elif (guess == "Heads" and result == 2) or (guess == "Tails" and result == 1):
    print("you lost " + str(bet))
    return bet
  else:
    print("\n")
    print("Guess invalid, please choose Heads or Tails")
    


# / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Cho-Han game

def cho_han(guess, bet):
  print("You guessed " + guess)
  print("...?")
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)

  #total count of random numbers combine
  total_count = dice1 + dice2
  print("total count is " + str(total_count))

  if total_count % 2 == 0:
    print("answer: Cho")
  else:
    print("answer: Han")
  
  if (guess == "Cho" and total_count % 2 == 0) or (guess == "Han" and total_count % 2 == 1):
    print("you won " + str(bet))
    return bet
  elif (guess == "Cho" and total_count % 2 == 1) or (guess == "Han" and total_count % 2 == 0):
    print("you lost " + str(bet))
    return bet
  else:
    print("\n")
    print("Guess invalid, please choose Cho or Han")



# / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Higher number 

def higher_card(bet):
  my_card =  random.randint(1, 52)
  player_two = random.randint(1, 52)

  print("Your card: \n" + str(my_card))
  print("player 2's card: \n" + str(player_two))

  if my_card > player_two:
    print("You Won! " + str(bet))
    return bet
  elif my_card < player_two:
    print("You lost " + str(bet))
    return bet
  else: 
    print("You have had the same number card, its a tie")
    return 0

 



# / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Roulette

def roulette(guess, bet):
  print("Welcome to Roulette!\n")
  print("Your guess is... " + str(guess))
  print("\n")
  print("Ball rolling.......Best of luck!")
  print("\n")
  result = random.randint(0, 37)

  if result == 37:
    print("ball landed on 00")
    print("\n")
  else:
    print("The ball landed on " + str(result))
    print("\n")

    #if numebr is even 
  if guess == "Even" and result % 2 == 0 and result != 0:
    print("The number was Even ")
    print("\n")
    print("You won! " + str(bet))
    return bet

    #if number is odd
  elif guess == "Odd" and result % 2 == 1 and result != 37:
    print("The number was Odd ")
    print("\n")
    print("You Won " + str(bet))
    return bet

  #checking if whole number is result number
  elif guess == result:
    print("Your guess was " + str(guess) + "the result was " + str(result))
    print("You won! " + str(bet * 35))
    return bet * 35

  else:
    print("You lost " + str(bet))
    return bet 
  
  




flip_a_coin("Heads", 10)
money += cho_han("Han", 40)
money += higher_card(50)
money += roulette(22, 50)
money += roulette("Even", 40)

  
