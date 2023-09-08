def hangman_game():

    name = input("What is your name? ")
    word = input("Enter the word for your friend :")
    print("Hello,"+name, "Hangman time")
    print("Start guessing ...")

    #variable for the game
    turns = 10
    failed = 0
    guesses = ""
    #word = "secret"      #word to be guessed
    while turns > 0:     #keep game running using loops
        if guesses == word:
          break
        for char in word:
            if char in guesses:
               print(char)
            else:
               print("_")
               failed += 1
        if failed == 0:
           print("You win!")
           break
        guess = input("Guess a charactor : ")
        guesses += guess
        if guess not in word:
           turns -= 1
           print("Wrong guess")
        print("You have" , +turns, "more guesses")
        if turns == 0:
           print("Game is over,you lost")
    check = input("Do you want to playagain Y?N?")
    if check == "Y":
        hangman_game()
        
hangman_game()
           
 
