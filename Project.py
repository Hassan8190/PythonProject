print(
    "\nWeclome to who wants to be a millionare, where you will puzzle through questions to win!\n"
)

player_name = input("What is your name? ")

print("Welcome " + player_name + ", We are glad to have you! Lets begin.\n")

player_winnings = 0
lost = 0
retry = 0
won = 0
again = 0
print(retry)
retry_yes = 0
while retry_yes == 0:
    while lost == 0:
        again = 0
        # QUESTION 1
        print(
            "\nThe first question is for 50000$. What is the capital of Canada? is it\n"
        )
        correct1 = "D"
        question_prize = 50000
        while retry == 0:
            print("A. Washington \nB. Edmonton \nC. Toronto \nD. Ottowa\n")
            answer1 = input(
                "Well " + player_name + ", what to you think? A,B,C or D? "
            ).upper()
            if answer1 == correct1:
                player_winnings += question_prize
                retry += 1
            elif answer1 in ["A", "B", "C", "D"]:
                retry += 1
                lost += 1
            else:
                print(
                    "\nSorry that isnt an option try again, you have to type either A,B,C or D\n"
                )
        if lost != 0:
            break
        retry -= 1
        cont = 0
        while cont == 0:
            continue_playing = input(
                "\nCongrats "
                + player_name
                + ", you are correct! You now have "
                + str(player_winnings)
                + "$. Would like to continue playing? Y/N "
            ).upper()

            if continue_playing == "Y":
                cont += 1
            elif continue_playing == "N":
                cont += 2
            else:
                print(
                    "Sorry that isnt an applicale answer, please try again, please type Y for yes and N for no.\n"
                )
        if cont == 2:
            retry_yes += 1
            again += 1
            lost += 1

        if lost != 0:
            break
        cont = 0
        # QUESTION 2
        print("The second question is for 100000$. What animal is a Mammal? is it\n")
        correct1 = "B"
        question_prize = 100000
        while retry == 0:
            print("A. Frog \nB. Whale \nC. Tuna \nD. A Toothbrush\n")
            answer1 = input(
                "Well " + player_name + ", what to you think? A,B,C or D? "
            ).upper()
            if answer1 == correct1:
                player_winnings += question_prize
                retry += 1
            elif answer1 in ["A", "B", "C", "D"]:
                retry += 1
                lost += 1
            else:
                print(
                    "\nSorry that isnt an option try again, you have to type either A,B,C or D\n"
                )
        if lost != 0:
            break
        cont = 0
        while cont == 0:
            continue_playing = input(
                "\nCongrats "
                + player_name
                + ", you are correct! You now have "
                + str(player_winnings)
                + "$. Would like to continue playing? Y/N "
            ).upper()

            if continue_playing == "Y":
                cont += 1
            elif continue_playing == "N":
                cont += 2
            else:
                print(
                    "Sorry that isnt an applicale answer, please try again, please type Y for yes and N for no.\n"
                )
        if cont == 2:
            retry_yes += 1
            again += 1
            lost += 1
        if lost != 0:
            break
        cont = 0
        retry = 0
        # QUESTION 3
        print("The second question is for 300000$. What is 50 x 24? is it\n")
        correct1 = "B"
        question_prize = 300000
        while retry == 0:
            print("A. 1100 \nB. 1200 \nC. 1250 \nD. 1400\n")
            answer1 = input(
                "Well " + player_name + ", what to you think? A,B,C or D? "
            ).upper()
            if answer1 == correct1:
                player_winnings += question_prize
                retry += 1
            elif answer1 in ["A", "B", "C", "D"]:
                retry += 1
                lost += 1
            else:
                print(
                    "\nSorry that isnt an option try again, you have to type either A,B,C or D\n"
                )

        cont = 0
        if lost == 0:
            while cont == 0:
                continue_playing = input(
                    "\nCongrats "
                    + player_name
                    + ", you are correct! You now have "
                    + str(player_winnings)
                    + "$. Would like to continue playing? Y/N "
                ).upper()

                if continue_playing == "Y":
                    cont += 1
                elif continue_playing == "N":
                    cont += 2
                else:
                    print(
                        "Sorry that isnt an applicale answer, please try again, please type Y for yes and N for no.\n"
                    )
        if cont == 2:
            retry_yes += 1
            again += 1
            lost += 1
        if lost != 0:
            break
        cont = 0
        retry = 0
        # QUESTION 4
        print(
            "\nThe fourth question is for 300000$. What year was Python created? is it\n"
        )
        correct1 = "C"
        question_prize = 300000
        while retry == 0:
            print("A. 2001 \nB. 1992 \nC. 1991 \nD. 1995\n")
            answer1 = input(
                "Well " + player_name + ", what to you think? A,B,C or D? "
            ).upper()
            if answer1 == correct1:
                player_winnings += question_prize
                retry += 1
            elif answer1 in ["A", "B", "C", "D"]:
                retry += 1
                lost += 1
            else:
                print(
                    "\nSorry that isnt an option try again, you have to type either A,B,C or D\n"
                )

        cont = 0
        if lost == 0:
            while cont == 0:
                continue_playing = input(
                    "\nCongrats "
                    + player_name
                    + ", you are correct! You now have "
                    + str(player_winnings)
                    + "$. Would like to continue playing? Y/N "
                ).upper()

                if continue_playing == "Y":
                    cont += 1
                elif continue_playing == "N":
                    cont += 2
                else:
                    print(
                        "Sorry that isnt an applicale answer, please try again, please type Y for yes and N for no.\n"
                    )
        if cont == 2:
            retry_yes += 1
            again += 1
            lost += 1
        if lost != 0:
            break
        cont = 0
        retry = 0
        # QUESTION 5
        print(
            "\nThe LAST question is for 250000$. What was the longest snake ever recorded? is it\n"
        )
        correct1 = "A"
        question_prize = 250000
        while retry == 0:
            print("A. 20ft \nB. 12ft \nC. 14ft \nD. 10ft\n")
            answer1 = input(
                "Well " + player_name + ", what to you think? A,B,C or D? "
            ).upper()
            if answer1 == correct1:
                player_winnings += question_prize
                retry += 1
            elif answer1 in ["A", "B", "C", "D"]:
                retry += 1
                lost += 1
            else:
                print(
                    "\nSorry that isnt an option try again, you have to type either A,B,C or D\n"
                )

        if lost != 0:
            break
        else:
            print("\nCongrats " + player_name + " you won 1 million dollars!")
            won += 1
            again = 1
            break

    if again != 0:
        break
    retry_yes = 0
    if lost == 1 and again == 0:
        retry_game = input(
            "\nIm sorry "
            + player_name
            + ", It looks like you lost, would you like to play again? Y/N "
        ).upper()
        while again == 0:
            if retry_game == "Y":
                retry_yes = 0
                again += 1
                player_winnings = 0
                lost = 0
                retry = 0
                won = 0
            elif retry_game == "N":
                retry_yes = 1
                again += 1
            else:
                print("Sorry that is not an applicable answer, please try again")
                again = 0


if lost == 2 and won == 0:
    print(
        "\nCongrats "
        + player_name
        + ", You won "
        + str(player_winnings)
        + "$. Congruglations!"
    )
