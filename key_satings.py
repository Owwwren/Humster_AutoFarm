from db.db_window import SQLighter
from pars.setingsPars import get_data


db = SQLighter('db/db.db')

def account_key(account_number):
    if db.get_account(value=account_number, method='number') == True:
        print('True')
    else:
        print('False')
        get_data()
    