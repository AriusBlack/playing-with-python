#!/usr/bin/env python3


def hangman(max_tries, word):
    tries = 0
    guesses = []

    word_show = list("-"*len(word))
    word_to_find = [c for c in word]

    while tries < max_tries:
        if word_show != list(word):
            guess = input("Guess a letter:  ")
            if len(guess) > 1 or len(guess) < 0:
                print("Please enter a single letter")
                continue

            if guess not in word and guess not in guesses:
                guesses.append(guess)
                tries += 1
                print("The letter {} is not in the secret word. You have {} tries left.".format(guess, max_tries-tries))
            elif guess in guesses:
                print("""You have already tried that letter. Your guesses :
                {}""".format(guesses))
            elif guess in word_to_find and guess not in guesses:
                word_show[word_to_find.index(guess)] = guess
                word_to_find[word_to_find.index(guess)] = ' '
                print("""Well done, keep going. You have so far found :
                {}""".format(word_show))
        else:
            print("You win!")
            break
    print("The word was {}, you guessed {}".format(word, word_show.join('')))


def play():
    again = 'Y'
    while again.lower() == 'Y':
        print("This is a hangman game, you need to find the word in 7 tries")
        hangman(7, "oregon")
        #To Fix : catch NameError
        again = input("Would you like to play again? Y/n")
    print("Bye!")


play()
