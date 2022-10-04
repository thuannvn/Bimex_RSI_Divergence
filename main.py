# -*- coding: utf-8 -*-
import arch as trading

### Edit here
trading_pair = "XBTUSD"
timeframe = "5m"
trace_back_days = 7
###

MonitorBot= trading.OnTick(trading_pair,timeframe,trace_back_days)
MonitorBot.main_job()
