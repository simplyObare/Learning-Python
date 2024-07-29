import random

def get_choices():
    player_choice = input('Enter a choice (rock, paper or scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}

    return choices

def check_win(player, computer):
    print(f'You chose: {player}, computer chose: {computer}')
    if player == computer:
        return "it's a tie!"
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors, YOU WIN!'
        else:
            return 'Paper covers rock, YOU LOSE!'
    elif player == 'paper':
        if computer == 'scissors':
            return 'Scissors cuts paper, YOU LOSE!'
        else:
            return 'Paper covers rock, YOU WIN!'
    elif player == 'scissors':
        if computer == 'rock':
            return 'Rock smashes scissors, YOU LOSE!'
        else:
            return 'Scissors cuts paper, YOU WIN!'

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)