import Stock
import StockType

stockDict = {
            "TEA": Stock.Stock("TEA", StockType.StockType.COMMON, 0, 0, 100),
            "POP": Stock.Stock("POP", StockType.StockType.COMMON, 8, 0, 100),
            "ALE": Stock.Stock("ALE", StockType.StockType.COMMON, 23, 0, 60),
            "GIN": Stock.Stock("GIN", StockType.StockType.PREFERRED, 8, 0.02, 100),
            "JOE": Stock.Stock("JOE", StockType.StockType.COMMON, 13, 0, 250)
}
