import sqlite3
import bcrypt
from .timestamp import Timestamp
#This module is for inserting in table
#method creating bank manager user
                  
def create_user(username, password):  
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO accounts (username, password, datetime) VALUES (?, ?, ?)', (username, hashed_password,Timestamp() ))
    conn.commit()
    conn.close()
#method for creating Bank Account

def add_bank_account(jmbg,valute,short_num,long_num):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    cursor.execute("""INSERT INTO bank_acc (jmbg, valute, short_num, long_num, timestamp) VALUES 
                (?, ?, ?, ?, ?)""", (jmbg,valute,short_num,long_num,Timestamp()))
    conn.commit()
    conn.close()
#method for creating Bank User

def create_bank_user(firstName, middleName, familyName, dateofBirth, placeofBirth, stateofBirth,jmbg, addressofLiving):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO bank_users (firstname, middlename, familyname, dateofbirth, placebirth, statebirth, 
                jmbg, adreessofliving, timestamp) VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (firstName,middleName,familyName,dateofBirth,placeofBirth,stateofBirth,jmbg,addressofLiving,Timestamp()))
    conn.commit()
    conn.close()
#add or withdraw money from cashflaw

def add_money(long_num, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO bank_transactions (long_num, amount, timestamp) VALUES 
                (?, ?, ? )""", (long_num, amount, Timestamp()))
    conn.commit()
    conn.close()


