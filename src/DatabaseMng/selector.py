import sqlite3
#Select personal number (JMBG)

def JMBG_selector(value):
        conn = sqlite3.connect('bank.db')
        cur = conn.cursor()
        cur.execute('SELECT jmbg FROM bank_users WHERE (?)= jmbg', (value,))
        row = cur.fetchone()
        conn.commit()
        conn.close()
        return row
    
#Select all short bank_accID from bank

def select_all_short_bankID():
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute('SELECT short_num FROM bank_acc')
    row = cur.fetchall()
    print(row)
    conn.commit()
    conn.close()
    return row

#Select all data for bank user

def select_bank_user_data(value):
    try:
        conn = sqlite3.connect('bank.db')
        cur = conn.cursor()
        cur.execute('SELECT firstname, familyname,adreessofliving FROM bank_users WHERE  jmbg = ? ', (value,))
        row = cur.fetchone()
        print(row)
        conn.commit()
        conn.close()
        return row
    except:
        return "NotFound"
        
#Get All user data

def Get_All_User_Data(jmbg):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute("""SELECT firstname, middlename, familyname, dateofbirth, placebirth, statebirth, 
                    adreessofliving FROM bank_users WHERE  jmbg = ? """, (jmbg,))
    row = cur.fetchone()
    print(row)
    conn.commit()
    conn.close()
    return row
# Staro je get_acc_number

def get_all_user_bank_ID(JMBG):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT long_num FROM bank_acc WHERE jmbg = (?)', (JMBG,))
        row = cursor.fetchall()
        row = list(row)
        print(row)
        conn.commit()
        conn.close()
        return row 
    
#staro je   get_all_user_bank_acc  (koristi se u delete USer)

def get_all_user_bank_ID1( jmbg):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT long_num FROM bank_acc WHERE jmbg = (?)', jmbg)
    row = cursor.fetchall()   
    print(row)
    conn.commit()
    conn.close()
    return row



def total_cash_flaw(self):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT amount FROM bank_transaction')
    p = cursor.fetchall()
    total = 0.0
    for i in p:
        total +=i
    conn.commit()
    conn.close()
    return total
def getTransactions(pipi):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT long_num,amount,timestamp FROM bank_transactions WHERE long_num = (?)', (pipi,))
    p = cursor.fetchall()
    conn.commit()
    conn.close()
    return p
