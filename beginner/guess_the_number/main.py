import math
import random
from typing import Optional

from colorama import Fore

SCREEN_WIDTH = 80

def info(message: str) -> None:
    print(Fore.BLUE + message)

def error(message: str) -> None:
     print(Fore.RED + '[x] ' + message)

def success(message: str) -> None:
    print(Fore.GREEN + '[+] ' + message)


def get_user_input(prompt: str, gt: Optional[int] = None) -> int:
    while True:
        i = input(prompt)
        try:
            i = int(i)
            if gt and gt >= i:
                error(f'please input number greater than {gt}')
                continue
        except ValueError:
            error('please input a whole number')
        else:
            break
    return i

def welcome_message():
    info('=' * SCREEN_WIDTH)
    info('Welcome to guess the number game'.center(SCREEN_WIDTH))
    info('Your mission is to guess the randomized secret number'.center(SCREEN_WIDTH))
    info('press ctrl + c to exit from any stage of your game play'.center(SCREEN_WIDTH))
    print('=' * SCREEN_WIDTH)

def main():
    welcome_message()
    
    counter, win, loose = 0, 0, 0

    while True:
        counter += 1

        info(f'[ ROUND {counter} ]'.center(SCREEN_WIDTH))
        info('-' * SCREEN_WIDTH)

        lower_bound = get_user_input(Fore.YELLOW + 'set the lower bound number: ')
        upper_bound = get_user_input(Fore.YELLOW + 'set the upper bound number: ', lower_bound)

        max_attempts = math.ceil(math.log(upper_bound-lower_bound+1, 2))
        secret_number = random.randint(lower_bound, upper_bound)

        info(f'Your mission is to guess the secret number from {lower_bound} to {upper_bound} in maxmium {max_attempts} attempts')
        
        total_attempts = 0
        while total_attempts < max_attempts:
            attempt = get_user_input(Fore.YELLOW + 'guess the number: ')
            total_attempts += 1
            if attempt == secret_number:
                win += 1
                success(f'You WIN! in {total_attempts} attempt(s)')
                break
            
            if total_attempts == max_attempts:
                loose += 1
                error(f"You Loose! secret number is {secret_number}")
            else:
                if attempt > secret_number:
                     error(f'oops! try to lower it down')
                else:
                     error(f'oops! make it higher')

        info('-' * SCREEN_WIDTH)
        info(f'{counter} games played with {win} win and {loose} loose')
        info('-' * SCREEN_WIDTH)


if __name__ == '__main__':
    main()
