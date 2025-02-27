from _pyrepl.commands import delete

from connection_db import *
from BankApp import *
def update(account_no):
    print('Welcome To Magadha Bank Update Function')
    conn = connect_to_db()
    cursor = conn.cursor()
    up_accountno = int(input('Enter Your Account Number: '))
    if up_accountno == account_no:
        print('Provide Details for Updating Account')
        user_name = input('Enter your username: ').capitalize()
        password = input('Enter your password: ')
        pin = int(input('Enter your pin: '))

        cursor.execute(
            "update users set username = %s,password = %s,pin = %s where account_no = %s",
            (user_name, password, pin,up_accountno)
            )
        conn.commit()
        print('Account Updated Successfully')

    else:
         print('invalid account_no')
def view(account_no,pin):
    print('Welcome To Magadha Bank View Function')
    v_account_no = int(input('Enter Your Account Number For Viewing: '))
    if v_account_no == account_no:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("select * from users where account_no = %s",(v_account_no,))
        all = cursor.fetchall()
        for i in all:
            print(f'Account Number:{i[1]}')
            print(f'Account Holder name:{i[2]}')
            print(f'Password of Account Holder {i[3]}')
            print(f'Pin of Account Holder {i[4]}')
            print(f'Balance of Account Holder {i[5]}')
def delete(account_no,pin):
    print('Welcome To Magadha Bank Delete Function')
    dl_account_no = int(input('Enter Your Account Number For Deleting: '))
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("delete from users where account_no = %s",(dl_account_no,))
    conn.commit()
    print('Account Deleted Successfully')
def edit_functions(account_no,pin):
    print('Welcome To Magadha_Bank Edit Functions')
    print('1.Update Details')
    print('2.view Details')
    print('3.Delete details')
    ef_option = int(input('Enter your option: '))
    if ef_option == 1:
        update(account_no)
    elif ef_option == 2:
        view(account_no,pin)
    elif ef_option == 3:
        delete(account_no,pin)
    else:
        print('Invalid option')
