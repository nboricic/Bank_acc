
import sqlite3

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()
#Create a table where all loging accounts will be stored
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    datetime TEXT NOT NULL
    
)''')
#Create table where all bank_users will be sotred             
cursor.execute('''CREATE TABLE IF NOT EXISTS bank_users (
    id INTEGER PRIMARY KEY,
    firstname TEXT  NOT NULL,
    middlename TEXT NOT NULL,
    familyname TEXT NOT NULL,
    dateofbirth TEXT NOT NULL,
    placebirth TEXT NOT NULL,
    statebirth TEXT NOT NULL,
    jmbg TEXT NOT NULL,
    adreessofliving TEXT NOT NULL, 
    timestamp TEXT NOT NULL
)             
''')
#Create table where all bank_accounts will be sotred  
cursor.execute('''CREATE TABLE IF NOT EXISTS bank_acc (
    id INTEGER PRIMARY KEY,
    jmbg TEXT NOT NULL,
    valute TEXT NOT NULL,
    short_num INT NOT NULL,
    long_num INT NOT NULL,
    timestamp TEXT NOT NULL
    
)             
''')
#Create table where all transactions will be stored
cursor.execute('''CREATE TABLE IF NOT EXISTS bank_transactions (
    id INTEGER PRIMARY KEY,
    long_num INT NOT NULL,
    amount FLOAT,
    timestamp TEXT NOT NULL
    
)             
''')


conn.commit()
conn.close()
