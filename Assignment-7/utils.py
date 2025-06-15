import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def choice(msg, choices: list):
    print()
    print('\n'.join([f'[{choices.index(choice)}] {choice}' for choice in choices]))
    print()
    return choices[int(input(msg + ' -> '))]