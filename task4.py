import random
def play():
  user=input("choose rock,paper or scissors:").lower()
  computer=random.choice(['rock','paper','scissors'])
  print(f"you chose:{user}")
  print(f"computer choose:{computer}")
  if user==computer:
    return "it's a tie"
  elif (user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper"):
    return "you win"
  else:
    return "you lose!"
def main():
  user=0
  computer=0
  while True:
    result=play()
    print(result)
    if "win" in result:
      user=user+1
    elif "lose" in result:
      computer=computer+1
    else:
      pass
    print(f"your score:{user} | computer score:{computer}")
    play_again=input("Do you want to play again? (y/n):").lower()
    if play_again=='yes':
      print("Thanks for playing")
      break
if __name__=="__main__":
  main()
