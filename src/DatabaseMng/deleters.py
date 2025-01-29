import sqlite3

#delete bank ACC
class Delete_Bank_ACC:
    def __init__(accID):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM bank_acc  WHERE long_num = (?)', (accID,))
        conn.commit()
        conn.close()
    
#delete bank user
class Delete_Bank_user:
    def __init__(self, accID, jmbg):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        for i in accID:
            cursor.execute('DELETE FROM bank_acc  WHERE long_num = (?)', (i,))
        cursor.execute('DELETE FROM bank_users  WHERE jmbg = (?)', jmbg)
        conn.commit()
        conn.close()
