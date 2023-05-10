#!/usr/bin/python3

#common_def 定义了所有全局变量, 为了区分A股，和创业板

creerFlag = 0   #是否是创业板, 1： 创业板， 0： A股主板

codeDate = ''   #获取某天的所有A股和创业板股票
startDate = ''  #获取股票的K线的开始日期
endDate = ''    #获取股票的K线的结束日期

zTing = 10.0    #涨停幅度
zMiddle = 18.0  #上涨用于判断是否涨停
dTing = 10.0    #跌停幅度
dMiddle = 8.0   #下跌中间值


pctChg = 20.0   #当前涨幅

