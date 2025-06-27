import random
import pandas as pd 

print("Welcome to Rock Paper Scissors!")
username = input("What is your username?\n")
print("Let's start " + username + "!")

try:
    df = pd.read_excel(f"{username}.xlsx")
except FileNotFoundError:
    df = pd.DataFrame([[0,0,0,0,0,0,0]],columns = ['Games Won', 'Games Lost', 'Series Won', 'Series Lost',
                                  'Rock Choosen', 'Paper Choosen', 'Scissors Choosen'])
    
playing_over = True
while playing_over: 

    play_stats = int(input("Menu: \n 1: Play \n 2: Stats \n 3: Exit\n"))

    if play_stats == 1:

        player_wins = 0
        computer_wins = 0
        game_over = False 

        while not game_over:
            computer_choice = random.randint(0,2)
            player_choice = input("What is your choice?\n")

            if player_choice.lower() == 'rock':
                if computer_choice == 0:
                    print("The computer choose rock, it's a tie.")
                    print(f"The series is {player_wins} to {computer_wins}!")
                    df['Rock Choosen'] = df['Rock Choosen'] + 1

                elif computer_choice == 1:
                    print("The computer choose paper, you lose!")
                    computer_wins = computer_wins + 1
                    print(f"The series is {player_wins} to {computer_wins}!")
                    df['Rock Choosen'] = df['Rock Choosen'] + 1
                    df['Games Lost'] = df['Games Lost'] + 1
                elif computer_choice == 2:
                    print("The computer choose scissors, you win!")
                    player_wins = player_wins + 1
                    print(f"The series is {player_wins} to {computer_wins}!")
                    df['Rock Choosen'] = df['Rock Choosen'] + 1
                    df['Games Won'] = df['Games Won'] + 1

            elif player_choice.lower() == 'paper':
                if computer_choice == 0:
                    print("The computer choose rock, you win!")
                    player_wins = player_wins + 1
                    print(f"The series is {player_wins} to {computer_wins}!")
                    df['Paper Choosen'] = df['Paper Choosen'] + 1
                    df['Games Won'] = df['Games Won'] + 1
                elif computer_choice == 1:
                    print("The computer choose paper, it's a tie.")
                    print(f"The series is {player_wins} to {computer_wins}!")
                    df['Paper Choosen'] = df['Paper Choosen'] + 1
                elif computer_choice == 2:
                    print("The computer choose scissors, you lose!")
                    computer_wins = computer_wins + 1
                    print(f"The series is {player_wins} to {computer_wins}!")
                    df['Paper Choosen'] = df['Paper Choosen'] + 1
                    df['Games Lost'] = df['Games Lost'] + 1

            elif player_choice.lower() == 'scissors':
                if computer_choice == 0:
                    print("The computer choose rock, you lose!")
                    computer_wins = computer_wins + 1
                    df['Scissors Choosen'] = df['Scissors Choosen'] + 1
                    df['Games Lost'] = df['Games Lost'] + 1
                    print(f"The series is {player_wins} to {computer_wins}!")

                elif computer_choice == 1:
                    print("The computer choose paper, you win!")
                    player_wins = player_wins + 1
                    df['Scissors Choosen'] = df['Scissors Choosen'] + 1
                    df['Games Won'] = df['Games Won'] + 1
                    print(f"The series is {player_wins} to {computer_wins}!")

                elif computer_choice == 2:
                    print("The computer choose scissors, it's a tie.")
                    print(f"The series is {player_wins} to {computer_wins}!")
                    df['Scissors Choosen'] = df['Scissors Choosen'] + 1
            else:
                print("Error please choose Rock, Paper, or Scissors")
    
            if player_wins == 4:
                print("Congratulations " + username + "! You won the series!") 
                df['Series Won'] = df['Series Won'] + 1
                game_over = True
                playing = input("Do you want to keep playing (yes/no)?")
                if playing.lower() == 'yes':
                    playing_over = True
                elif playing.lower() == 'no':
                    playing_over = False
                else:
                    print("Error: Choose Yes or No")
            
            if computer_wins == 4:
                print("Sorry " + username + " you lost the series")
                df['Series Lost'] = df['Series Lost'] + 1
                game_over = True
                
                playing = input("Do you want to keep playing (yes/no)?\n")
                if playing.lower() == 'yes':
                    playing_over = True
                elif playing.lower() == 'no':
                    playing_over = False
                else:
                    print("Error: Choose Yes or No")

    elif play_stats == 2:
        print(df)
        erase = int(input("Keep or erase stats?\n 1. Keep\n 2. Erase"))
        if erase == 1:
            continue
        elif erase == 2:
            for col in df.columns:
                df[col].values[:] = 0
        else:
            print("Error: Please Choose 1 or 2")

        playing = input("Do you want to keep playing (yes/no)?")
        if playing.lower() == 'yes':
            playing_over = True
        elif playing.lower() == 'no':
            playing_over = False
        else:
            print("Error: Choose Yes or No")
    elif play_stats == 3:
        playing_over = False
    else:
        print("Error: Choose 1, 2, 3")

df.to_excel(f"{username}.xlsx", index=False)
print(f"Thanks for playing {username} come again soon!")
