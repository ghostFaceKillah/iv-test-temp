import Accountant
import Strategy
import DataFeed
import matplotlib.pyplot as plt

def runTask():
    data = DataFeed.TextDataFeed('spx_prices.csv')
    params = {'signal_window' : 40, 'max_position' : 100, 
              'wait_period' : 100}
    trader = Strategy.SNPStrategy(params)
    booky = Accountant.Accountant(data, trader)
    booky.runBacktest()
    return booky

def showResults(resu):
    plt.plot(resu.cumPnl)
    plt.show()
