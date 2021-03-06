# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random
from datetime import date

NO_OF_RECENT_SCORES = 10
aceHigh = False
sameCardEndGame = False
GameOver = False

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.date = None

Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print("5. Options")
  print("6. Save scores")
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  Choice = Choice.lower()
  print()
  return Choice

def DisplayOptions():
  print()
  print("OPTIONS MENU")
  print()
  print("1. Set ace as high or low")
  print("2. Card of same score ends game")
  print()

def GetOptionChoice():
  valid = False
  while not valid:
    optionChoice = input("Select an option from the menu (or enter q to quit): ")
    if optionChoice in ["1","2","q"]:
      valid = True
    else:
      print("Please enter a valid option.")
  print()
  return optionChoice.lower()

def SetOptions(optionChoice):
  if optionChoice == "1":
    SetAceHighOrLow()
  elif optionChoice == "2":
    SetSameScore()

def SetAceHighOrLow():
  global aceHigh
  valid = False
  while not valid:
    aceValue = input("Do you want the Ace to be (h)igh or (l)ow: ")
    aceValue = aceValue.lower()
    if aceValue in ["h","l"]:
      valid = True
    else:
      print("Please enter a valid choice.")
    if aceValue == "h":
      aceHigh = True
    else:
      aceHigh = False

def SetSameScore():
  global sameCardEndGame
  valid = False
  while not valid:
    sameCard = input("Do you want cards with the same value as the previous card to end the game? (y or n)")
    sameCard = sameCard.lower()
    if sameCard in ["y","n"]:
      valid = True
    else:
      print("Please enter a valid choice.")
    if sameCard == "y":
      sameCardEndGame = True
    else:
      sameCardEndGame = False

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  global aceHigh
  global sameCardEndGame
  global GameOver
  if aceHigh and NextCard.Rank == 1:
    NextCard.Rank = 14
  if aceHigh and LastCard.Rank == 1:
    LastCard.Rank = 14
  if not aceHigh and NextCard.Rank == 14:
    NextCard.Rank = 1
  if not aceHigh and LastCard.Rank == 14:
    LastCard.Rank = 1
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  elif sameCardEndGame and NextCard.Rank == LastCard.Rank:
    GameOver = True
  elif not sameCardEndGame:
    GameOver = False
  return Higher

def GetPlayerName():
  print()
  valid = False
  while not valid:
    PlayerName = input("Please enter your name: ")
    if len(PlayerName) > 0:
      valid = True
    else:
      print("You must enter something for your name!")
  print()
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  Choice = Choice.lower()
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].date = None

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("{0:<12}{1:<10}{2:<5}".format("date", "Name", "Score"))
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    if RecentScores[Count].date != None:
      scoreDate = RecentScores[Count].date.strftime("%d/%m/%Y")
    else:
      scoreDate = "N/A"
    print("{0:<12}{1:<10}{2:<5}".format(scoreDate, RecentScores[Count].Name, RecentScores[Count].Score))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def BubbleSortScores(RecentScores):
  swapped = True
  while swapped:
    for count in range(1,NO_OF_RECENT_SCORES):
      if RecentScores[count].Score < RecentScores[count + 1].Score:
        temp1 = RecentScores[count]
        RecentScores[count] = RecentScores[count + 1]
        RecentScores[count + 1] = temp1
    swapped = False

def SaveScores(RecentScores):
  with open("save_scores.txt",mode="w",encoding="utf-8")as my_file:
    for Score in RecentScores:
      if Score != None:
        if Score.Name != "":
          my_file.write(Score.date.strftime("%d/%m/%Y")+",")
          my_file.write(Score.Name+",")
          my_file.write(str(Score.Score)+"\n")

def LoadScores(RecentScores):
  try:
    with open("save_scores.txt",mode="r",encoding="utf-8")as my_file:
      scores = my_file.read().splitlines()
      for score in range(len(scores)):
        temp = scores[score].split(",")
        scores[score] = temp
        scoreDate = scores[score][0]
        day = scoreDate[0:2]
        month = scoreDate[3:5]
        year = scoreDate[6:]
        scoreDate = date(int(year),int(month),int(day))
        scores[score][0] = scoreDate
      RecentScores = [None]
      for score in scores:
        newScore = TRecentScore()
        newScore.date = score[0]
        newScore.Name = score[1]
        newScore.Score = int(score[2])
        RecentScores.append(newScore)
  except FileNotFoundError:
      RecentScores = [None]
  return RecentScores

def UpdateRecentScores(RecentScores, Score):
  addScore = ""
  while addScore == "":
    print()
    addScore = input("Do you want to add your score to the high score table? (y or n): ")
    print()
    if addScore == "y":
      PlayerName = GetPlayerName()
      FoundSpace = False
      Count = 1
      while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
        if RecentScores[Count].Name == '':
          FoundSpace = True
        else:
          Count = Count + 1
      if not FoundSpace:
        for Count in range(1, NO_OF_RECENT_SCORES):
          RecentScores[Count].Name = RecentScores[Count + 1].Name
          RecentScores[Count].Score = RecentScores[Count + 1].Score
        Count = NO_OF_RECENT_SCORES
      RecentScores[Count].Name = PlayerName
      RecentScores[Count].Score = Score
      RecentScores[Count].date = date.today()
    elif addScore == "n":
      print()
      print("Returning to main menu")
      print()
    elif addScore != "y" or addScore != "n":
      print()
      print("Invalid choice, please try again.")
      print()
      addScore = ""

def PlayGame(Deck, RecentScores):
  global GameOver
  LastCard = TCard()
  NextCard = TCard()
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while Choice not in ["y","yes","n","no"]:
      Choice = GetChoiceFromUser()
    if Choice == "yes":
      Choice = "y"
    elif Choice == "no":
      Choice = "n"
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if not GameOver:
      if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
        DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
        LastCard.Rank = NextCard.Rank
        LastCard.Suit = NextCard.Suit
      else:
        GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  RecentScores = LoadScores(RecentScores)
  if len(RecentScores) == 0 or len(RecentScores) < NO_OF_RECENT_SCORES:
    additionalScores = NO_OF_RECENT_SCORES - len(RecentScores) + 1
    for Count in range(1, additionalScores + 1):
      RecentScores.append(TRecentScore())
  Choice = ''
  while Choice not in ['q',"quit"]:
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptions()
      optionChoice = GetOptionChoice()
      if optionChoice != "q":
        SetOptions(optionChoice)
    elif Choice == "6":
      SaveScores(RecentScores)
