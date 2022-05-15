import Trade
import BuySell
import StockType

def processTradeStockNotInReferenceData():
    trade = Trade.Trade("COF", 25, 1, BuySell.BuySell.SELL)
    processed = Trade.Trade.processTrade(trade)
    assert processed == False
    print (Trade.Trade.reportTrade(trade))

def processTradePreferredStock():
    trade = Trade.Trade("GIN", 25, 1, BuySell.BuySell.SELL)
    processed = Trade.Trade.processTrade(trade)
    assert processed == True
    assert trade.stock.stockType == StockType.StockType.PREFERRED
    assert trade.stock.fixedDividend == 0.02
    assert trade.stock.parValue == 100
    assert trade.price == 25
    assert trade.dividendYield == 0.08
    assert trade.peratio == 3.125

def processTradeCommonStock():
    trade = Trade.Trade("POP", 250, 15, BuySell.BuySell.BUY)
    processed = Trade.Trade.processTrade(trade)
    assert processed == True
    assert trade.stock.stockType == StockType.StockType.COMMON
    assert trade.stock.lastDividend == 8
    assert trade.stock.parValue == 100
    assert trade.price == 250
    assert trade.dividendYield == 0.032
    assert trade.peratio == 31.25

def processZeroDividend():
    trade = Trade.Trade("TEA", 25, 1, BuySell.BuySell.SELL)
    processed = Trade.Trade.processTrade(trade)
    assert processed == True
    assert trade.stock.stockType == StockType.StockType.COMMON
    assert trade.stock.lastDividend == 0
    assert trade.stock.parValue == 100
    assert trade.price == 25
    assert trade.dividendYield == 0
    assert trade.peratio == 0


processTradeStockNotInReferenceData()
processTradePreferredStock()
processTradeCommonStock()
processZeroDividend()