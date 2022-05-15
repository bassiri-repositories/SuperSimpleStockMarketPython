import SuperSimpleStockMarket
import Trade
import BuySell

sssm = SuperSimpleStockMarket.SuperSimpleStockMarket()
trade = Trade.Trade("GIN", 25, 1, BuySell.BuySell.SELL)
trade2 = Trade.Trade("TEA", 43, 6, BuySell.BuySell.BUY)
trade3 = Trade.Trade("COF", 43, 6, BuySell.BuySell.BUY)


print ("processing trade")
sssm.processTrade(trade)
print ("processing trade2")
sssm.processTrade(trade2)
print ("processing trade3")
sssm.processTrade(trade3)

sssm.printTrades()