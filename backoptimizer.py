import json

import backtrader as bt

from stocks import Stock
from loader import load_stock_data, date_ahead
from strategies.strategy2 import Strategy2
from strategies.strategy4 import Strategy4
from strategies.strategy5 import Strategy5
from strategies.strategySMA import StrategySMA
from strategies.strategynorth import StrategyNorth


# start, end = '2014-06-18', None       #从开始到现在
# start, end = '2015-05-01', None       #2015股灾到现在
# start, end = '2015-05-01', '2019-01-01'       #2015股灾到2019爆发前夕
# start, end = '2014-06-18', '2019-01-01'       #从开始到2019爆发前夕
# start, end = '2019-01-01', '2020-12-31'       #此轮牛市
# start, end = '2020-07-01', '2021-03-31'
# start, end = '2018-01-01', None
from strategies.strategynorth2 import StrategyNorth2
from strategies.strategynorth3 import StrategyNorth3
from strategies.strategynorth4 import StrategyNorth4
from strategies.strategynorthsma import StrategyNorthWithSMA

durations = [
    # ('2014-06-18', None),
    # ('2015-05-01', None),
    # ('2014-06-18', '2019-01-01'),
    # ('2014-06-18', '2019-01-01'),
    # ('2019-01-01', '2020-12-31'),
    ('2015-12-01', '2021-07-07'), #1
    # ('2018-01-22', '2020-06-30'),
    ('2016-07-22', '2020-07-07'), #2
    # ('2016-07-22', '2019-01-30'),
    # ('2015-05-01', '2019-01-01'),
    # ('2021-03-20', None), #3
    # (None, None)
    # ('2017-01-01', '2017-12-31'),
    # ('2017-01-01', '2018-12-31'),
    # ('2017-01-01', '2019-12-31'),
    # ('2017-01-01', '2020-12-31'),
]

for duration in durations:
    start, end = duration

    cerebro = bt.Cerebro()

    # cerebro.optstrategy(Strategy1, maperiod=[5, 10, 20, 60], minchgpct=range(0, 4, 1), printlog=False)
    # cerebro.optstrategy(Strategy2, buyperiod=[10, 20, 60], sellperiod=[5, 10, 20], minchgpct=range(0, 4, 1),
    #                     printlog=False)
    # cerebro.optstrategy(Strategy4, buyperiod=[10, 20, 60], sellperiod=[5, 10, 20], minchgpct=range(0, 4, 1),
    #                     printlog=False, starttradedt=start)
    # cerebro.optstrategy(Strategy5, buyperiod=[10, 20, 30, 60], sellperiod=[5, 10, 20, 60], minchgpct=range(0, 4, 1),
    #                     shouldbuypct=[0.2, 0.5, 0.7], printlog=False, starttradedt=start)
    # cerebro.optstrategy(StrategyNorth, period=[60, 120, 250, 500], highpercent=[0.6, 0.7, 0.8, 0.9],
    #                     lowpercent=[0.1, 0.2, 0.3, 0.4], maxdrawback=[0.02, 0.05, 0.1, 0.2],
    #                     printlog=False)
    # cerebro.optstrategy(StrategyNorthWithSMA, smaperiod=[5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 120],
    #                     printlog=False)
    # cerebro.optstrategy(StrategyNorth4, period=[60, 120, 250, 500], highpercent=[0.6, 0.7, 0.8, 0.9],
    #                     lowpercent=[0.1, 0.2, 0.3, 0.4], maxdrawback=[0.02, 0.05, 0.1, 0.2],
    #                     printlog=False)
    # cerebro.optstrategy(StrategyNorth2, period=[60, 120, 250, 500], highpercent=[0.6, 0.7, 0.8, 0.9],
    #                     lowpercent=[0.1, 0.2, 0.3, 0.4], maxdrawback=[0.02, 0.05, 0.1, 0.2],
    #                     printlog=False)
    # cerebro.optstrategy(StrategyNorth3, period=[60, 120, 250, 500], highpercent=[0.6, 0.7, 0.8, 0.9],
    #                     lowpercent=[0.1, 0.2, 0.3, 0.4], maxdrawback=[0.02, 0.05, 0.1, 0.2], phase=[1, 2, 3],
    #                     printlog=False)
    # cerebro.optstrategy(StrategyNorth2,
    #                     period=[250, 500], maxdrawback=[0.02, 0.05, 0.1],
    #                     highpercent1=[0.6, 0.7, 0.8, 0.9], lowpercent1=[0.1, 0.2, 0.3, 0.4],
    #                     highpercent2=[0.6, 0.7, 0.8, 0.9], lowpercent2=[0.1, 0.2, 0.3, 0.4],
    #                     printlog=False, starttradedt=start)
    # cerebro.optstrategy(StrategyNorth, period=[250, 500], highpercent=[0.8, 0.9],
    #                     lowpercent=[0.1, 0.2], maxdrawback=[0.02, 0.05, 0.1, 0.2],
    #                     offset=[0, 1, 5, 10, 20], printlog=False)
    cerebro.optstrategy(StrategySMA, smaperiod=[20, 30, 40, 60], daystobuy=[5, 6, 7, 8, 9, 10, 11, 12, 13],
                        daystosell=[2, 3, 4, 5, 6, 7], rsihigh=[74, 75, 76, 77, 78],
                        printlog=False)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe_ratio')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')

    # cerebro.addanalyzer(bt.analyzers.PyFolio, _name='PyFolio')

    load_stock_data(
        cerebro,
        # [Stock.HS300, Stock.CYB50, Stock.ZZ500],
        # [Stock.HS300ETF, Stock.CYB50ETF],
        # [Stock.CYB50ETF],
        # [Stock.CYB50],
        [Stock.HS300ETF],
        date_ahead(start, 365),
        end
    )

    print('Optimizing %s, %s' % duration)

    initial_cash = 1000000.0
    cerebro.broker.setcash(initial_cash)
    cerebro.addsizer(bt.sizers.PercentSizerInt, percents=95)
    cerebro.broker.setcommission(commission=0.00025)

    optimized_runs = cerebro.run(maxcpus=1)

    final_results_list = []
    for run in optimized_runs:
        for strategy in run:
            sharpe = strategy.analyzers.sharpe_ratio.get_analysis()
            trades = strategy.analyzers.trades.get_analysis()
            drawdown = strategy.analyzers.drawdown.get_analysis()
            try:
                net_total = trades['pnl']['net']['total']
                win_rate = trades['won']['total'] / (trades['won']['total'] + trades['lost']['total'])
                max_drawdown = drawdown['max']['drawdown']
                pd_rate = net_total / max_drawdown / initial_cash * 100
                sharpe_ratio = sharpe['sharperatio']
                final_results_list.append((json.dumps(strategy.params.__dict__),
                                           net_total,
                                           win_rate,
                                           max_drawdown,
                                           pd_rate,
                                           sharpe_ratio,
                                           ))
            except:
                pass

    sort_by_sharpe = sorted(final_results_list, key=lambda x: x[1],
                            reverse=True)
    for line in sort_by_sharpe[:10]:
        print('Param: %s, PNL Net %f, Win Rate %.2f, Max Drawdown %.2f, Profit Drawdown Rate %.2f, Sharp Ratio %f' % line)
