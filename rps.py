# Create a Rock Paper Scissors game. The rules of the game are Rock dulls Scissors, Scissors cut Paper, and Paper covers Rock.
import random


def proc_game(u_play: str, u_score: dict, r_play: str) -> dict:
    # To keep immutability, make a copy of the score dict
    RET_SCORE = u_score
    
    def win():
        print(f'\nYou played {u_play}, and the AI played {r_play}. You win!\n')
        RET_SCORE['player_w'] += 1
    def lose():
        print(f'\nYou played {u_play}, and the AI played {r_play}. You lose.\n')
        RET_SCORE['computer_w'] += 1
    
    
    if u_play == r_play: # Tied computer and player
        print(f'\nYou played {u_play}, and the AI played {r_play}. You tied!')
        print(f'The score is still {u_score["player_w"]} to {u_score["computer_w"]}\n')
    else:
        if u_play == 'rock':
            if r_play == 'scissors': # Win condition // rock > scissors
                win()
            elif r_play == 'paper': # Lose condition // rock < paper
                lose()
        elif u_play == 'paper':
            if r_play == 'rock': # Win condition // paper > rock
                win()
            elif r_play == 'scissors': # Lose condition // paper < scissors
                lose()
        elif u_play == 'scissors':
            if r_play == 'paper': # Win condition // scissors > paper
                win()
            elif r_play == 'rock': # Lose condition // scissors < rock
                lose()
    
    RET_SCORE['games_played'] += 1
    return RET_SCORE
                

def prompt_game() -> bool:
    temp_game = bool()
    while True:
        print("Get ready! 3, 2, 1! What are you picking? rock/paper/scissors")
        # Using .lower() allows to check the value ignoring the case.
        U_GAME = input().lower()
        
        # if var in tuple allows for if statements matching a variable to many values.
        if U_GAME in ('rock', 'paper', 'scissors'):
            temp_game = U_GAME
            break
        elif U_GAME:
            print("Assure that the input is of the right value.\n")
            continue
    return temp_game
    # assert U_GAME != '', "Input is empty."

if __name__ == '__main__':
    STATE = int(input("How many rounds would you like to play? (min 1 round)"))
    # Make sure that the levels are more than one.
    assert STATE > 0, "Not enough rounds provided."
    
    score = {
        'games_played': 0,
        'computer_w': 0,
        'player_w': 0
    }

    while STATE > 0:
        U_INPUT = prompt_game()
        print(f"DEBUG: The user inputted '{U_INPUT}'")
         
        # IMPLEMENT RANDOM NUMBER GEN (R, P, S)
        AI_PLAY = random.choice(['rock', 'paper', 'scissors'])
        print(f"DEBUG: The AI chose '{AI_PLAY}'")

        score = proc_game(U_INPUT, score, AI_PLAY)
        print(f"DEBUG: The returned value of proc_game is {score}")
        
        STATE -= 1
        
        continue
    
    print(f"The final score is {score['player_w']} to {score['computer_w']}")
    
    if score['player_w'] > score['computer_w']:
        print("\n\nYou won the game!")
    elif score['player_w'] == score['computer_w']:
        print("\n\nYou tied the game!")
    else: 
        print("\n\nYou lost the game!, play again some time?")