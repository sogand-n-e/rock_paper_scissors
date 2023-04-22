import random

user_name = str(input('Input your name: '))

round_counter = 1
user_score = 0
system_score = 0

final_result = []

print(user_name ,'E Mohtaram!')
print('Wellcome!')
print('please choose a valid answer!')
print('valid answers are:')
print('   Rock:  Rock, rock, R & r ...')
print('   Paper:  Paper, paper, P & p ...')
print('   Scissors:  Scissors, scissors, S & s ...')

print('----------------------------')

with open('attachment_modules_and_files/win_score.txt', 'r') as score_file:
    winer_score = int(score_file.read())

while True:
    while True:
        print('Round', round_counter)
        user_choice = input('Enter your choice: ')
    
        if user_choice == 'Rock' or user_choice == 'rock' or user_choice == 'R' or user_choice == 'r':
            user_choice = 'Rock'
            print(user_name,'choosed:', user_choice)
            round_counter = round_counter + 1
            break

        elif user_choice == 'Paper' or user_choice == 'paper' or user_choice == 'P' or user_choice == 'p':
            user_choice = 'Paper'
            print(user_name,'choosed:', user_choice)
            round_counter = round_counter + 1
            break

        elif user_choice == 'Scissors' or user_choice == 'scissors' or user_choice == 'S' or user_choice == 's':
            user_choice = 'Scissors'
            print(user_name,'choosed:', user_choice)
            round_counter = round_counter + 1
            break

        else:
            print('your input is not correct.')
    
    valid_answers = ['Rock', 'Paper', 'Scissors']
    system_choice = random.choice(valid_answers)
    print('System Choice:', system_choice)

    if user_choice == system_choice:
        result = 'Draw !'
        final_result.append('D')
        print(result)
        
    if user_choice == 'Rock':
        if system_choice == 'Scissors':
            result = user_name + ' won !'
            final_result.append('W')
            print(result)
            user_score = user_score + 1
        if system_choice == 'Paper':
            result = 'System won !'
            final_result.append('L')
            print(result)
            system_score = system_score + 1

    if user_choice == 'Paper':
        if system_choice == 'Rock':
            result = user_name + ' won !'
            final_result.append('W')
            print(result)
            user_score = user_score + 1
        if system_choice == 'Scissors':
            result = 'System won !'
            final_result.append('L')
            print(result)
            system_score = system_score + 1

    if user_choice == 'Scissors':
        if system_choice == 'Paper':
            result = user_name + ' won !'
            final_result.append('W')
            print(result)
            user_score = user_score + 1
        if system_choice == 'Rock':
            result = 'System won !'
            final_result.append('L')
            print(result)
            system_score = system_score + 1
        
    if user_score == winer_score or system_score == winer_score:
        break

    print(user_name, 'score is =', user_score)
    print('System score is =', system_score)

    print('----------------------------')
    
print(user_name, 'score is =', user_score)
print('System score is =', system_score)

print('----------------------------')
print('----------------------------')

if user_score == winer_score:
    print('Final winner is', user_name, '!')
if system_score == winer_score:
    print('Final winner is SYSTEM !')

for index, value in enumerate(final_result):
    print('Round ' + str(index + 1) + ':', value)