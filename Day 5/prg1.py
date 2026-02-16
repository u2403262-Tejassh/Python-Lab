class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self,acc_num,holder):
        self.accounts[acc_num] = [holder,0]
    def deposit(self, acc_num, amount):
        self.accounts[acc_num][1] += amount
    def withdraw(self, acc_num, amount):
        if self.accounts[acc_num][1]<amount:
            print("\nInsufficient balance! Withdraw canceled.")
        else:
            self.accounts[acc_num][1] = self.accounts[acc_num][1]-amount
    def display(self, acc_num):
        print(f"\nAccount number: {acc_num}\nHolder name: {self.accounts[acc_num][0]}\nBalance: {self.accounts[acc_num][1]}")
SBI = Bank()
while True:
    choice = int(input("\nWelcome to SBI bank\n'1' to add new account\n'2' to deposit\n'3' to withdraw\n'4' to display account details\n'5' to exit\n\nEnter choice: "))
    if choice == 1:
        holder = input("Enter account holder name: ")
        while True:
            acc_num = int(input("Choose an account number: "))
            if acc_num in SBI.accounts.keys():
                print("Account number already taken, choose another.")
            else:
                SBI.create_account(acc_num, holder)
                break
    elif choice == 2:
        while True:
            acc_num = int(input("Enter account number: "))
            if acc_num not in SBI.accounts.keys():
                print("Account number not present, try again.")
            else:
                amount = int(input("Enter amount: "))
                SBI.deposit(acc_num, amount)
                break
    elif choice == 3:
        while True:
            acc_num = int(input("Enter account number: "))
            if acc_num not in SBI.accounts.keys():
                print("Account number not present, try again.")
            else:
                amount = int(input("Enter amount: "))
                SBI.withdraw(acc_num, amount)
                break
    elif choice == 4:
        while True:
            acc_num = int(input("Enter account number: "))
            if acc_num not in SBI.accounts.keys():
                print("Account number not present, try again.")
            else:
                SBI.display(acc_num)
                break
    elif choice == 5:
        break
    else:
        print("Invalid choice!")
