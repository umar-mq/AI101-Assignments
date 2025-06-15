from utils import *

db = {0: {'name': 'Umar Qureshi', 'pin': 2010, 'balance': 52000}}

def get_balance(id_):
    print('Your balance is', db[id_]['balance'])

def deposit_money(id_, amount):
    db[id_]['balance'] += amount
    print('Money depositted successfully.')
    get_balance(id_)

def withdraw_money(id_, amount):
    balance = db[id_]['balance']
    if amount > balance:
        print("Withdrawal unseccessful. Not enough balance.")
        return
    
    db[id_]['balance'] -= amount
    print("Withdrawal successful!")
    get_balance(id_)

cls()
while True:
    cls()
    option = choice('Select option', ['Create Account', 'Login', 'Exit'])

    if option == 'Create Account':
        _id = max(list(db.keys())) + 1
        db[_id] = {'name': input('Enter full name: '), 'pin': int(input('Enter 4 digit pin: ')), 'balance': 0}
        cls()
        print('Account created successfully! Your account id is', _id)
    elif option == 'Login':
        account_id = int(input('Enter account id: '))
        if account_id in db:
            pin = int(input('Enter account pin: '))
            if pin == db[account_id]['pin']:
                cls()
                print('Logged in successfully!')

                while True:
                    sub_option = choice('Choose action', ['Get Balance', 'Deposit Money', 'Withdraw Money', 'Log out'])

                    if sub_option == 'Get Balance':
                        cls()
                        get_balance(account_id)
                    
                    if sub_option == 'Deposit Money':
                        cls()
                        amount = int(input('Enter amount: '))
                        deposit_money(account_id, amount)

                    if sub_option == 'Withdraw Money':
                        cls()
                        amount = int(input('Enter amount: '))
                        withdraw_money(account_id, amount)

                    if sub_option == 'Log out':
                        break
            
            else:
                print('Invalid pin!')
        else:
            print('Invalid ID!')
    else:
        print('Exiting!')
        break