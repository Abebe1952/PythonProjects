# ReSharper disable all CheckNamespace
import paper
#class Task
#{
#    public static void Main(string[] args)
 #   {
 #       # your code here
 #       Console.WriteLine("Hello world");
 #   }
#}
#
#random_number_0_to_1=random.random()
#print(random_number_0_to_1)

# Rock,paper, scissors game



game_images=[rock,paper,scissors]
user_choice=int(input("what do you choose? Type 0 for Rock,1 for paper, or 2 for scissors\n"))
if user_choice>=0 and user_choice<=2:
  print(game_images[user_choice])
computer_choice=random.randint(0,2)
print("computer chose:")
print("game_images[computer_choice]")
elif user_choice>=3 or user_choice<0:
  print("you typed an invalid number. You lost!")
elif user_choice==0 and computer_choice==2:
  print("You win!")
elif computer_choice==0 and user_choice==2:
  print("You lose !")
elif computer_choice>user_choice:
  print("You lose!")
elif user_choice > computer_choice