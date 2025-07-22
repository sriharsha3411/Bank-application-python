import random
class Bank:
    holders_details=[]
    def create_account(self):
        new_holder={}
        new_holder["Holder_Name"]=input("enter holder name:")
        new_holder["Age"]=int(input("enter holder age:"))
        new_holder["Account_Number"]=random.randint(100000000,999999999)
        new_holder["mobile_Number"]=int(input("enter mobile number:"))
        new_holder["aadhar_no"]=int(input("enter aadhar number:"))
        new_holder["IFSCCODE"]="IFSC57845"
        new_holder["account_balance"]=0
        new_holder["account_type"]=input("enter account type zero or saving:".lower())

        if new_holder["account_type"]=="saving":
            while True:
                n1=int(input("you choosen savings account, so deposit minimum 500 rupees:"))
                if n1>=500:
                    new_holder["account_balance"]=n1
                    break
                else:
                    print("deposit minimum 500 rupees to open savings account")
        else:
            while True:
                n1=int(input("you choosen zero account, so deposit minimum 100 rupees:"))
                if n1>=100:
                    new_holder["account_balance"]=n1
                    break
                else:
                    print("deposit minimum 100 rupees to open zero account")
        
        Bank.holders_details.append(new_holder)
        print(f"Account created successfully, your details: {new_holder}")
        
  
    def deposit(self):
        print("========welcome to deposit section========")
        name=input("Enter your name to verify:")
        acc_no=int(input("Enter account number to verify:"))
        amount=int(input("Enter amount to deposit:"))
        for holder in Bank.holders_details:
            if holder["Holder_Name"]==name and holder["Account_Number"]==acc_no:
                holder["account_balance"]+=amount
                print(f"{amount} has deposited to your account.")
                print(holder)
                break
        else:
            print("Account Not Found")
        
    
    def withdraw(self):
        print("========welcome to withdraw section========")
        name=input("Enter your name to verify:")
        acc_no=int(input("Enter account number to verify:"))
        amount=int(input("Enter amount to withdraw:"))
        for holder in Bank.holders_details:
            if holder["Holder_Name"]==name and holder["Account_Number"]==acc_no:
                holder["account_balance"]-=amount
                print(f"{amount} has withdrawn from your account.")
                print(holder)
                break
        else:
            print("Account Not Found")


    def check_balance(self):
        print("========welcome to Check Balance section========")
        name=input("Enter your name to verify:")
        acc_no=int(input("Enter account number to verify:"))
        for holder in Bank.holders_details:
            if holder["Holder_Name"]==name and holder["Account_Number"]==acc_no:
                print(f"Your Account Balance is: {holder["account_balance"]}")
                break
        else:
            print("Invalid Credentials")


    def details(self):
        print("========welcome to details section========")
        print("To view your Accoount Details")
        name=input("Enter your name:")
        acc_no=int(input("Enter account number:"))
        for holder in Bank.holders_details:
            if holder["Holder_Name"]==name and holder["Account_Number"]==acc_no:
                print(f"Your Details: {holder}")
                break
        else:
            print("Account Not Found")
       
    
obj=Bank()
while True:
    print('''1. create account 
          2. deposit
          3. withdraw 
          4. Check Balance
          5. details   
          6. break''')
    
    n=input("enter your choice:")
    if n=="1":
        obj.create_account()
    elif n == "2":
        obj.deposit()
    elif n=="3":
        obj.withdraw()
    elif n=="4":
        obj.check_balance()
    elif n=="5":
        obj.details()
    elif n=="6":
        break
    else:
        print("enter valid number")