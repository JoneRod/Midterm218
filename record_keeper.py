import pandas as pd

# Sample data to simulate a calculation history
data = {
    "Calculation": ["2 + 2", "3 * 5", "10 / 2", "15 - 4"],
    "Result": [4, 15, 5.0, 11]
}

# Create a DataFrame from the sample data
history = pd.DataFrame(data)

# Specify the filename to save the record
filename = 'calculation_history.csv'

# Save the DataFrame to a CSV file
history.to_csv(filename, index=False)

print(f"Calculation history saved to {filename}.")