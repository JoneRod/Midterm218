from app import App
import pandas as pd

history = pd.DataFrame(columns=["Calculation", "Result"])

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_to_history(calculation, result):
        global history
        new_entry = pd.DataFrame([[calculation, result]], columns=["Calculation", "Result"])
        history = pd.concat([history, new_entry], ignore_index=True)
        print("Calculation added to history.")

    @classmethod
    def save_history(filename='calculation_history.csv'):
        global history
        history.to_csv(filename, index=False)
        print(f"History saved to {filename}.")
    
    @classmethod
    def load_history(filename='calculation_history.csv'):
        global history
        try:
            history = pd.read_csv(filename)
            print(f"History loaded from {filename}.")
        except FileNotFoundError:
            print("File not found. Please check the filename or save the history first.")
    
    @classmethod
    def clear_history():
        global history
        history = pd.DataFrame(columns=["Calculation", "Result"])
        print("History cleared.")