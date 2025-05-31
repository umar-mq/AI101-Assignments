import os

def print_with_clear(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(text)

def choose_option(title, options, prompt="Choose an option: "):
    print_with_clear(f"\033[31m{title}\033[0m")
    print()
    for option in options:
        print(f"\033[34m[{options.index(option)}]\033[0m \033[94m{option}\033[0m")
    print()
    choice = input(prompt)
    return options[int(choice)]