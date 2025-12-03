print("Welcome to the Treasure island!")
print(" Your mission is to find the treasure")
choice1=input('you\'re at a crossroad,where do you want to go?' 'Type "left" or "right".\n').lower()

if choice1=="left":
    choice2=input('You\'ve come to a lake.'
                  "There e is an island in the middle of the lake."
                  'Type "wait" to wait for a boat.'
                  'Type "swim" to swim across.\n').lower()
    if choice2 =="wait":
        choice3=input("You arrive at the island unharmed."
                      "There is a house with 3 doors.One red,"
                      "one yellow and one blue."
                      "which colour do you choose\n").lower()
        if choice3=="red":
            print("It is a room full of fire. Game over")
        elif choice3=="yellow":
            print("you found the treasure. you win")
        elif choice3 =="blue":
            print("you entered a room of beasts.Game over")
else:
    print("Game over.")



