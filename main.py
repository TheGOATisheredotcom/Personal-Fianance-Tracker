import sys
from storage import load_file, save_file
from menu import display_menu
from transaction import Transaction
from finance_manager import FinanceManager

# Initialize the global manager object to handle business logic
manager = FinanceManager()


# ---------------- Helper Functions ----------------
def export_data():
    return {
        "transactions": [tx.to_dict() for tx in manager.transactions],
        "expense_goals": manager.expense_goals
    }

def pause():
    """Pauses the program until the user presses Enter."""
    input("Press Enter to continue...")
# ---------------- Main Program Loop ----------------

def main():

    data = load_file()
    
    # Check if we actually got a dictionary (not an empty list from an old version)
    if isinstance(data, dict):
        # 1. Rehydrate Transactions
        raw_txs = data.get("transactions", [])
        for item in raw_txs:
            manager.transactions.append(Transaction.from_dict(item))
            
        # 2. Rehydrate Goals (Directly assign the dictionary)
        manager.expense_goals = data.get("expense_goals", {})
    
    while True:
        # Display the UI menu
        display_menu()
        
        try:
            choice = input("Choose an option: ").strip()
        except EOFError:
            # Handles unexpected program interruptions
            break
        
        if choice == '1':
            manager.add_transaction()
            save_file(export_data())
            pause()

        elif choice == '2':
            manager.delete_transaction()
            save_file(export_data())
            pause()

        elif choice == '3':
            balance = manager.get_balance()
            print(f"CURRENT BALANCE: ${balance:.2f}")
            pause()

        elif choice == '4':
            manager.view_transactions()
            save_file(export_data())
            pause()
        
        elif choice == '5':
            manager.view_by_category()
            save_file(export_data())
            pause()
        
        elif choice == '6':
            manager.view_by_date()
            save_file(export_data())
            pause()
        
        elif choice == '8':
            manager.set_expense_goal()
            save_file(export_data())
            pause()
        
        elif choice == '9':
            manager.view_expense_goals()
            pause()

        elif choice == '10':
            manager.check_expense_goals()
            pause()

        # CHOICE 11: Graceful Exit
        elif choice == '11':
            print("Exiting and saving data...")
            save_file(export_data()) # Final save before closing
            sys.exit()

        # ERROR HANDLING: Catches invalid menu inputs
        else:
            print("Invalid choice. Please select a valid option.")
            pause()

# Boilerplate to ensure main() only runs if the script is executed directly
if __name__ == "__main__":
    main()