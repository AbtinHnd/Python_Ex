import random

score = 0
while True:
    rand = random.randint(100, 1000)
    flag = False
    attem = 6
    print("\n Welcome to the Guessing Game")
    print("1. Play Game")
    print("2. score ")
    print('3. Exit Game')
    try:
        choice = int(input('what is your choice?'))
    except ValueError:
        print('Please enter a valid number')
        continue

    if choice == 1:
        while not flag and attem > 0:
            print("Guess Number in three digits: ")
            guess = int(input())
            if guess < 100 or guess > 999:
                print("Please enter a number in three digits")
                continue
            else:
                if guess == rand:
                    print("( ** <3 Congratulations! You have guessed the number <3 **)")
                    flag = True
                    print(f'You have {attem} attempts left')
                    score += 1
                elif guess < rand:
                    print("Your guess is lower than the number")
                    attem -= 1
                    print('|*' * attem)
                else:
                    print("Your guess is higher than the number")
                    attem -= 1
                    print('|*' * attem)
                if attem == 0:
                    print("You have exhausted all your attempts and you LOSE :(( ")
                    print(f'The number was {rand}')
                    flag = True
    if choice == 2:
        print(f'Your score is {score}')
    if choice == 3:
        print('Goodbye')
        break
    else:
        print('Please enter a valid number')
        continue



