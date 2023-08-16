import random

name = input("Enter you name: ")
choices = ["rock", "paper", "scissors"]

Cscore = 0
Pscore = 0
Round = 0

print(f"Welcome {name.title()}.")
print("IF YOU'VE ENTERED A WORD OTHER THAN THE CHOICES, A COMPUTER AUTOMATICALLY WINS. BE CAREFUL AND GOODLUCK.")
print("")
print("")

while True:
  Poption = input("Please enter your choice(Rock / Paper / Scissors): ").lower()
  Coption = random.choice(choices)

  print("")
  print(f"{name} option: {Poption}")
  print(f"Computer option: {Coption}")

  Round += 1

  if Poption == Coption:
    print("It's a tie")

  elif (Poption == "rock" and Coption == "scissors") or (Poption == "paper" and Coption == "scissors") or (Poption == "scissors" and Copttion == "rock"):
    print("Computer win!")
    Cscore += 1

  elif (Poption=="rock" and Coption=="scissor") or (Poption=="scissor" and Coption=="paper") or (Poption=="paper" and Coption=="rock"):
        print("You win!")
        PScore = PScore + 1

  else:
      print("You've entered a wrong choice. Computer wins")
      CScore = CScore + 1

  print("----------------------------------")
  print("")
  print("Round No. " + str(Round))
  print("-------S C O R E  B O A R D------")
  print(f"{anme.title()} : {PScore} --0-- Computer {CScore}")
  print("~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.")
  print("")


  if Pscore == 5 or Cscore == 5:
    break

if Pscore > Cscore:
  print("You win! :>")

else:
  print("You lose! :<")
