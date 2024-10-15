import csv
import os

class ScoreManager:
    def __init__(self, filename="game_history.csv"):
        """Initialize ScoreManager with a CSV file for saving/loading game results."""
        self.filename = filename
        self.scores = []
        
        # If the file already exists, load the game history from it
        if os.path.exists(self.filename):
            self.load_game_history()

    def save_game_result(self, player_name, moves, game_time):
        """
        Save the game result to the CSV file.
        
        Parameters:
        - player_name: The name of the player.
        - moves: The number of moves the player made.
        - game_time: The time taken by the player to finish the game.
        """
        try:
            # Open the file in append mode and write the result
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([player_name, moves, game_time])
            print("Game result saved successfully.")
        except Exception as e:
            # Handle any exceptions that occur during file write
            print(f"Error saving game result: {e}")

    def load_game_history(self):
        """
        Load the game history from the CSV file and store it in self.scores.
        """
        try:
            # Open the file in read mode and load all past game results
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                self.scores = list(reader)
            print("Game history loaded.")
        except FileNotFoundError:
            # Handle the case where the file does not exist
            print("No previous history found.")
        except Exception as e:
            # Catch any other exceptions during file reading
            print(f"Error loading game history: {e}")

    def calculate_score(self, moves):
        """
        Calculate the player's score based on the number of moves.
        
        Parameters:
        - moves: The number of moves the player took.
        
        Returns:
        - The calculated score (max score of 1000, reduced by 10 for each move).
        """
        try:
            max_score = 1000
            score = max_score - moves * 10
            return max(score, 0)  # Ensure the score doesn't go below 0
        except TypeError as e:
            # Handle the case where 'moves' is not a valid integer
            print(f"Error calculating score: {e}")
            return 0

    def get_scores(self):
        """
        Get the loaded game history.
        
        Returns:
        - A list of previous game scores.
        """
        try:
            return self.scores
        except Exception as e:
            # Catch any errors when accessing the scores
            print(f"Error retrieving scores: {e}")
            return []
