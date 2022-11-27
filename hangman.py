import random
from os import system
import logging
import logging


# creating logging info file with data
logging.basicConfig(level=logging.INFO, filename="hangman.log", filemode = "w", 
format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("info")

hangman_lives = 10

# greeting with a player
name = input("Enter your name: ")
logging.info(f"Hello {name}") 
print(f"Hello {name}")

word = ['cat', 'racoon', 'criminal', 'different', 'lady', 'manufacturing', 'occupation', 'cheer', 'light']
# generate random word list
# creating function to play the game
def generate_word():
    return word[random.randint(0, len(word) -1)]

def draw_body(bad_attempt):
    
    if bad_attempt == 1:
        return """
 ------
 |    
 |    
 |
 |
 |
 |
 |
 |
----------
"""

    if bad_attempt == 2:
        return  """
 ------
 |    |
 |    
 |
 |
 |
 |
 |
 |
----------
"""

    if bad_attempt == 3:
        return """
 ------
 |    |
 |    O
 |   
 | 
 |   
 |   
 |   
 |   
----------
"""

    if bad_attempt == 4:
        return """
 ------
 |    |
 |    O
 |   -+-
 |   
 |   
 |   
 |   
 |   
----------
"""

    if bad_attempt == 5:
        return """
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
"""

    if bad_attempt == 6:
        return """
 ------
 |    |
 |    O
 |  /-+-/
 |    
 |   
 |   
 |   
 |   
----------
"""
    if bad_attempt == 7:
        return """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 | 
 |    
 |   
----------
"""

    if bad_attempt == 8:
        return """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |  
----------
"""
    
    if bad_attempt == 9:
        return """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
"""
    
def play_game() ->None:
    word = generate_word()
    progress = ''
    for i in range(len(word)):
        progress += '_'
    bad_attempt = 0
    tries = []


    while True:
        _ = system('clear')
        # clear window game
        guessesString = ''
        
        for i in range(len(tries)):
            if i != len(tries) and i !=0:
                guessesString += ', '
            guessesString += tries[i]
        print(f'Your guesses: {guessesString}')
        print(draw_body(bad_attempt))

        if progress == word:
            print(progress)
            print('You win!')
            break
        if bad_attempt >=10:
            print('You lose!')
            logging.info(f'The word was "{word}".')
            print(f'The word was "{word}".')
            break
        print(progress)
        
        guess = input()
     
        if guess not in tries:
            tries.append(guess)
        if guess in word:
            # print(f'The letter {guess} is in the word.')
            for i in range(len(word)):
                if guess == word[i]:
                    progressStart = progress[0:i]
                    progressEnd = progress[i+1:]
                    progress = progressStart + guess + progressEnd
        else:
            logging.info(f'The letter {guess} is not in the word.')
            print(f'The letter {guess} is not in the word.')
            bad_attempt +=1

if __name__ == '__main__':

    while True:
        print('Hi! Want to play hangman? (yes / no)')
        answer = input()
        if answer.lower() == 'yes':
           play_game()
        if answer.lower() == 'no':
            print('Bye bye!')
            break
    