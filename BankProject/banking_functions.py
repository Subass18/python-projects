
from BankApp import *

def deposit(account_no,pin):
    print('welcome to the magadha bank deposit functions...')
    conn = connect_to_db()
    cursor = conn.cursor()
    dep_account_no = int(input('Enter Account Number: '))
    if dep_account_no == account_no:
        dep_pin = int(input('Enter your pin for deposit:'))
        if dep_pin == pin:
            amount = float(input('Enter your deposit amount: '))
            cursor.execute(
                "update users set balance = balance + %s where account_no = %s",
                (amount, account_no)
            )
            conn.commit()
            cursor.execute("SELECT balance FROM users WHERE account_no = %s", (account_no,))
            new_balance = cursor.fetchone()[0]
            print(f'your amount ₹{amount}Deposited successfully now your current balance')
            print(f"Your updated balance is ₹{new_balance}.")
        else:
            print('invalid pin entered')
    else:
        print('Invalid Account Number')

def withdraw(account_no,pin):
    print('welcome to the magadha bank withdraw functions...')
    conn = connect_to_db()
    cursor = conn.cursor()
    wd_account_no = int(input('Enter Account Number: '))
    if wd_account_no == account_no:
        wd_pin = int(input('enter your pin for withdraw:'))
        if wd_pin == pin:
            wd_amount = float(input('Enter your withdraw amount: '))
            cursor.execute("select balance from users where account_no = %s", (wd_account_no,))
            users= cursor.fetchone()[0]
            if wd_amount <= users:
                print(f'your entered amount ₹{wd_amount} was withdrawn successfully')
                cursor.execute("update users set balance = balance - %s where account_no = %s", (wd_amount,wd_account_no))
                conn.commit()
                cursor.execute("select balance from users where account_no = %s", (wd_account_no,))
                new_balance = cursor.fetchone()[0]
                print(f'your current balance was ₹{new_balance}')
            else:
                print('you dont have enough balance')
        else:
            print('invalid pin entered')
    else:
        print('invalid account_no is entered')

def balance_check(account_no,pin):
    print('welcome to the magadha balance checking functions...')
    conn = connect_to_db()
    cursor = conn.cursor()
    bc_account_no = int(input('Enter Account Number for Balance Check: '))
    if bc_account_no == account_no:
        bc_pin = int(input('Enter your pin for balance check:'))
        if bc_pin == pin:
            cursor.execute("select balance from users where account_no = %s", (bc_account_no,))
            balance = cursor.fetchone()[0]
            print(f'you have a balance amount of ₹{balance} ')

def banking_functions(account_no,pin):
    print('please select the option below for banking functions ')
    print('1.deposit')
    print('2.withdraw')
    print('3.balance check')
    option = int(input('please select your option: '))
    if option == 1:
        deposit(account_no,pin)
    elif option == 2:
        withdraw(account_no,pin)
    elif option == 3:
        balance_check(account_no,pin)