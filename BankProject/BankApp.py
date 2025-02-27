from idlelib.run import exit_now

from connection_db import *
from edit_functions import *
from banking_functions import *


def signup():
    print('WELCOME TO THE SIGNUP OF MAGADHA BANK🙏🙏🙏..')
    account_no = int(input('Enter your account number from 4 to 5 digits: '))
    user_name = input('Enter your username: ').capitalize()
    password = input('Enter your password: ')
    pin = int(input('Enter your pin: '))
    amount = float(input('Enter initial deposit amount: '))

    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (account_no,username, password, pin, balance) VALUES (%s, %s, %s, %s,%s)",
            (account_no, user_name, password, pin, amount)
        )
        conn.commit()
        print(f'{user_name} you are Signed In Successfully!')
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    cursor.close()
    conn.close()

def login():
    print('WELCOME TO THE MAGADHABANK LOGIN................=')
    account_no = int(input('Enter your account number from 4 to 5 digits: '))
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute(
    "select pin from users where account_no = %s",
    (account_no,))
    users = cursor.fetchone()
    # print(users)
    if users:
         pin = (users[0])
         entered_pin = int(input('Enter your pin number: '))
         # print(pin)
         if entered_pin == pin:
             print('welcome to the magadhabank functions...')
             print('1.Banking Functions')
             print('2.Edit Functions')
             option = int(input('Enter your option: '))
             if option == 1:
                 banking_functions(account_no,pin)
             elif option == 2:
                 edit_functions(account_no,pin)
             else:
                 exit()

         else:
             print('you are pin was not correct !')
    else:
         print('you are not signned in please signup before the login!')
def exit_now():
    print('Thank you for visiting the Magadhabank functions 🙏🙏🙏!')
    exit()

while True:
        print("\nWELCOME TO THE MAGADHA BANK APP")
        print("1. LOGIN😁")
        print("2. SIGN UP🐾")
        print("3. EXIT🙏")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            login()
        elif choice == 2:
            signup()
        elif choice == 3:
            exit_now()

        else:
            print("Invalid Choice")


