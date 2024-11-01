import sys
from app.commands import Command
import logging

class MenuCommand(Command):
    def execute(self):
        print("\nAvailable commands:")
        print("1. add - Add two numbers")
        print("2. subtract - Subtract two numbers")
        print("3. multiply - Multiply two numbers")
        print("4. divide - Divide two numbers")
        print("5. exit - Exit the program")