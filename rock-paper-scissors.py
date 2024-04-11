rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Welcome to the rock paper scissors game!\n choose : \n 1 for rock \n 2 for paper \n 3 for scissors")
user_choice = int(input("What do you choose?:- "))
if user_choice >3 or user_choice <1:
  print("You typed an invalid number, you lose!, Next time choose between 1,2,3")
else:
  import random
  
  
  computer_choice=random.randint(0,2)
  choice_lst=[rock,paper,scissors]
  
  print(f"You chose {choice_lst[user_choice-1]}")
  print(f"computer chose {choice_lst[computer_choice]}")
  
  if computer_choice==0 and user_choice==2:
    print("You win!")
  
  elif computer_choice==1 and user_choice==3:
    print("You win!")
  
  elif computer_choice==2 and user_choice==1:
    print("You win!")
  
  elif computer_choice==user_choice-1:
    print("draw!")
  
  else:
    print("You lose!")
