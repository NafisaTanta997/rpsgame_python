from random import randint

#create options for game
t = ["Rock", "Paper", "Scissors"]

#keep track of scores
p_score = 0
c_score = 0
p_str = "Player: "
c_str = ", Computer: "


#assign a random player to the computer
computer = t[randint(0,2)]

#set player to FALSE
player = False

while player == False:
#set player to True
  player = input("Rock, Paper, Scissors?")
  if player == computer:
    print("Tie!")

  elif player == "Rock":
    if computer == "Paper":
      c_score += 1
      print("You lose " + computer + " covers " + player)
      print(p_str + str(p_score) + c_str + str(c_score))
    else:
      p_score += 1
      print("You win! " + player + " breaks " + computer)  
      print(p_str + str(p_score) + c_str + str(c_score))

  elif player == "Paper":
    if computer == "Scissors":
      c_score += 1
      print("You lose " + computer + " cuts " + player)
      print(p_str + str(p_score) + c_str + str(c_score))

    else:
      p_score += 1
      print("You win! " + player + " covers " + computer)
      print(p_str + str(p_score) + c_str + str(c_score))

  elif player == "Scissors":
    if computer == "Rock":
      c_score += 1
      print("You lose " + computer + " breaks " + player)
      print(p_str + str(p_score) + c_str + str(c_score))

    else:
      p_score += 1
      print("You win! " + computer + " cuts " + player)
      print(p_str + str(p_score) + c_str + str(c_score))

  else:
    print("That's not a valid play. Check your spelling!")

  #player was set to True, but we want it to be False so that the loop continues
  player = False
  computer = t[randint(0,2)]  

