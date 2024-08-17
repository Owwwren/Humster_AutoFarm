from db.db_window import SQLighter
from pars.config import starter


db = SQLighter('db/db.db')

def account_key(account_number):
    if db.get_account(value=account_number, method='number') == True:
        print('True')
    else:
        print('False')
        starter()
    