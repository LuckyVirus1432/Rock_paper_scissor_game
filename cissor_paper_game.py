#importing random module 
import random           

#game() function where we have implemented the actual logic of the game.
def game(compturn, yourturn):           
    if compturn == yourturn:
        return None
    elif compturn == 1:
        if yourturn==2:
            return True
        else:
            return False
    elif compturn == 2:
        if yourturn==1:
            return False
        else:
            return True
    elif compturn == 3:
        if yourturn==2:
            return False
        else:
            return True
        
print("*" * 100)
print("*" + (" " * 35) + " Rock, Paper, Scissor Game  " + (" " * 35) + "*")
print("*" * 100)       
rules = '''(!) Rules to play Rock, Paper, Scissor: 
        1) You are playing with computer i.e computer will choose 1 randomly among Rock, paper, Scissor.
        2) You have to choose 1 among Rock, paper, Scissor with 1, 2 & 3 numbers respectively.
        3) Rock vs Paper => Paper wins
        4) Rock vs Scissor => Rock wins
        5) Paper vs Scissor => Scissor wins
        6) If result comes as:
            None => Draw
            True => You won
            False => You Loose.
        6) To exit from game press 4.
    '''
print(rules)
while(True):
    try:
        print("*" * 100)
        compturn = random.randint(1,3)
        print("Comp Turn: Rock(1), Paper(2), Scissor(3)? ")
        yourturn = int(input("Your Turn: Rock(1), Paper(2), Scissor(3), Exit(4)? "))

        if yourturn < 1 or yourturn > 4:
            print("Invalid input..!")
        elif yourturn==4:
            print("\nExiting game..!")
            break
        else:
            print(game(compturn, yourturn))
    except ValueError as t:
        print("\nError occured: Only numbers are allowed.\n")
    except Exception as e:
        print(f"Error: {e}")


