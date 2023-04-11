import random

user_score = 0
system_score = 0

print('User E Mohtaram!')
print('please choose a valid answer!')
print('valid answers are:')
print('   Rock:  Rock, rock, R & r ...')
print('   Paper:  Paper, paper, P & p ...')
print('   Scissors:  Scissors, scissors, S & s ...')

while True:
    while True:
        user_choice = input('Enter your choice: ')
    
        if user_choice == 'Rock' or user_choice == 'rock' or user_choice == 'R' or user_choice == 'r':
            user_choice = 'Rock'
            print('Your Choice:', user_choice)
            break

        elif user_choice == 'Paper' or user_choice == 'paper' or user_choice == 'P' or user_choice == 'p':
            user_choice = 'Paper'
            print('Your Choice:', user_choice)
            break

        elif user_choice == 'Scissors' or user_choice == 'scissors' or user_choice == 'S' or user_choice == 's':
            user_choice = 'Scissors'
            print('Your Choice:', user_choice)
            break

        else:
            print('your input is not correct.')
    
    valid_answers = ['Rock', 'Paper', 'Scissors']
    system_choice = random.choice(valid_answers)
    print('System Choice:', system_choice)

    if user_choice == system_choice:
        print('Result: Equal !')
        
    if user_choice == 'Rock':
        if system_choice == 'Scissors':
            print('Result: You won !')
            user_score = user_score + 1
        if system_choice == 'Paper':
            print('Result: System won !')
            system_score = system_score + 1

    if user_choice == 'Paper':
        if system_choice == 'Rock':
            print('Result: You won !')
            user_score = user_score + 1
        if system_choice == 'Scissors':
            print('Result: System won !')
            system_score = system_score + 1

    if user_choice == 'Scissors':
        if system_choice == 'Paper':
            print('Result: You won !')
            user_score = user_score + 1
        if system_choice == 'Rock':
            print('Result: System won !')
            system_score = system_score + 1
        
    if user_score == 3 or system_score == 3:
        break

    print('Your score is =', user_score)
    print('System score is =', system_score)

    print('----------------------------')
    
print('Your score is =', user_score)
print('System score is =', system_score)

print('----------------------------')
print('----------------------------')

if user_score == 3:
    print('Final winner is YOU !')
if system_score == 3:
    print('Final winner is SYSTEM !')