def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())
        displayed_word = "".join(
            [char if char.lower() in guesses else "_" for char in secret_word]
        )
        print(displayed_word)

        all_guessed = all(char.lower() in guesses for char in secret_word)
        return all_guessed

    return hangman_closure


if __name__ == "__main__":
    secret = input("Enter secret word: ")
    game = make_hangman(secret)
    is_complete = False

    while not is_complete:
        guess = input("Guess a letter: ")
        is_complete = game(guess)

    print("You guessed the word!")