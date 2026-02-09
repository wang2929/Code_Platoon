import random

class GuessingGame():
    def __init__(self, answer):
        self.answer = answer # GuessingGame(10) => self.answer = 10
        self.status = False # Status of the game (true - solved, false - not solved)
        
    def solved(self):
        return self.status # says if game is solved or not solved yet
    
    def guess(self, guess):
        try:
            guess = int(guess)
        except:
            return None
        if guess > self.answer:     # game.guess(20): 20 > 10
            return "high"
        elif guess < self.answer:   # game.guess(5) : 5 < 10
            return "low"
        else:
            self.status = True      # game.guess(10) : they won the game!
            return "correct"

def game_driver():
    # __init__ initializer/constructor call
    game = GuessingGame(10)

    # solved method call
    print(f"game.solved(): {game.solved()}")   # => False
    print(f"game.status: {game.status}")
    
    print(f"Guess 5: {game.guess(5)}")  # => 'low'
    print(f"Guess 20: {game.guess(20)}") # => 'high'
    print(f"Is the game done? {game.solved()}")   # => False
    print(f"Guess 10: {game.guess(10)}") # => 'correct'
    print(f"Is the game done? {game.solved()}")   # => True
    
    if (not game.solved()):
        return
        
    print("\n\nWelcome to the guessing game! Guess a number between 1 and 100.")
    game = GuessingGame(random.randint(1,100))
    last_guess  = None
    last_result = None

    while game.solved() == False:
        if last_guess != None: 
            print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
            print("")

        last_guess  = input("Enter your guess (1-100): ")
        last_result = game.guess(last_guess)
        
        if last_guess == "":
            return


    print(f"{last_guess} was correct!")
    
if __name__ == "__main__":
    game_driver()