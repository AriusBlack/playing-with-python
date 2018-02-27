# Need to catch the error on first guess without ''. Throws an UnboundLocalError.
guesses = []
max_tries = 7
word = "oregon"

def hangman():
    tries = 0
    word_to_find = list(word)
    word_show = "-"*len(word)
    word_show = list(word_show)
    while tries < max_tries:
        if word_show != list(word):
            try:
                guess = input("Guess a letter:  ")
                guess = str(guess).lower()
            except TypeError:
                print("Error retrieving your guess")
            except NameError and UnboundLocalError:
                print("Remember to add ' before and after your input")
            if guess not in word and guess not in guesses:
                guesses.append(guess)
                tries += 1
                print("The letter {} is not in the secret word, you have {} tries left".format(guess, str(max_tries-tries)))
            elif guess not in word and guess in guesses:
                print("""You have already tried that letter. Your guesses : 
                {}""".format(guesses))
            elif guess in word and guess in guesses:
                print("""You already tried that letter bou, you guesses so far :
                {}""".format(guesses))
            elif guess in word and guess not in guesses:
                while guess in word_to_find:
                    word_show[word_to_find.index(guess)] = guess
                    word_to_find[word_to_find.index(guess)] = ' '
                print("""Well done, keep going. You have so far found :
                {}""".format(word_show))
        else:
            print("You win!")
            break
    print("The word was {}, you found {}".format(word,word_show))



def play():
    again = 'Y'
    while again == 'Y':
        print("This is a hangman game, you need to find the word in 7 tries")
        hangman()
        #To Fix : catch NameError
        again = input("Would you like to play again? Y/n")
    print("Bye!")

play()

