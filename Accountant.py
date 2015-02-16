class Accountant(object):
    def __init__(self, dataFeed, strategy):
        self.dataFeed = dataFeed
        self.strategy = strategy
        # these will probably later become numpy arrays
        self.date = []
        self.price = []
        self.contract_value = []
        self.position = []
        self.cumPnl = []
        self.todayPnl = []

    def runBacktest(self):
        for day in self.dataFeed.getDataStream():
            # store needed data
            self.date.append(day['date'])
            self.price.append(day['price'])
            self.contract_value.append(day['value'])
            # account pnl
            if len(self.date) < 2:
                self.cumPnl.append(0)
                self.todayPnl.append(0)
            else:
                p_diff = self.price[-1] - self.price[-2]
                pnl = p_diff * self.position[-1] * self.contract_value[-1]
                self.todayPnl.append(pnl)
                self.cumPnl.append(self.cumPnl[-1] + pnl)
            # pass data to strategy and compute todays
            signal = self.strategy.computeSignal(day)
            self.position.append(signal)
