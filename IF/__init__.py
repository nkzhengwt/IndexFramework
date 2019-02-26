# -*- coding: utf-8 -*-
"""
Created on Fri Jan  30 11:54:11 2019

@author: Wentao
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from core import *
from algos import *
from backtest import *
import ffn
ffn.extend_pandas()

#generate fake data
data = pd.DataFrame(np.random.uniform(0,900,size=(900, 4)), columns=list('ABCD'), \
                    index=[pd.Timestamp(datetime.utcnow().date() + timedelta(days=-i)) \
                           for i in range(900,0,-1)])

#s = Strategy('s1', [RunAfterDays(20),RunMonthly(),SelectAll(),WeighERC(),Rebalance()])
#s = Strategy('s1', [RunAfterDays(20),RunQuarterly(),SelectAll(),WeighInvVol(),Rebalance()])
#s = Strategy('s1', [RunAfterDays(20),RunQuarterly(),SelectRandomly(),WeighMeanVar(),Rebalance()],['A','B'])


mom_s = Strategy('mom_s', [RunMonthly(),SelectAll(),SelectMomentum(1),WeighEqually(), \
                              Rebalance()],
                    ['A', 'B','C','D'])


s = Strategy('master', [RunMonthly(),SelectAll(),WeighEqually(),Rebalance()], \
                    [mom_s, 'A','C'])
test = Backtest(s, data)
res = run(test)
res.plot()
res.display()
res.plot_histogram()
res.plot_security_weights()