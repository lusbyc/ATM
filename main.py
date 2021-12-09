account_balance = 500
account_balance_formatted = "${:,.2f}".format(account_balance)

account_action = ""

attempts = 0
passcode = "1619"

while attempts < 3:
    attempts += 1
    passcode_entry = input("Please enter your passcode: ")
    
    if passcode_entry == passcode:
        
        keep_going = "y"

        while keep_going.lower() == "y":

            while account_action != "4":
                account_action = input (f"""
                ***********************
                Welcome to DevYou Bank!
                ***********************

                [1] Check Balance
                [2] Deposit
                [3] Withdraw
                [4] Exit

                """)

                if account_action == "1":
                    print(f"""
                Your current balance is {account_balance_formatted}""")
                elif account_action == "2":
                    deposit_amount = int(input("""
                Enter amount to deposit: """))
                    account_balance = account_balance + deposit_amount
                    account_balance_formatted = "${:,.2f}".format(account_balance)
                    print(f"""
                Your new balance is {account_balance_formatted}""")
                elif account_action == "3":
                    withdrawal_amount = int(input("""
                Enter amount to withdraw: """))
                    while withdrawal_amount > account_balance:
                        withdrawal_amount = int(input(f"""
                Insufficient Funds.
                Account Balance: {account_balance_formatted}
                Please enter an amount that does not exceed your balance:
                
                """))

                    else:
                        while withdrawal_amount % 20 != 0:
                            withdrawal_amount = int(input("""
                Please enter an amount in increments of $20: """))
                        else:
                            account_balance = account_balance - withdrawal_amount
                            account_balance_formatted = "${:,.2f}".format(account_balance)
                            print(f"""
                Your new balance is {account_balance_formatted}""")     
            else: 
                account_action == "4"
                print("""
                ******************************************************
                Thank You for Banking with DevYou and Have a Nice Day!
                ******************************************************
                """)
                break
print(f"""
    ************************************************************************************
        You have entered an invalid passcode multiple times. Your card is now locked.       
    Please contact DevYou Customer Service during business hours to access your account.
    ************************************************************************************
    """)
