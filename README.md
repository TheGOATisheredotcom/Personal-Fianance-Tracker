# Personal Finance Tracker

A robust Python command-line application designed to help users track spending, manage income, and set category-based expense goals.

## 🚀 Features
- **Transaction Management**: Add, view, and delete income or expense records.
- **Smart Categorization**: Use a guided selection menu to prevent typing errors.
- **Goal Tracking**: Set monthly spending limits per category (e.g., Food, Rent).
- **Progress Reports**: Real-time alerts showing if you are under or over your budget.
- **Persistent Storage**: All data is automatically saved to and loaded from a local JSON file.
- **Data Filtering**: Filter your financial history by specific dates.

## 🛠️ Project Structure
- `main.py`: The entry point and main application loop.
- `finance_manager.py`: Contains the core logic for calculations and data management.
- `transaction.py`: Defines the `Transaction` class and data serialization.
- `storage.py`: Handles file I/O operations for JSON persistence.
- `menu.py`: Manages the terminal user interface.

## 💻 How to Run
1. Ensure you have Python 3.x installed.
2. Clone this repository.
3. Run the application:
   ```bash
   python main.py