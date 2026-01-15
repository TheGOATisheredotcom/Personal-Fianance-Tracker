"""
This module handles Persistent Storage for the application.
It ensures that transaction data is saved to and loaded from a local JSON file.
"""
import json
import os

# ---------------- File Configuration ----------------

# Determine the absolute path of the directory where this script is located.
# This ensures the 'transactions.json' file is created in the same folder as the code,
# preventing "File Not Found" errors regardless of where the program is run from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_n = os.path.join(BASE_DIR, "transactions.json")

# ---------------- Storage Functions ----------------

def load_file():
    try:
        with open(file_n, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} # Return empty dict to match our new Master structure
    
def save_file(students):
    """
    Writes the current student data to the JSON file.
    
    Args:
        students (dict): The dictionary of data (processed by export_data in main.py).
    """
    try:
        with open(file_n, 'w') as file:
            # Serialize the dictionary to JSON format with 4-space indentation
            # for human-readability.
            json.dump(students, file, indent=4)
            
    except Exception as e:
        # Catch-all for permission errors or hardware issues
        print(f"Error saving data: {e}")