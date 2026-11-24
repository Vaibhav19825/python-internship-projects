
import random
import os

max_attempts = 7


# ----- Guessing game -----

def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("That is not a whole number, try again.")
            continue

        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.")
        else:
            return guess


def play_round():
    number = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        if guess == number:
            score = 100 - (attempts - 1) * 10
            print("Correct! Attempts used:", attempts)
            print("Round score:", score)
            return score
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        print("Attempts left:", max_attempts - attempts)

    print("You are out of attempts. The number was", number)
    return 0


def play_game():
    total_score = 0
    best_score = 0
    rounds = 0
    playing = True

    while playing:
        score = play_round()
        rounds += 1
        total_score += score
        if score > best_score:
            best_score = score

        answer = input("Play again? (y/n): ")
        if answer.lower() != "y":
            playing = False

    print("\nRounds played:", rounds)
    print("Total score:", total_score)
    print("Best round score:", best_score)


# ----- Word counter -----

def read_file(filename):
    
    folder = os.path.dirname(__file__)
    path = os.path.join(folder, filename)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def count_words(text):
    counts = {}
    words = text.lower().split()
    for word in words:
        word = word.strip(".,!?;:'\"()")
        if word == "":
            continue
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts


def word_counter():
    filename = input("Enter file name (for example sample.txt): ")
    text = read_file(filename)

    if text is None:
        print("File not found.")
        return

    counts = count_words(text)
    if len(counts) == 0:
        print("The file is empty.")
        return

    
    pairs = []
    for word in counts:
        pairs.append((counts[word], word))
    pairs.sort(reverse=True)

    print("\nTotal words:", sum(counts.values()))
    print("Unique words:", len(counts))
    print("Top 10 words:")
    for i in range(min(10, len(pairs))):
        print(i + 1, pairs[i][1], "-", pairs[i][0])


# ----- Main menu -----

def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()