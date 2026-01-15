class Transaction:
    def __init__(self, date, description, category, amount, transaction_type):
        # We use 'transaction_type' because 'type' is a built-in Python function
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount
        self.type = transaction_type

    def to_dict(self):
        """Converts the object to a dictionary for JSON storage."""
        return {
            "date": self.date, # Added this so dates are saved!
            "description": self.description,
            "category": self.category,
            "amount": self.amount,
            "type": self.type
        }
    
    @classmethod
    def from_dict(cls, data):
        """Creates a Transaction object from a dictionary."""
        # Note: Since 'date' is now inside the dict, we don't need it as a separate argument
        return cls(
            data["date"], 
            data["description"], 
            data["category"], 
            data["amount"], 
            data["type"]
        )