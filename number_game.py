import random
import json
import os
import time
from typing import Dict, Any, List

class NumberGame:
    def __init__(self):
        self.scores_file = "scores.json"
        self.difficulties = {
            1: {"name": "Easy", "range": 50, "attempts": 15, "hints": 2},
            2: {"name": "Medium", "range": 100, "attempts": 10, "hints": 1},
            3: {"name": "Hard", "range": 200, "attempts": 8, "hints": 0}
        }
        self._ensure_scores_file()

    def _ensure_scores_file(self) -> None:
        """Create scores file if it doesn't exist."""
        if not os.path.exists(self.scores_file):
            with open(self.scores_file, 'w') as f:
                json.dump({"scores": []}, f)

    def _save_score(self, player: str, score: int, difficulty: str) -> None:
        """Save score to file."""
        try:
            with open(self.scores_file, 'r') as f:
                data = json.load(f)
            data["scores"].append({
                "player": player,
                "score": score,
                "difficulty": difficulty,
                "date": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            data["scores"].sort(key=lambda x: x["score"], reverse=True)
            data["scores"] = data["scores"][:10]  # Keep top 10 scores
            with open(self.scores_file, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"\nError saving score: {e}")

    def _show_high_scores(self) -> None:
        """Display high scores."""
        try:
            with open(self.scores_file, 'r') as f:
                data = json.load(f)
            
            if not data["scores"]:
                print("\nNo high scores yet!")
                return

            print("\n=== High Scores ===")
            print(f"{'Rank':<6}{'Player':<20}{'Score':<10}{'Difficulty':<15}")
            print("-" * 51)
            for i, score in enumerate(data["scores"][:10], 1):
                print(f"{i:<6}{score['player']:<20}{score['score']:<10}{score['difficulty']:<15}")
        except Exception as e:
            print(f"\nError loading scores: {e}")

    def _get_hint(self, secret: int, guess: int) -> str:
        """Get hint based on the difference between numbers."""
        diff = abs(secret - guess)
        if diff <= 10:
            return "You're very close! Within 10 numbers."
        elif diff <= 25:
            return "Getting warmer! Within 25 numbers."
        else:
            return "You're quite far! More than 25 numbers away."

    def play(self) -> None:
        """Main game loop."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== Number Guessing Game ===\n")
        
        # Get player name
        while True:
            player_name = input("Enter your name: ").strip()
            if player_name:
                break
            print("\nName cannot be empty!")

        # Choose difficulty
        print("\nDifficulty Levels:")
        for level, settings in self.difficulties.items():
            print(f"{level}. {settings['name']} (1-{settings['range']}, {settings['attempts']} attempts, {settings['hints']} hints)")
        
        while True:
            try:
                difficulty = int(input("\nChoose difficulty (1-3): "))
                if difficulty in self.difficulties:
                    break
                print("\nPlease enter a number between 1 and 3.")
            except ValueError:
                print("\nPlease enter a valid number.")

        settings = self.difficulties[difficulty]
        secret_number = random.randint(1, settings['range'])
        attempts = 0
        hints_remaining = settings['hints']
        start_time = time.time()

        while attempts < settings['attempts']:
            print(f"\nAttempts: {attempts}/{settings['attempts']}")
            print(f"Hints remaining: {hints_remaining}")
            
            guess_input = input("\nEnter your guess (or 'h' for hint): ").strip().lower()
            
            if guess_input == 'h':
                if hints_remaining > 0:
                    if attempts > 0:
                        print(f"\nHint: {self._get_hint(secret_number, last_guess)}")
                    else:
                        print("\nMake a guess first to get a hint!")
                    hints_remaining -= 1
                else:
                    print("\nNo hints remaining!")
                continue

            try:
                guess = int(guess_input)
                last_guess = guess
            except ValueError:
                print("\nPlease enter a valid number!")
                continue

            attempts += 1

            if guess == secret_number:
                time_taken = time.time() - start_time
                score = int(settings['range'] - (attempts * 10) - (time_taken * 5))
                score = max(0, score)  # Ensure score doesn't go negative
                
                print(f"\n🎉 Congratulations! You've guessed the number in {attempts} attempts!")
                print(f"Time taken: {time_taken:.2f} seconds")
                print(f"Score: {score}")
                
                self._save_score(player_name, score, settings['name'])
                self._show_high_scores()
                break
            elif guess < secret_number:
                print("\nToo low!")
            else:
                print("\nToo high!")

        if attempts >= settings['attempts']:
            print(f"\n😢 Game Over! The number was {secret_number}")

        if input("\nPlay again? (yes/no): ").lower() != 'yes':
            print("\nThanks for playing! Goodbye!")
            return
        
        self.play()  # Play again

if __name__ == "__main__":
    game = NumberGame()
    game.play() 