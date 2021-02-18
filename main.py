import random

print("Welcome to Rock, Paper, Scissors!\n")

rpsNames = {"r" : "Rock", "p" : "Paper", "s" : "Scissors"}
beats = {"r" : "s", "p" : "r", "s" : "p"}

ant = ""
winCount = 0
tieCount = 0
loseCount = 0

def win():
  global winCount
  print("\nYou win!")
  winCount += 1
  print("You've won " + str(winCount) + " times.")

def lose():
  global loseCount
  print("\nI win!")
  loseCount += 1
  print("I've won " + str(loseCount) + " times.")

def tie():
  global tieCount
  print("\nIt's a tie.")
  tieCount += 1
  print("We've tied " + str(tieCount) + " times.")

while ant != "q":
  myGuess = random.choice(["r", "p", "s"])
  while ant not in ("r", "p", "s", "q"):
    ant = input("Enter [R]ock, [P]aper, [S]cissors, or [Q]uit)!: ")
    if ant:
      ant = ant[0].lower()

  if ant != "q":
    print("You guessed: " + rpsNames[ant])
    print("I guessed " + rpsNames[myGuess])
    if ant == myGuess:
      tie()
    if myGuess == beats[ant]:
      win()
    if ant == beats[myGuess]:
      lose()
    print("\nPlay again?")
    ant = ""

print("Thank you for playing.")