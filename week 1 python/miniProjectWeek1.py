# Initial accounts database (Simulating a real system)
account_data = {
    "balance": 5000.0,
    "pin": "1234"
}

def login():
    """Handles user PIN verification with a maximum of 3 attempts."""
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == account_data["pin"]:
            print("\n✓ Login Successful!")
            return True
        else:
            attempts -= 1
            print(f"✗ Incorrect PIN. Attempts remaining: {attempts}")
    
    print("\nToo many incorrect attempts. Card blocked!")
    return False

def check_balance():
    """Displays the current balance."""
    print(f"\nYour current balance is: ₹{account_data['balance']:.2f}")

def deposit():
    """Handles depositing money into the account."""
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            account_data["balance"] += amount
            print(f"✓ Successfully deposited ₹{amount:.2f}")
            check_balance()
        else:
            print("✗ Deposit amount must be greater than zero.")
    except ValueError:
        print("✗ Invalid input. Please enter a valid number.")

def withdraw():
    """Handles withdrawing money with balance validation."""
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("✗ Withdrawal amount must be greater than zero.")
        elif amount > account_data["balance"]:
            print("✗ Insufficient funds!")
        else:
            account_data["balance"] -= amount
            print(f"✓ Successfully withdrew ₹{amount:.2f}")
            check_balance()
    except ValueError:
        print("✗ Invalid input. Please enter a valid number.")

def atm_main():
    """Main function controlling the ATM interface loop."""
    print("=== Welcome to the Automated Teller Machine ===")
    if not login():
        return
        
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("\nThank you for using our ATM services. Goodbye!")
            break
        else:
            print("✗ Invalid choice. Please select a valid option from the menu.")

# Run the ATM Simulation
if __name__ == "__main__":
    atm_main()