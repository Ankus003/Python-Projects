import time

# Initial setup
password = 1223  # Pin number for the ATM
balance = 10000  # Initial balance
transaction_history = []  # Store transaction history

#All transactions are done and added here
def add_transaction(transaction):
    transaction_history.append(transaction) 

#All transactions are showed here using this function
def show_transaction_history():
    if transaction_history:
        print("Transaction History:")
        for transaction in transaction_history:
            print(transaction)
        print("================================================")
        print("================================================")
        print("================================================")
        
    else:
        print("No transactions yet.")
        print("================================================")
        print("================================================")
        print("================================================")

#For changing pin of ATM System.A global variable password is assigned so it can be used outside the function change_pin.
#Then an if-else loop runs to check the new pin is same as confirmed pin or not. 
def change_pin():
    global password
    new_pin = int(input("Enter your new 4-digit PIN: "))
    confirm_pin = int(input("Confirm your new PIN: "))
    
    if new_pin == confirm_pin:
        password = new_pin
        print("PIN successfully changed.")
        add_transaction("PIN changed")
        return True  # Indicating the PIN was changed successfully
        print("================================================")
        print("================================================")
        
       
    else:
        print("PIN confirmation does not match.")
        print("PIN change failed.")
        return False  # Indicating the PIN changed failed
        print("================================================")
        print("================================================")
    
# Here the main atm system is created. Here all functions are added in a single function using switch case where balance is checked,
# withdrawn balance, deposit balance, change pin, transaction history and exit when done logics are pushed.
def atm_system():
    global balance
    while True:
      pin = int(input("Enter your ATM pin: "))
    
      if pin == password:
         while True:
            print("""
                  1 == Check Balance
                  2 == Withdraw Balance
                  3 == Deposit Balance
                  4 == Change PIN
                  5 == Transaction History
                  6 == Exit
                  """)
            try:
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("Please enter a valid option.")
                continue  

            if option == 1:
                print(f"Your current balance is {balance}")
                print("================================================")
                print("================================================")
                print("================================================")

            elif option == 2:
                withdraw_amount = int(input("Please enter withdrawal amount: "))
                print("================================================")
                print("================================================")
                print("================================================")

                if withdraw_amount > balance:
                    print("Insufficient balance!")
                else:
                    balance = balance - withdraw_amount
                    print(f"{withdraw_amount} is debited from your account.")
                    print(f"Your current balance is {balance}")
                    add_transaction(f"Withdrawal: -{withdraw_amount}")
                    print("================================================")
                    print("================================================")
                

            elif option == 3:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance = balance + deposit_amount
                print(f"{deposit_amount} is credited to your account.")
                print(f"Your updated balance is {balance}")
                add_transaction(f"Deposit: +{deposit_amount}")
                print("================================================")
                print("================================================")

            elif option == 4:
                pin_changed = change_pin()
                if pin_changed:
                    # Ask user to enter the new PIN again
                    print("Please enter your new PIN to continue.")
                    break  # Break out of the inner loop to restart PIN prompt
                
            elif option == 5:
                show_transaction_history()

            elif option == 6:
                print("Exiting the ATM system. Have a nice day!")
                print("================================================")
                print("================================================")
                print("================================================")
                break
            

            else:
                print("Invalid option. Please choose a valid action.")
    else:
        print("Wrong PIN inserted")
        print("================================================")
        print("================================================")
        print("================================================")

# Running the ATM system function above
atm_system()
