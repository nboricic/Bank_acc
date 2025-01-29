import requests
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def fetch_bitcoin_data():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30'
    response = requests.get(url)
    data = response.json()
    dates = [datetime.datetime.fromtimestamp(item[0] // 1000).date() for item in data['prices']]
    prices = [item[1] for item in data['prices']]
    return dates, prices
class BitcoinPriceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UiBitcoin()
    def back_to_main(self):
        self.hide()
        self.window1.show()
    def back_to_main_manu(self, window1):
        self.window1 = window1
    def UiBitcoin(self):
        dates, prices = fetch_bitcoin_data()
        self.setWindowTitle("Bitcoin price over last 30 Days")
        self.setGeometry(100, 100, 800, 800)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.plot(dates, prices)
        self.pushButtonClose = QtWidgets.QPushButton("Close", central_widget)
        self.pushButtonClose.clicked.connect(self.back_to_main)
        layout.addWidget(self.pushButtonClose)
    def plot(self, dates, prices):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(dates, prices)
        ax.set_title("Bitcoin Price Over Last 30 Days")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        ax.grid(True)
        self.canvas.draw()

