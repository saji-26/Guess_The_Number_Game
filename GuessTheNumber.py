import random

# Counters for the game statistics
games_won = 0
games_lost = 0
games_played = 0
total_score = 0

# Ask for the player's name once, so it can be used in messages and stats
name = input('What is your name? ')

def get_guess():
    """Ask the player for a guess and keep asking until it is valid.
    Returns:
        int: a whole number between 1 and 100."""
    
    while True: 
        try:
            guess = int(input("Choose a number between 1 - 100: "))
        except ValueError:
            # int() fails on letters, decimals or empty input
            print('Please enter a whole number.')
            continue

            # Reject numbers outside the allowed range
        if guess < 1 or guess > 100:
            print('Please enter a number between 1 - 100.')
            continue

        return guess

def game():
    """Play one round of Guess The Number and update the global counters."""

    # 'global' lets this function change the counters defined outside it
    global games_played, games_won, games_lost, total_score

    secret_number = random.randint(1, 100)
    attempts = 7
    guesses = 0

    print('=======Welcome to Guess The Number!=======')
    print('You have 7 attempts, try to guess the same as me!')
    print('Remember, you get more points the less attempts it takes!')

    # Keep looping until the player runs out of attempts or wins
    while attempts > 0:
        guess = get_guess()

        guesses += 1
        attempts -= 1

        if guess == secret_number:
            print(f'Well done {name}! The number was {secret_number}!')
            print(f'It took you {guesses} guesses.')

            # Fewer guesses = more points. attempts was already reduced
            # by 1, so attempts + 1 is how many the player had before
            # this guess (first guess = 70 points, last guess = 10).
            points = (attempts + 1) *10
            total_score += points
            print(f'You scored {points} points!')

            games_won += 1
            games_played += 1
            return
        
        # Give a hint so the player can narrow down the number
        elif guess < secret_number:
            print('Too low!')
        else:
            print('Too high!')

        if attempts > 0:
            print(f'You have {attempts} attempts remaining')

    # Reaching this point means the loop ended without a win
    print(f'Sorry {name}, GAME OVER!')
    print(f'The number was {secret_number}.')

    games_lost += 1
    games_played += 1


def statistics():
    print(f'====== {name} GAME STATISTICS ======')
    print(f'Games Played: {games_played}')
    print(f'Games Won: {games_won}')
    print(f'Games Lost: {games_lost}')

    # Avoid dividing by zero if no games have been played yet
    if games_played > 0:
        win_percentage = (games_won/games_played) *100
    else:
        win_percentage = 0

    print(f'Win Percentage = {win_percentage}%')
    print(f'Total Score: {total_score}')

# Main loop: play rounds until the player chooses to stop
while True:
    game()

    play_again = input('Would you like to play again? (Yes/No): ').lower()

    if play_again == "yes":
        continue
    elif play_again == "no":
        statistics()
        print(f'Thanks for playing {name}! Goodbye!')
        break