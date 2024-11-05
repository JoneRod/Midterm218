## Calculation Application
# This project is a command-line-based calculation application that supports basic arithmetic operations (add, subtract, divide, multiply) through plugins. It also includes a menu plugin to display available commands and an exit plugin to quit the application. The application uses pandas to maintain a history of calculations, which can be saved to a CSV file, loaded from a file, and cleared when needed.

## Features
1. Basic arithmetic operations: add, subtract, divide, and multiply.
2. Command-based interface for flexibility and modularity.
3. Plugin architecture to allow for easy extension of commands.
4. Uses pandas to store a calculation history.
Ability to save, load, and clear calculation history

## Plugins
# This application uses a plugin-based architecture to support various commands. Below are descriptions of each plugin.

## Add Plugin
1. Command: add
2. Description: Prompts the user to input two numbers and returns their sum.
3. Usage: add (follow prompts for numbers)
# Subtract Plugin
1. Command: subtract
2. Description: Prompts the user to input two numbers and returns the result of subtracting the second number from the first.
3. Usage: subtract (follow prompts for numbers)
# Divide Plugin
1. Command: divide
2. Description: Prompts the user to input two numbers and returns the result of dividing the first number by the second. Handles division by zero gracefully.
3. Usage: divide (follow prompts for numbers)
# Multiply Plugin
1. Command: multiply
2. Description: Prompts the user to input two numbers and returns their product.
3. Usage: multiply (follow prompts for numbers)
## Menu Plugin
1. Command: menu
2. Description: Lists all available commands.
3. Usage: menu
## Exit Plugin
1. Command: exit
2. Description: Exits the application.
3. Usage: exit

## Current Issues
# I ain't great at coding so the plugin history frankly doesn't like me. 