import json
import os

class MiniBank:
    def __init__(self):
        self.main_userInfo = {}
        self.load_data()

    def load_data(self):
        if os.path.exists("userlist.txt") and os.path.getsize("userlist.txt") > 0:
            with open("userlist.txt", "r") as file:
                try:
                    self.main_userInfo = json.load(file)
                except json.JSONDecodeError:
                    print("Error: userlist.txt is corrupted! Resetting data.")
                    self.main_userInfo = {}
        else:
            self.main_userInfo = {}

    def save_data(self):
        with open("userlist.txt", "w") as file:
            json.dump(self.main_userInfo, file, indent=4)

    def firstOpt(self):
        while True:
            try:
                option = int(input("\nPress 1 to Login\nPress 2 to Register\nChoice: "))
                if option == 1:
                    self.login()
                    break
                elif option == 2:
                    self.register()
                    break
                else:
                    print("Invalid choice! Please enter 1 or 2.")
            except ValueError:
                print("Please enter a valid number.")

    def returnId(self, transfer_uname):
        for user_id, user_data in self.main_userInfo.items():
            if user_data["r_uname"] == transfer_uname:
                return user_id
        return None

    def menu(self, loginID):
        while True:
            try:
                menu_input = int(input("\nPress 1 to Transfer\nPress 2 to Withdraw\nPress 3 to Update\nPress 4 to Logout\nChoice: "))
                if menu_input == 1:
                    self.transfer(loginID)
                elif menu_input == 2:
                    self.withdraw(loginID)
                elif menu_input == 3:
                    self.update(loginID)
                elif menu_input == 4:
                    print("Logging out...\n")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1-4.")
            except ValueError:
                print("Please enter a valid number.")

    def transfer(self, loginID):
        print("\n--- Money Transfer ---")
        transfer_uname = input("Enter recipient username: ")

        if self.main_userInfo[loginID]["r_uname"] == transfer_uname:
            print("Error: You cannot transfer money to yourself!")
            return

        transfer_id = self.returnId(transfer_uname)
        if transfer_id is None:
            print("User not found!")
            return

        try:
            amount = int(input(f"Enter amount to transfer to {transfer_uname}: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            if self.main_userInfo[loginID]["amount"] >= amount:
                self.main_userInfo[loginID]["amount"] -= amount
                self.main_userInfo[transfer_id]["amount"] += amount
                self.save_data()
                print(f"Transfer successful! Your new balance is {self.main_userInfo[loginID]['amount']}")
            else:
                print("Insufficient balance!")
        except ValueError:
            print("Please enter a valid amount.")

    def withdraw(self, loginID):
        print("\n--- Withdraw Money ---")
        print("Your current balance:", self.main_userInfo[loginID]["amount"])

        try:
            withdraw_amount = int(input("Enter amount to withdraw: "))
            if withdraw_amount <= 0:
                print("Amount must be greater than zero.")
                return
            if self.main_userInfo[loginID]["amount"] >= withdraw_amount:
                self.main_userInfo[loginID]["amount"] -= withdraw_amount
                self.save_data()
                print(f"Withdrawal successful! Your new balance is {self.main_userInfo[loginID]['amount']}")
            else:
                print("Insufficient balance!")
        except ValueError:
            print("Please enter a valid amount.")

    def update(self, loginID):
        print("\n--- Update Account ---")
        try:
            update_option = int(input("Press 1 to Change Username\nPress 2 to Change Password\nPress 3 to Add Money\nChoice: "))
            if update_option == 1:
                new_username = input("Enter new username: ")
                self.main_userInfo[loginID]["r_uname"] = new_username
                self.save_data()
                print(f"Username updated successfully! New username: {new_username}")
            elif update_option == 2:
                current_passcode = int(input("Enter current passcode: "))
                if self.main_userInfo[loginID]["r_pcode"] == current_passcode:
                    new_passcode = int(input("Enter new passcode: "))
                    confirm_passcode = int(input("Confirm new passcode: "))
                    if new_passcode == confirm_passcode:
                        self.main_userInfo[loginID]["r_pcode"] = new_passcode
                        self.save_data()
                        print("Passcode updated successfully!")
                    else:
                        print("Passcodes do not match!")
                else:
                    print("Incorrect current passcode!")
            elif update_option == 3:
                additional_amount = int(input("Enter amount to add: "))
                if additional_amount > 0:
                    self.main_userInfo[loginID]["amount"] += additional_amount
                    self.save_data()
                    print(f"Amount updated successfully! New balance: {self.main_userInfo[loginID]['amount']}")
                else:
                    print("Amount must be greater than zero.")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")

    def login(self):
        print("\n--- User Login ---")
        l_uname = input("Enter username: ")
        try:
            l_pcode = int(input("Enter passcode: "))
        except ValueError:
            print("Invalid passcode!")
            return

        loginID = self.returnId(l_uname)
        if loginID and self.main_userInfo[loginID]["r_pcode"] == l_pcode:
            print("\n--- Login Successful ---\n")
            self.menu(loginID)
        else:
            print("Invalid username or passcode!")

    def register(self):
        print("\n--- User Registration ---")
        r_uname = input("Enter username: ")

        if self.returnId(r_uname):
            print("Error: Username already exists!")
            return

        try:
            r_amount = int(input("Enter initial deposit amount: "))
            if r_amount < 0:
                print("Amount cannot be negative!")
                return
            r_pcode1 = int(input("Enter passcode: "))
            r_pcode2 = int(input("Confirm passcode: "))

            if r_pcode1 == r_pcode2:
                user_id = str(len(self.main_userInfo) + 1)
                self.main_userInfo[user_id] = {"r_uname": r_uname, "r_pcode": r_pcode2, "amount": r_amount}
                self.save_data()
                print("Registration successful!")
            else:
                print("Passcodes do not match!")
        except ValueError:
            print("Invalid input! Please enter numbers for amount and passcode.")

if __name__ == "__main__":
    miniBank = MiniBank()
    while True:
        miniBank.firstOpt()

