import random


def choose_word():
    words = ["binary","method","string","debugs","syntax","branch", "script","module"]
    return random.choice(words)

def get_feedback(secret_word, guess):
  if len(guess) != len(secret_word):
    return "Invalid guess length"
  feedback = ""
  for i in range(len(secret_word)):
      if guess[i] == secret_word[i]:
          feedback += secret_word[i]
      elif guess[i] in secret_word:
          feedback += "x"
      else:
          feedback += "-"
  return feedback



def wordmind_game():
    secret_word = choose_word()
    attempts = 0
    while True:
        guess = input("Enter your guess: ").lower()

        if guess == secret_word:
            print("Congratulations! You guessed the word correctly.")
            break

        feedback = get_feedback(secret_word, guess)
        print("Feedback:", feedback)

        attempts += 1
        if attempts >= 6:
            print("Sorry, you've run out of attempts. The correct word was:", secret_word)
            break

def replay():
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again == "yes":
        return True
    else:
        print("Thanks for playing!")
        return False

def main():
    print("Welcome to Wordmind!")
    print("letter = right location of the letter")
    print("X = letter is in another location")
    print("- = no letter correct in that spot")
    
    while True:
        wordmind_game()
        if not replay():
            break

main()