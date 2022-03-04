play_another = "yes"
a = range(1,4)
while play_another == "yes":
    user1 = int(input("Player one, enter your choise:\n1 - Scissors\n2 - Paper\n3 - Rock: "))
    while user1 not in a:
        user1 = int(input("Player one, enter your choise:\n1 - Scissors\n2 - Paper\n3 - Rock: "))
    user2 = int(input("Player two, enter your choise:\n1 - Scissors\n2 - Paper\n3 - Rock: "))
    while user2 not in a:
        user2 = int(input("Player two, enter your choise:\n1 - Scissors\n2 - Paper\n3 - Rock: "))
    if user1 == user2:
        print("It's a tie!\n")
    elif user1 == 1:
        if user2 == 2:
            print("user1 win!\n")
        else:
            print("user2 win!\n")
    elif user1 == 2:
        if user2 == 1:
            print("user2 win!\n")
        else:
            print("user1 win!\n")
    elif user1 == 3:
        if user2 == 1:
            print("user1 win!\n")
        else:
            print("user2 win!\n")
    play_another = input("'yes' for another game, anything else to exit")