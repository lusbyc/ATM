account_balance = 500
account_balance_formatted = "${:,.2f}".format(account_balance)

account_action = ""

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
