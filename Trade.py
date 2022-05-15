import StockMap
import StockType
from datetime import datetime

class Trade:
    def __init__(self, stockSymbol, price, quantity, buySell):
        self.stockSymbol = stockSymbol
        self.price = price
        self.quantity = quantity
        self.buySell = buySell
        self.tradeProcessed = False
        self.dividendYield = 0
        self.peratio = 0
        self.stock = None
        self.tradeTimestamp = None

    def processTrade(self):
        if self.stockSymbol in StockMap.stockDict.keys():
            self.stock = StockMap.stockDict[self.stockSymbol];
            self.dividendYield = self.calculateDividendYield()
            self.peratio = self.calculatePeRatio()
            print(self.stockSymbol + " is in stockMap")
            print("Stock type: " + self.stock.stockType.name + " dividend yield: " + str(self.dividendYield) + " pe ratio: " + str(self.peratio))
            self.tradeTimestamp = datetime.now()
            self.tradeProcessed = True

        else:
            print("Stock Symbol " + self.stockSymbol + " is not in the reference data. Ignoring this trade.")
        return self.tradeProcessed

    def reportTrade(self):
        if self.tradeProcessed:
            return "Stock Symbol: {stockSymbol}, Quantity: {quantity}, Buy/Sell: {buysell}, Price: {price}, Dividend Yield: {divyield}, P/E ratio: {peratio}, Trade timestamp {tradeTimestamp}"\
                .format(stockSymbol = self.stockSymbol, quantity = self.quantity, buysell = self.buySell.name, price = self.price, divyield = self.dividendYield, peratio = self.peratio, tradeTimestamp = self.tradeTimestamp)
        else:
            return "Stock Symbol: {stockSymbol}, Quantity: {quantity}, Buy/Sell: {buysell}, Price: {price}" \
                .format(stockSymbol = self.stockSymbol, quantity = self.quantity, buysell = self.buySell.name, price = self.price)


    def calculateDividendYield(self):
        if self.stock.stockType == StockType.StockType.COMMON:
            return 0 if self.price == 0 else self.stock.lastDividend / self.price
        else:
            return 0 if self.price == 0 else self.stock.fixedDividend * self.stock.parValue / self.price

    def calculatePeRatio(self):
        return 0 if self.stock.lastDividend == 0 else self.price / self.stock.lastDividend