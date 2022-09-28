from ast import Return
from turtle import pd
import yfinance as yf
import ta
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

class SMAcross(Strategy):
    n1 = 50 #50 day window
    n2 = 100 #100 day window

    def init(self):
        close = self.data.Close #close price
        self.sma1 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n1)
        self.sma2 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2): #sma Golden Cross
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

df = yf.download('ETH-USD', start='2020-01-01')
bt = Backtest(df, SMAcross, cash=10000, commission=0.002, exclusive_orders=True)

output = bt.run()
# print (df)
# print (output)
# bt.plot()

#finding optimization output
optim = bt.optimize(n1=range(50,160,10), n2=range(50,160,10), constraint=lambda x: x.n2-x.n1 >20, maximize= 'Return [%]')
bt.plot()
print (optim)
