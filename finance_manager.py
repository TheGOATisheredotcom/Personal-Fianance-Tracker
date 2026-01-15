import datetime as dt

from numpy import rint
CATEGORIES = ["Food", "Rent", "Salary", "Entertainment", "Utilities", "Other"]

class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.expense_goals = {} 

    def select_category(self):
        print("\n--- Select a Category ---")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}. {cat}")
        while True:
            try:
                choice = int(input("Choose a category number: "))
                if 1 <= choice <= len(CATEGORIES):
                    return CATEGORIES[choice - 1]
                else:
                    print(f"Please select a number between 1 and {len(CATEGORIES)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def select_type(self):
        print("\n--- Select Transaction Type ---")
        print("1. Income")
        print("2. Expense")
        
        while True:
            choice = input("Choose (1 or 2): ").strip()
            if choice == '1':
                return "Income"
            elif choice == '2':
                return "Expense"
            print("Invalid choice. Enter 1 or 2.")

    def add_transaction(self):
        while True:
            try:
                amount = float(input("Enter amount: ")) # Changed to float for cents/decimals
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue # Restart the loop to ask for amount again
                break # Valid amount, move to the next field
            except ValueError:
                print("Amount must be a number, try again.")

        description = input("Enter a description: ").strip()

        category = self.select_category()
        
        trans_type = self.select_type()

        # Gets current date and formats it as a string YYYY-MM-DD
        date = dt.datetime.today().strftime('%Y-%m-%d')

        # Create the object (Ensure the order matches your Transaction class!)
        from transaction import Transaction # Assuming it's in transaction.py
        new_tx = Transaction(date, description, category, amount, trans_type)
        
        # ADD to the list, don't replace the list
        self.transactions.append(new_tx)
        print("Transaction added successfully!")
        return True
    
    def delete_transaction(self):
        if not self.transactions:
            print("No transactions to delete.")
            return False
        
        self.view_transactions()
        
        while True:
            try:
                index = int(input("Enter the transaction number to delete (0 to cancel): "))
                if index == 0:
                    print("Deletion cancelled.")
                    return False
                elif 1 <= index <= len(self.transactions):
                    deleted_tx = self.transactions.pop(index - 1)
                    print(f"Deleted transaction: {deleted_tx.description}, Amount: ${deleted_tx.amount:.2f}")
                    return True
                else:
                    print(f"Please enter a number between 1 and {len(self.transactions)}, or 0 to cancel.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    def get_balance(self):
        total = 0
        for tx in self.transactions:
            # Ensure the string matches the casing used in add_transaction
            if tx.type == "Income":
                total += tx.amount
            elif tx.type == "Expense":
                total -= tx.amount
        return total
    
    def view_transactions(self):
        if not self.transactions:
            print("No transactions to print.")

        else:
            print("\n" + "-" * 60)
            print(f"{'Count':<5} {'Date':<12} {'Description':<20} {'Category':<12} {'Amount':<10}")
            print("-" * 60)
            count = 0
            for tx in self.transactions:
                count += 1
                amount = tx.amount if tx.type == 'Income' else -tx.amount

                print(f"{count:<5} {tx.date:<12} {tx.description:<20} {tx.category:<12} ${amount:>8.2f}")
            
            print("-" * 60)

    def view_by_category(self):
        if not self.transactions:
            print("No transactions to print.")
            return
        
        category_totals = {}

        for tx in self.transactions:
            category = tx.category
            amount = tx.amount if tx.type == 'Income' else -tx.amount

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
            
        print("\n" + "-" * 40)

        for cat, total in category_totals.items():
            sign = "+" if total >= 0 else ""
            print(f"{cat:<15}: {sign}${total:.2f}")

    
    def view_by_date(self):
        date_str = input("Enter date to filter by (YYYY-MM-DD): ").strip()

        """View transactions for a specific date (YYYY-MM-DD)."""
        filtered_txs = [tx for tx in self.transactions if tx.date == date_str]
        
        if not filtered_txs:
            print(f"No transactions found for {date_str}.")
            return
        
        print(f"\nTransactions for {date_str}:")
        print("-" * 60)
        print(f"{'Count':<5} {'Description':<20} {'Category':<12} {'Amount':<10}")
        print("-" * 60)
        
        count = 0
        for tx in filtered_txs:
            count += 1
            amount = tx.amount if tx.type == 'Income' else -tx.amount
            print(f"{count:<5} {tx.description:<20} {tx.category:<12} ${amount:>8.2f}")
        
        print("-" * 60)

    def set_expense_goal(self):
        category = self.select_category()
        
        while True:
            try:
                goal_amount = float(input(f"Set expense goal for {category}: "))
                if goal_amount <= 0:
                    print("Goal amount must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        self.expense_goals[category] = goal_amount
        print(f"Expense goal of ${goal_amount:.2f} set for category '{category}'.")
        return True
    
    def view_expense_goals(self):
        if not self.expense_goals:
            print("No expense goals set.")
            return
        
        count = 0
        print("\n--- Expense Goals ---")
        for category, goal in self.expense_goals.items():
            count += 1
            print(f"{count}. {category}: ${goal:.2f}")
    
    def check_expense_goals(self):
        if not self.expense_goals:
            print("No expense goals set.")
            return
        
        category_totals = {}
        for tx in self.transactions:
            if tx.type == 'Expense':
                category_totals[tx.category] = category_totals.get(tx.category, 0) + tx.amount

        print("\n--- Goal Progress Report ---")
        print(f"{'Category':<15} {'Spent':<10} {'Goal':<10} {'Status':<15}")
        print("-" * 55)

        # 2. Compare totals to goals
        for cat, goal in self.expense_goals.items():
            spent = category_totals.get(cat, 0)
            remaining = goal - spent
            
            if remaining < 0:
                status = "⚠️ OVER LIMIT"
            else:
                status = "✅ UNDER GOAL"
                
            print(f"{cat:<15} ${spent:>8.2f} / ${goal:>8.2f} {status}")
