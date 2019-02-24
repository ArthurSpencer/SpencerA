import random
import os



def display_secret_word(secret_word, guesses):
    letters_missing = 0
    for letter in secret_word:
        if letter in guesses:
            print(letter, sep=' ', end='', flush=True)
        else:
            print ("_ ", sep=' ', end='', flush=True)

def display_hangman(incorrect_guesses):

        if incorrect_guesses ==  0:
            print("__________")
            print("|/        ")	
            print("|        ")
            print("|        ")
            print("|         ")
            print('|        ')
            print("|")
            print("|___")

        elif incorrect_guesses ==  1:
            print("__________")
            print("|/        |")	
            print("|        ")
            print("|        ")
            print("|         ")
            print('|        ')
            print("|")
            print("|___")
            
        elif incorrect_guesses ==  2:
            print("__________")
            print("|/        |")	
            print("|        (_)")
            print("|        ")
            print("|           ")
            print('|        ')
            print("|")
            print("|___")
            
        elif incorrect_guesses ==  3:
            print("__________")
            print("|/        |")	
            print("|        (_)")
            print("|        \|/")
            print("|          ")
            print('|        ')
            print("|")
            print("|___")
            
        elif incorrect_guesses ==  4:
            print("__________")
            print("|/        |")	
            print("|        (_)")
            print("|        \|/")
            print("|         |  ")
            print('|        ')
            print("|")
            print("|___")

        elif incorrect_guesses ==  5:
            print("__________")
            print("|/        |")	
            print("|        (_)")
            print("|        \|/")
            print("|         |  ")
            print('|        / \\')
            print("|")
            print("|___")
              
        #endif
    

    
words = ['bop', 'house', 'mouth', 'bone', 'mode', 'modular']
secret_word = random.choice(words)
guesses = []
incorrect_guesses = 0
correct_needed = len(secret_word)
correct = 0
game_over = False

while not game_over:
    print('time to play hangman')


    
    display_secret_word(secret_word, guesses)

    print("")


    display_hangman(incorrect_guesses)


    guess = input('guess a letter: ')
    letter = guess
    guesses.append(guess)


    if letter in secret_word:
        correct = correct + 1
        correct_needed = correct_needed - 1
    else:
        incorrect_guesses = incorrect_guesses + 1
    
    print ('Guesses made: ')
    print (guesses)
    print ('Incorrect guesses: ')
    print (incorrect_guesses)

    input()
    
    os.system('cls')

    if incorrect_guesses == 5 or correct_needed == 0:
        game_over = True
    else:
        game_over = False

#endwhile

if incorrect_guesses == 5:
    print ("Loser")
else:
    print ("Winner")
        
#endif
