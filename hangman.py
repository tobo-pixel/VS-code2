word = "laptop"
dash = ["_","_","_","_","_","_"]
attempts = 10
while attempts > 0:
    guess = input("Guess a letter in the word: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                dash[i] = guess
            else:
                continue
        print(guess,"is a letter")
        print("".join(dash))    
        if list(word) == dash:
            print("You've guessed it")
            print("".join(dash),"was the word")
            break    
        else:
            continue
    else:
        attempts -= 1
        print("Wrong")
        print("".join(dash))
        print("You have",attempts,"attempts left")
else:
    print("You've used up your attempts")
    print("You lose")

    
