import SuperSimpleStockMarket
import Trade
import BuySell
import time


def giveMeListOfTrades():
    return [
        Trade.Trade("POP", 1, 15, BuySell.BuySell.BUY),
        Trade.Trade("ALE", 5, 7, BuySell.BuySell.BUY),
        Trade.Trade("GIN", 25, 1, BuySell.BuySell.SELL),
        Trade.Trade("COF", 25, 1, BuySell.BuySell.SELL)
    ]

def giveMeListOfTradesWithZeroPrice():
    return [
        Trade.Trade("POP", 1, 15, BuySell.BuySell.BUY),
        Trade.Trade("ALE", 0, 7, BuySell.BuySell.BUY),
        Trade.Trade("GIN", 25, 1, BuySell.BuySell.SELL),
        Trade.Trade("COF", 25, 1, BuySell.BuySell.SELL)
    ]

def processTrades(sssm, trades, sleepTime):
    for trade in trades:
        sssm.processTrade(trade)
        time.sleep(sleepTime)

def runTheTest(lookbackTime, sleepTime, expectedWeightedStockPrice, expectedGeometricMean, trades):
    sssm = SuperSimpleStockMarket.SuperSimpleStockMarket(lookbackTime)
    processTrades(sssm, trades, sleepTime)
    volumeWeightedStockPrice = sssm.calculateVolumeWeightedStockPrice()
    sssm.printTrades()
    assert volumeWeightedStockPrice == expectedWeightedStockPrice
    geometricMean = sssm.calculateGeometricMean()
    assert geometricMean == expectedGeometricMean

def testAllWithinLookbackTime():
    runTheTest(900, 0, 3.2608695652, 5.0000000000, giveMeListOfTrades()) #Lookback of 900 seconds is 15 mins, no delay between trades

def testNoneWithinLookbackTime():
    runTheTest(15, 10, 0, 5.0000000000, giveMeListOfTrades()) #lookback of 15 seconds, 10 sec delay between trades

def testSomeWithinLookbackTime():
    runTheTest(35, 10, 7.5000000000, 5.0000000000, giveMeListOfTrades()) #lookback of 35 seconds, 10 sec delay between trades

def testWithZeroPrice():
    runTheTest(900, 0, 1.7391304348, 0, giveMeListOfTradesWithZeroPrice()) #Lookback of 900 seconds is 15 mins, no delay between trades

def testWithNoTrades():
    runTheTest(900, 0, 0, 0, []) #Lookback of 900 seconds is 15 mins, no trades to process

testAllWithinLookbackTime()
testNoneWithinLookbackTime()
testSomeWithinLookbackTime()
testWithZeroPrice()
testWithNoTrades()