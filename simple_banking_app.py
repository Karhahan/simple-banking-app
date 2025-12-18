balance = 0.0
kyc_documents = {}

def check_balance():
    print("Checking balance ....")
    print(f"Your balance is {balance}")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Cannot withdraw the amount")
    elif amount > balance:
        print("You don't have enough money")
    else:
        balance -= amount
        print(f"The amount {amount} has been withdrawn, new balance is {balance}")

def deposit(amount):
    global balance
    if amount <= 0:
        print("Cannot deposit the amount")
    else:
        balance += amount   # FIXED HERE
        print(f"The amount {amount} has been deposited. New balance is {balance}")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if not kyc_documents:
        print("No KYC documents found")
    else:
        print("KYC Documents:")
        for doc, value in kyc_documents.items():
            print(f"{doc} : {value}")

# ✅ MAIN PROGRAM
if __name__ == "__main__":

    while True:
        print("-----------------------------------")
        print("Welcome to the Simple Banking App")
        print("-----------------------------------")
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Update KYC")
        print("5. Check KYC")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_balance()

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)

        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)

        elif choice == '4':
            doc_name = input("Enter document name: ")
            doc_value = input("Enter document value: ")
            update_kyc({doc_name: doc_value})
            print("KYC updated successfully")

        elif choice == '5':
            check_kyc()

        elif choice == '6':
            print("Thank you for using the banking app")
            break

        else:
            print("Invalid choice")
