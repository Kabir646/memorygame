import csv
import os

class ScoreManager:
    def __init__(self, filename="game_history.csv"):
        self.filename = filename
        self.scores = []
        if os.path.exists(self.filename):
            self.load_game_history()

    def save_game_result(self, player_name, moves, game_time):
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([player_name, moves, game_time])
            print("Game result saved successfully.")
        except Exception as e:
            print(f"Error saving game result: {e}")

    def load_game_history(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                self.scores = list(reader)
            print("Game history loaded.")
        except FileNotFoundError:
            print("No previous history found.")
        except Exception as e:
            print(f"Error loading game history: {e}")

    def calculate_score(self, moves):
        max_score = 1000
        score = max_score - moves * 10
        return max(score, 0)

    def get_scores(self):
        return self.scores
