class Schedule:

    def __init__(self, symbol, function, interval, from_currency, to_currency, market):
        self.symbol = symbol
        self.function = function
        self.interval = interval
        self.fromCurrency = from_currency
        self.toCurrency = to_currency
        self.market = market
