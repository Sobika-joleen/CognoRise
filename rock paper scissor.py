import random
moves = ["rock", "paper", "scissors"]
for i in range (100):
    print("1.play  \n 2. exit")
    ch=int(input("enter your choice"))
    if(ch==1):
           user_action = input("Enter a choice (rock, paper, scissors): ")
           computer_action = random.choice(moves)
           if user_action == computer_action:
               print(f"It's a tie! Both chose {user_action}.")
           elif (user_action == "rock" and computer_action == "scissors") or \
            (user_action == "paper" and computer_action == "rock") or \
            (user_action == "scissors" and computer_action == "paper"):
             print(f"You win! {user_action} beats {computer_action}.")
           else:
             print(f"You lose! {computer_action} beats {user_action}.")
    else:
        break


