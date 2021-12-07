"""
Enhancements to work on during break between first and second Python class:
- Prompt user for 4 digit passcode
    - Only allow 3 attempts 
    - Lock out user if they enter an incorrect passcode 3 times
    - Do not loop if the wrong passcode is entered 3 times

- For withdrawals 
    - Do not allow the user to take out an amount larger than the current balance
    - Check that user is requesting an amount in increments of $20 as ATMs do not allow you to withdraw $5, $1, or $11 etc

"""


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
        while withdrawal_amount > account_balance:
            withdrawal_amount = int(input(f"""
    Insufficient Funds.
    Account Balance: {account_balance_formatted}
    Please enter an amount that does not exceed your balance:
    
    """))

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
