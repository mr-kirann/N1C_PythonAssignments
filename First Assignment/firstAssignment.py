#firstAssignment
class MiniBank:

    main_userInfo:dict = {}

    def firstOpt(self):
        option:int = int(input("Press 1 to Login:\nPress 2 to Register:"))
        if (option==1):
            self.login()
        else:
            self.register()

    def returnId(self, transfer_uname):
        userInfo_len:int=len(self.main_userInfo)
        for i in range(1,userInfo_len+1):
            if self.main_userInfo[i]["r_uname"]==transfer_uname:
                return i
        return None

    def menu(self, loginID):
        menu_input:int=int(input("Press 1 to Transfer:\nPress 2 to Withdraw:\nPress 3 to Update:"))
        if menu_input==1:
            transfer_uname=input("Please enter username to transfer:")
            transfer_id:int=self.returnId(transfer_uname)
            if transfer_id is None:
                print("User not found!")
                return
            
            amount:int = int(input("Enter amount to transfer to {0}: ".format(self.main_userInfo[transfer_id]["r_uname"])))
            if self.main_userInfo[loginID]["amount"] >= amount:
                self.main_userInfo[loginID]["amount"] -= amount
                self.main_userInfo[transfer_id]["amount"] += amount
                print(f"Transfer successful!\nYou're current amount is {self.main_userInfo[loginID]['amount']}")
            else:
                print("Insufficient balance!")

        elif menu_input==2:
            self.withdraw(loginID)

        elif menu_input==3:
            self.update(loginID)

    def withdraw(self, loginID):
        print("Your current balance is:", self.main_userInfo[loginID]["amount"])
        withdraw_amount:int=int(input("Enter amount to withdraw: "))
        if self.main_userInfo[loginID]["amount"] >= withdraw_amount:
            self.main_userInfo[loginID]["amount"] -= withdraw_amount
            print(f"Withdrawal successful!\nYou're amount is now {self.main_userInfo[loginID]['amount']}")
        else:
            print("Insufficient balance!")

    def update(self, loginID):
        update_option:int = int(input("Press 1 to change username:\nPress 2 to change password:\nPress 3 to update amount:"))
        if update_option == 1:
            new_username = input("Please enter the new username: ")
            self.main_userInfo[loginID]["r_uname"] = new_username
            print(f"Username updated successfully!\nYou're current username is {new_username}")
        elif update_option == 2:
            current_passcode = int(input("Please enter the current passcode: "))
            if self.main_userInfo[loginID]["r_pcode"] == current_passcode:
                new_passcode = int(input("Please enter the new passcode: "))
                confirm_passcode = int(input("Please confirm the new passcode: "))
                if new_passcode == confirm_passcode:
                    self.main_userInfo[loginID]["r_pcode"] = new_passcode
                    print("Passcode updated successfully!")
                else:
                    print("Passcodes do not match!")
            else:
                print("Incorrect current passcode!")
        elif update_option == 3:
            additional_amount = int(input("Please enter the amount to add: "))
            self.main_userInfo[loginID]["amount"] += additional_amount
            print(f"Amount updated successfully!\nYou're amount is now {self.main_userInfo[loginID]['amount']}")

    def login(self):
        print("\n__________This is from Login__________\n")
        l_uname:str = input("Plese enter username to login:")
        l_pcode:int = int(input("Please enter passcode to login:"))
        exitUser = self.exitUser(l_uname, l_pcode)
        if(exitUser):
            print("\n\n\n_____Login successful!_____\n\n\n")
            loginID:int = self.returnId(l_uname)
            self.menu(loginID)
        else:
            print("You can't login!")

    def exitUser(self, l_uname, l_pcode):
        u_count = len(self.main_userInfo)
        for i in range(1,u_count+1):
            if self.main_userInfo[i]["r_uname"]==l_uname and self.main_userInfo[i]["r_pcode"]==l_pcode:
                return True
        return False

    def register(self):
        print("\n__________This is from Register__________\n")
        r_uname:str = input("Please enter username to register:")
        r_amount:int = int(input("Enter amount:"))
        r_pcode1:int = int(input("Please enter passcode to register:"))

        r_pcode2:int = int(input("Please enter again passcode to com:"))

        if (r_pcode1 == r_pcode2):
            id:int=self.checkUserNum()
            userInfoForm:dict={id:{"r_uname":r_uname,"r_pcode":r_pcode2,"amount":r_amount}}
            self.main_userInfo.update(userInfoForm)
            print("#### Success Registered! ####\n\n")

    def checkUserNum(self):
           count = len(self.main_userInfo)
           return count+1
    
if __name__=="__main__":
    miniBank:MiniBank=MiniBank()
    while True:
        miniBank.firstOpt()

