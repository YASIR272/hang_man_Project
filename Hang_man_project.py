import random

# List of words to guess
words = ['python', 'hangman', 'programming', 'developer', 'keyboard', 'function']

def play_hangman():
    word = random.choice(words)
    word_letters = set(word)
    guessed_letters = set()
    attempts = 6

    print("🎉 Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0 and word_letters:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("⛔ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong! You have {attempts} attempts left.")

        # Display current word state
        display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word:", ' '.join(display))

    if not word_letters:
        print("🎉 You guessed the word correctly! You win! 🏆")
    else:
        print(f"💀 You're out of attempts. The word was '{word}'. Better luck next time!")

# Run the game
play_hangman()
