# This is a sample Python script.
import paper
import rock


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random

#random_heads_or_tails=random.randint(0,1)
#print(random_heads_or_tails)
#if random_heads_or_tails==0:
#    print("Heads")
#else:
#    print("Tails")

#friends=["Alice","Bob","Charlie","David","Emanuel"]
#random_name=random.choice(friends)
#print(random_name)
#random_index=random.randint(0,4)
#print(friends[random_index])

# Create a list of dirty_dozen

dirty_dozens=["strawberries","spinach","kale","Nectarines","Apples","Grapes","peaches","cherries","pears"]
#Separate the list into two: one, a list of fruits, and the second one a list of vegetables

#fruits=["strawberries","Nectarines","Apples","Grapes","peaches","cherries","pears"]
#vegetables=["spinach","kale","Tomatoes","celery","potatoes"]
# create a new list containing the above list
#dirty_dozen=[fruits,vegetables]
#print(dirty_dozen[0])
#print(dirty_dozen[1])
#print(dirty_dozen[1][1])
#print(dirty_dozen[1][2])
#print(dirty_dozen[1][3])

# This is a game of Rock, paper, Scissors

game_images=[rock,paper,scissors]
user_choice= int(input("what do you choose? Type  0 for Rock,  1 for paper, or  2 for Scissors\n"))
computer_choice=random.randint(0,2)
print(f"computer_chose {computer_choice}")
if user_choice >=3 or user_choice <0:
    print("You typed an invalid number. You lose" )
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice==user_choice:
    print("It is a draw")
else:
    print("You typed an invalid number")


#else:
#   print("You won the game !")



