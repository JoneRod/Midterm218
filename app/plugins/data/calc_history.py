from app.commands import Command
import pandas as pd
import logging

class Calculations(Command):
    def __init__(self):
        self.history = pd.DataFrame(columns=["Calculation", "Result"])

    @classmethod
    def add_to_history(self, calculation, result):
        global history
        new_entry = pd.DataFrame([[calculation, result]], columns=["Calculation", "Result"])
        self.history = pd.concat([history, new_entry], ignore_index=True)
        print("Calculation added to history.")

    @classmethod
    def save_history(self, filename='calculation_history.csv'):
        global history
        self.history.to_csv(filename, index=False)
        print(f"History saved to {filename}.")
    
    @classmethod
    def load_history(self, filename='calculation_history.csv'):
        global history
        try:
            self.history = pd.read_csv(filename)
            print(f"History loaded from {filename}.")
        except FileNotFoundError:
            print("File not found. Please check the filename or save the history first.")
    
    @classmethod
    def clear_history(self):
        global history
        self.history = pd.DataFrame(columns=["Calculation", "Result"])
        print("History cleared.")