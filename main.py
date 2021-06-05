
def goInside():
  print()
  print("You walk inside the pub. It's loud, noisy, and there appear to be owls on the wall? What do you want to do next?")
  barChoice = input("A - Buy a drink  B - Talk to a lady skeleton")
  if barChoice == "A":
    orderADrink()
  else:
    talkToALady()

def playTromBone():
  print()
  print("You take out your trombone from your pocket dimension and ask the lady, Bonejour, may I humble you to a song?")

def callGoons():
  print("You have annoyed the lady a lot so she calls her goons. What will you do now?")


def persist():
  print()
  print("He taps her shoulder and says HEY, my names Gandalf. You get to Mordor much?")
  persistChoice = input("A - Play the trom-🦴. B - Ask for her name")
  if persistChoice == "A":
    playTromBone()
  


def talkToALady():
  print()
  print("'Hi' he said awkwardly. She ignores him")
  talkChoice = input("A - You Walk Away And Order a Drink    B - You Persist and still try to strike up a conversation")
  if talkChoice == "A":
    orderADrink()
  else:
    persist()
  

def walkAway():
  print()
  print("You walk back home, take a quick ride on your broomstick to let off some steam. Then you went to bed, and thus ends our tale")

def orderADrink():
  print()
  print("You walk up to the bar and ask for a Bone Broth on the rocks")

print("-------------------------------")
print("The Tale of Romeo and Skeletina")
print("-------------------------------")

print("Greetings, your name is Skeletina. You're a good looking skeleton, but a little bored.")
print("One night, you go walking and come up to the local skeleton pub. What do you want to do?")
print("A - Go Inside")
print("B - Turn Your Bony Nose Up and Walk Away")

choiceOne = input()

if choiceOne == "A":
  goInside()
else:
  walkAway()
