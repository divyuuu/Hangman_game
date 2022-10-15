# Step 5

import random
import hangman_art
import hangman_words


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
guess_words = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()



    if guess in guess_words:
        print(f"{guess} is already guessed by you.")
    guess_words += guess
    # print(guess_words)
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:

        lives -= 1
        print("You have guessed wrong. You lose one life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
