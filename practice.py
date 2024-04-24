import random

name = input ("Enter your name: ")
print("Hello " + name + "!")


def play_game(numbers) :

    total = 0
    print("Welcome to the game of 21")
    

    print("You have chosen to play with ", numbers, ".")


    while total < 21:
       print("Total:", total)

       if numbers == 3 :
            move = int(input("Enter your move (1, 2, or 3): "))
       else :
            move = int(input("Enter your move (1 or 2): "))
               

       if move < 1 or move > numbers :
           print("Invalid move, please enter a number between 1 and", numbers)
           continue

       total += move
    

       if total >= 21 :
           print (name, "you said 21! Computer wins!")
           return
       
       computer_move = random.randint(1, numbers)
       print("Computers move: ", computer_move)
       total += computer_move

       if total >= 21 :
          print("Computer said 21! You win")
          return
       
    print ("Winner")   

num_numbers = int(input("Enter the number of numbers to play with (2 or 3): "))

if num_numbers !=2 and num_numbers != 3:
    print("Invalid input. Please enter either 2 or 3.")
else :
    play_game(num_numbers)    
