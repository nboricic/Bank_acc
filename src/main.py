import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainManu import Ui_MainWindow
from Delete_User import Ui_DeleteUser
from Calculate_Credit import Ui_MainWindow as Ui_CalculateCredit
from iow import Ui_MainWindow as Ui_iow
from Add_User import Ui_add_a_new_user
from add_new_bank_account import Ui_addNewBankAccount
from Edit_User import Ui_Edit_user
from Delete_Account import Ui_DeleteAccount
from Add_to_bank import Ui_MainWindow as Ui_AddToBank
from Bit_Coin import BitcoinPriceWindow
class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_manu = Ui_MainWindow()
        self.delete_user = Ui_DeleteUser()
        self.calculate_credit = Ui_CalculateCredit()
        self.add_user = Ui_add_a_new_user()
        self.iow = Ui_iow()
        self.add_a_new_bank_account = Ui_addNewBankAccount()
        self.edit_user = Ui_Edit_user()
        self.delete_account = Ui_DeleteAccount()
        self.add_to_bank = Ui_AddToBank()
        self.bit_coin = BitcoinPriceWindow()
        self.main_manu.set_window(self.add_user,self.iow,self.add_a_new_bank_account, self.delete_user,self.edit_user, self.calculate_credit,
                                   self.delete_account, self.add_to_bank, self.bit_coin)
        self.delete_user.back_to_main_manu(self.main_manu)
        self.add_user.back_to_main_manu(self.main_manu)
        self.iow.back_to_main_manu(self.main_manu)
        self.edit_user.back_to_main_manu(self.main_manu)
        self.add_a_new_bank_account.back_to_main_manu(self.main_manu)
        self.calculate_credit.back_to_main_manu(self.main_manu)
        self.delete_account.back_to_main_manu(self.main_manu)
        self.add_to_bank.back_to_main_manu(self.main_manu)
        self.bit_coin.back_to_main_manu(self.main_manu)
        self.main_manu.show()
        sys.exit(self.app.exec_())
        
if __name__ == "__main__":
    app = App()
    