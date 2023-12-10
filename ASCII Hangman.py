'''Simple version of Hangman with no external modules or packages.
ASCII images added'''

MAX_WRONGS = 10

def title():
  print("     _         __         _")
  print("| | | | |\\  | |  \\ |\\ /| | | |\\  |")
  print("|-| |-| | \\ | |  _ | V | |-| | \\ |")
  print("| | | | |  \\| \\__/ |   | | | |  \\|")

def playerNames():
  names = []
  for i in range(1,3):
    names.append(input("Player " + str(i) + " what is your name? " ))
    print("Thank you", names[-1])
  return names

def isGuesser(name):
  ans = input(name + " do you want to guess the answer this time? ")
  return ans.lower() in ["yes", "y"]
    
def getAns(guesser, host):
    print(guesser, "please look away for just now")
    ans = input(host + " please think of a movie, song, game, book etc title: ").lower()
    input("thanks "+ host + " press enter to clear the screen and start the next round")
    print("\n"*200)
    print(guesser, "please look now")
    return ans

def hideText(ans):
  hidden = []
  for char in ans:
    if char == " ":
      hidden.append("/")
    else:
      hidden.append("*")
  return hidden

def drawMan(livesLost):
  print(livesLost)
  print(" "+"_"*9)
  print("|"+" "*9+"|")
  if livesLost>=1:
    # head
    print("|"+" "*8+"_|_")
    print("|"+" "*7+"/o o\\")
    print("|"+" "*6+"|  L  |")
    print("|"+" "*7+"\ - /")
    print("|"+" "*9+"v")
  else:
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
  if livesLost >=4:
    # upper arms
    print("|"+" "*8+"/|\\")
    print("|"+" "*7+"/ | \\")
    print("|"+" "*6+"/  |  \\")
  elif livesLost == 3:
    # one set of arms
    print("|"+" "*8+"/|")
    print("|"+" "*7+"/ |")
    print("|"+" "*6+"/  |")
  elif livesLost == 2:
    # torso only
    print("|"+" "*8+" |")
    print("|"+" "*7+"  |")
    print("|"+" "*6+"   |")
  else:
    print("|")
    print("|")
    print("|")
  if livesLost >=8:
    # lower arms and upper legs
    print("|"+" "*5+"|   |   |")
    print("|"+" "*5+"|   |   |")
    print("|"+" "*5+"|  / \\  |")
    print("|"+" "*5+"O /   \\ O")
    print("|"+" "*5+" /     \\ ")
  elif livesLost == 7:
    #lower arms and one set of legs
    print("|"+" "*5+"|   |   |")
    print("|"+" "*5+"|   |   |")
    print("|"+" "*5+"|  /    |")
    print("|"+" "*5+"O /     O")
    print("|"+" "*5+" /      ")
  elif livesLost == 6:
    #lower arms only
    print("|"+" "*5+"|   |   |")
    print("|"+" "*5+"|   |   |")
    print("|"+" "*5+"|       |")
    print("|"+" "*5+"O       O")
    print("|"+" "*5+"        ")
  elif livesLost == 5:
    # one lower arm only
    print("|"+" "*5+"|   |   ")
    print("|"+" "*5+"|   |   ")
    print("|"+" "*5+"|       ")
    print("|"+" "*5+"O       ")
    print("|"+" "*5+"       ")
  else:
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")

  if livesLost >= 10:
    # lower legs
    print("|"+" "*5+"|       |")
    print("|"+" "*5+"|       |")
    print("|"+" "*5+"|       |")
    print("|"+" "*4+"[]       []")
  elif livesLost == 9:
    # left lower leg
    print("|"+" "*5+"|       ")
    print("|"+" "*5+"|       ")
    print("|"+" "*5+"|       ")
    print("|"+" "*4+"[]       ")
  else:
    print("|")
    print("|")
    print("|")
    print("|")

  
  print("|")
  print("|")
  print("|________________")

def add_letter(letter, answer, solution):
  for pos, val in enumerate(answer):
    if val == letter:
      solution[pos] = letter
  return solution

def lose_life(lives_lost):
  print("bad luck, it is not in the title")
  lives_lost += 1
  drawMan(lives_lost)
  return lives_lost


def turn(answer, guesser):
  print(guesser, "it is your turn to guess")
  wrongs = 0 
  past_letters = []
  guessed = hideText(answer)
  while True:
    print("solution so far is: ")
    print(guessed)
    letter = input("what letter do you think is in the answer? ")
    while letter in past_letters:
      print("you have already chosen that letter, try again")
      print("you have already chosen", past_letters)
      letter = input("please chose a different letter: ")
    past_letters.append(letter)
    if letter in answer:
      print("well done, it is in the answer")
      guessed = add_letter(letter, answer, guessed)
      if "*" not in guessed:
        print("well done!  You got it!")
        print("you had", wrongs, "wrong guesses")
        return True
    else:
      wrongs = lose_life(wrongs)
      if wrongs > MAX_WRONGS:
        print("sorry you have no tries left")
        return False
    
def game_2p():
  title()
  players = playerNames()
  if isGuesser(players[0]):
    guesser = players[0]
    host = players[1]
  else:
    guesser = players[1]
    host = players[0]
  # players.remove(guesser)
  scores = {players[0]: 0, players[1]: 0}

  while True:
    print("let's play Hangman")
    title()
    ans = getAns(guesser, host)
    win = turn(ans, guesser)
    if win:
      scores[guesser] += 1
    else:
      scores[host] += 1
    print("the scores are", guesser, scores[guesser], host, scores[host])
    ans = input("play again? ")
    if ans.lower() in ["no", "n"]:
      print("nice having you, bye!")
      return
    host, guesser = guesser, host
    
game_2p()




