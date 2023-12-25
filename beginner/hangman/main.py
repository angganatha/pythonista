import random
from typing import List
from colorama import Fore

WORDS = """Apple Banana Durian Rambutan Manggo"""
SCREEN_SIZE = 80
PUNISHMENTS = ['HEAD', 'BODY', 'LEFT HAND', 'RIGHT HAND', 'LEFT FOOT', 'RIGHT FOOT']

def punish(punishments: List[str]) -> List[str]:
    if PUNISHMENTS != punishments:
        punishments.append(PUNISHMENTS[len(punishments)])
    return punishments

def is_loose(punishments: List[str]) -> bool:
    return PUNISHMENTS == punishments

def is_win(disclosed: List[str], unique_count: int) -> bool:
    return len(disclosed) == unique_count

def displays(symbol: str, secret: str, disclosed: str) -> None:
    displays = []
    for i in secret:
        if i in disclosed:
            displays.append(i)
        else:
            displays.append(symbol)
    print(Fore.WHITE + ' '.join(displays))

def welcome_message():
    print(Fore.BLUE + '=' * SCREEN_SIZE)
    print(Fore.BLUE + 'Guess the word right'.upper().center(SCREEN_SIZE))
    print(Fore.BLUE + 'to quit anytime from your game play press CTRL + C'.upper().center(SCREEN_SIZE))
    print(Fore.BLUE + '=' * SCREEN_SIZE)

def guess() -> str:
    bet = input(Fore.WHITE + 'Your letter guess: ')
    bet = bet.upper().strip()
    return bet

def warn(prompt: str, punishments: List[str]) -> List[str]:
    punishments = punish(punishments)
    print(Fore.YELLOW + prompt)
    print(Fore.RED + f'You got your {punishments[-1]} hanged')
    return punishments

def main():
    words = [f.upper() for f in WORDS.split()]
    rounds, win, loose = 0,0,0

    while True:
        rounds += 1
        attempts = 0
        punishments = []
        disclosed = []
        secret_word = random.choice(words)
        unique_count = len(set(list(secret_word)))
    
        welcome_message()

        while True:
            if is_loose(punishments):
                loose += 1
                print(Fore.RED + f'You hanged! word is {secret_word} {attempts} attempts')
                break

            attempts += 1

            displays('*', secret_word, disclosed)
            bet = guess()

            if len(bet) > 1 or not bet:
                punishments = warn('Oops! one letter at a time', punishments)
                continue

            if bet in disclosed:
                punishments = warn('You have guessed this letter right', punishments)
                continue

            if bet not in secret_word:
                punishments = warn('Ouch! guess it better', punishments)
            else:
                disclosed.append(bet)
                if unique_count != len(disclosed):
                    print(Fore.GREEN + f'You got {secret_word.count(bet)} letter right! {unique_count-len(disclosed)} more to go')
                else:
                    win += 1
                    print(Fore.GREEN + 'Congrats! You win this round!')
                    print(Fore.CYAN + f'{rounds} games with {win} win and {loose} loose')
                    break

if __name__ == '__main__':
    main()
