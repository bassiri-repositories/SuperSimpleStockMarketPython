import time
from datetime import datetime, date, time, timedelta

class SuperSimpleStockMarket:
    def __init__(self, lookbackTime):
        self.lookbackTime = lookbackTime
        self.processedTrades = []
        self.unprocessedTrades = []
        self.FLOAT_PRECISION = 10

    def processTrade(self, trade):
        if trade.processTrade():
            self.processedTrades.append(trade)
            print("trade was successfully processed")
        else:
            self.unprocessedTrades.append(trade)
            print("trade was not processed")

    def calculateVolumeWeightedStockPrice(self):
        currentInstant = datetime.now()
        sigmaTradeTimesQuantity = 0
        sigmaQuantity = 0
        for trade in self.processedTrades:
            if trade.tradeTimestamp > currentInstant - timedelta(seconds=self.lookbackTime):
                sigmaTradeTimesQuantity = sigmaTradeTimesQuantity + trade.price * trade.quantity
                sigmaQuantity = sigmaQuantity + trade.quantity
        volumeWeightedStockPrice = 0
        if sigmaQuantity > 0:
            volumeWeightedStockPrice = round(sigmaTradeTimesQuantity / sigmaQuantity, self.FLOAT_PRECISION)
        return volumeWeightedStockPrice

    def calculateGeometricMean(self):
        if not self.processedTrades:
            return 0
        productOfPrices = 1
        for trade in self.processedTrades:
            productOfPrices = productOfPrices * trade.price
        geometricMean = productOfPrices ** (1/len(self.processedTrades))
        return geometricMean



    def printTrades(self):
        print("Processed trades:")
        for trade in self.processedTrades:
            print(trade.reportTrade())

        print("Unprocessed trades:")
        for trade in self.unprocessedTrades:
            print(trade.reportTrade())


