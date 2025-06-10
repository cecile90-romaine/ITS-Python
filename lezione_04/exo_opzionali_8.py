# esercizio_8:
"""
ATM Machine Simulator:

    Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
     Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction.
"""

# Function to simulate a simple ATM interface
def atm_simulator() -> None:
    # Initialize account balance to $1000.00
    balance: float = 1000.0

    # Infinite loop to keep showing the ATM menu until user exits
    while True:
        # Display the menu options
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")

        # Get the user's menu choice
        choice: str = str(input("Choose an option: "))

        # Handle deposit
        if choice == "1":
            amount: float = float(input("Enter deposit amount: "))
            balance += amount  # Add the deposit amount to the balance

        # Handle withdrawal
        elif choice == "2":
            amount: float = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount  # Subtract the withdrawal amount from balance
            else:
                print("Insufficient funds.")  # Prevent overdraft

        # Handle balance check
        elif choice == "3":
            print(f"Balance: ${balance:.2f}")  # Show current balance with 2 decimal places

        # Exit the ATM simulator
        elif choice == "4":
            break  # Exit the loop and end the function

        # Handle invalid menu options
        else:
            print("Invalid option.")  # Prompt user to try again

# Call the function to run the ATM simulator
atm_simulator()  # Uncomment to run interactively