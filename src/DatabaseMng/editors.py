import sqlite3
from .timestamp import Timestamp

def Edit_User_Data(self, firstName,middleName,familyName,dateofBirth,placeofBirth,stateofBirth,jmbg,addressofLiving):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    cursor.execute("""UPDATE  bank_users SET firstname = ?, middlename = ?, familyname = ?, dateofbirth = ?, placebirth = ?, statebirth = ?, 
                    adreessofliving = ?, timestamp = ?
                    WHERE jmbg   = ? """, (firstName,middleName,familyName,dateofBirth,placeofBirth,stateofBirth,addressofLiving,Timestamp(),jmbg))
    conn.commit()
    conn.close()
