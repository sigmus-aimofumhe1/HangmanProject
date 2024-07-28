import random

# Get the words from the hangman_words list
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user enters a letter already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}. Try again!")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess}; that's not in the chosen word. You lose a life.")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("Sorry, you lose!")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("Congratulations, you win!")

   # Import the stages from hangman_art.py and make this error go away.
   # from hangman_art import stages. This has been done in line 13

    print(stages[lives])