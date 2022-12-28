import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
num_words = len(word_list)
chosen_word = word_list[random.randint(0, num_words - 1)]
chosen_word_length = len(chosen_word)
# Testing
print(f"The chosen word is {chosen_word}.")

# Create an empty list called display. For each letter in the chosen_word, add a "_" to "display".
display = []

for letter in chosen_word:
    display.append("_")

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Loop through each position in the chosen_word. If the letter at that position matches "guess", then reveal that letter in the display at that position.
    for i in range(chosen_word_length):
        if chosen_word[i] == guess:
            display[i] = guess

    # Join all the elements in the list and turn it into a string 
    print(f"{' '.join(display)}")

    # Check if the user has got all the letters
    if "_" not in display:
        end_of_game = True
        print("You win.")
