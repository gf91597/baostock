#!/usr/bin/python3
import baostock as bs
import pandas as pd


# BaoStock login

def baoStockLogin():
    lg = bs.login()
    # show login return infomation
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

def baoStockClose():
    bs.logout()

# get stock Code
#
def getStockCode(date, creerFlag):
    #### login baostock ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    #### 获取证券信息 ####
    rs = bs.query_all_stock(day=date)
    print('query_all_stock respond error_code:' + rs.error_code)
    print('query_all_stock respond  error_msg:' + rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())

#    print("data list is ")
#    print(data_list)
    fcode = open("stockCode", "w+")

    listLen = len(data_list)
    #print(data_list)


    code = []
    for data in data_list:

        if (creerFlag == 0):
            if (data[0][3:6] == '600' or data[0][3:6] == '000' or data[0][3:6] == '002'):
                fcode.write(data[0] + '\n')
                code.append(data[0])
        elif (creerFlag == 1):
            if (data[0][3:6] == '300' or data[0][3:6] == '301'):
                fcode.write(data[0] + '\n')
                code.append(data[0])
        #elif (creerFlag == 2):
            #if (data[0][3:6] == '600' or data[0][3:6] == '000' or data[0][3:6] == '002' or data[0][3:6] == '300'):
                #fcode.write(data[0] + '\n')
               #code.append(data[0])
        else:
            print("set creerFlag as 0, 1, 2")
    fcode.close()
    print(len(code))
    #print(code)

    #### 登出系统 ####
    bs.logout()
    return code


# get stock K line data
def get_K_Line(code, start, end):
    #### login baostock ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
    for cd in code:
        rs = bs.query_history_k_data_plus(cd,
            "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
            start_date=start, end_date=end,
            frequency="d", adjustflag="3")
        #print('query_history_k_data_plus respond error_code:'+rs.error_code)
        #print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

        #### 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        #### 结果集输出到csv文件 ####
        locate = "./curday/"+cd+".csv"
        print(locate)
        result.to_csv(locate, index=False)
    #print(result)

    #### 登出系统 ####
    bs.logout()


# get sz50 stock data
def get_sz50_stock():

    # login baostock
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取上证50成分股
    rs = bs.query_sz50_stocks()
    print('query_sz50 error_code:'+rs.error_code)
    print('query_sz50  error_msg:'+rs.error_msg)

    # 打印结果集
    sz50_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        sz50_stocks.append(rs.get_row_data())
    result = pd.DataFrame(sz50_stocks, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("./save/sz50_stocks.csv", encoding="gbk", index=False)
    #print(result)

    # 登出系统
    bs.logout()

def query_hs300_stocks():
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取沪深300成分股
    rs = bs.query_hs300_stocks()
    print('query_hs300 error_code:'+rs.error_code)
    print('query_hs300  error_msg:'+rs.error_msg)

    # 打印结果集
    hs300_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        hs300_stocks.append(rs.get_row_data())
    result = pd.DataFrame(hs300_stocks, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("./save/hs300_stocks.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()

def query_zz500_stocks():
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取中证500成分股
    rs = bs.query_zz500_stocks()
    print('query_zz500 error_code:'+rs.error_code)
    print('query_zz500  error_msg:'+rs.error_msg)

    # 打印结果集
    zz500_stocks = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        zz500_stocks.append(rs.get_row_data())
    result = pd.DataFrame(zz500_stocks, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("./save/zz500_stocks.csv", encoding="gbk", index=False)
    print(result)

    # 登出系统
    bs.logout()



#get all stock inderstry
def get_all_stock_inderstry():
    # login baostock
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # 获取行业分类数据
    rs = bs.query_stock_industry()
    # rs = bs.query_stock_basic(code_name="浦发银行")
    print('query_stock_industry error_code:'+rs.error_code)
    print('query_stock_industry respond  error_msg:'+rs.error_msg)

    # 打印结果集
    industry_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        industry_list.append(rs.get_row_data())
    result = pd.DataFrame(industry_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("./save/stock_industry.csv", encoding="gbk", index=False)
    #print(result)

    # 登出系统
    bs.logout()

#get core forecast report

def get_forecast_report(code, startDate, endDate):

    #### login baostock ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取公司业绩预告 ####
    rs_forecast = bs.query_forecast_report(code, start_date=startDate, end_date=endDate)
    print('query_forecast_reprot respond error_code:'+rs_forecast.error_code)
    print('query_forecast_reprot respond  error_msg:'+rs_forecast.error_msg)
    rs_forecast_list = []
    while (rs_forecast.error_code == '0') & rs_forecast.next():
        # 分页查询，将每页信息合并在一起
        rs_forecast_list.append(rs_forecast.get_row_data())
    result_forecast = pd.DataFrame(rs_forecast_list, columns=rs_forecast.fields)
    #### 结果集输出到csv文件 ####
    result_forecast.to_csv("./forecast_report.csv", encoding="gbk", index=False)
    print(result_forecast)

    #### 登出系统 ####
    bs.logout()


def query_dividend_data(code, year, rsList):

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 查询除权除息信息####
    # 查询2015年除权除息信息
    rs_dividend = bs.query_dividend_data(code=code, year=year, yearType="report")
    while (rs_dividend.error_code == '0') & rs_dividend.next():
        rs_list.append(rs_dividend.get_row_data())

    result_dividend = pd.DataFrame(rs_list, columns=rs_dividend.fields)
    # 打印输出
    print(result_dividend)

    #### 结果集输出到csv文件 ####   
    result_dividend.to_csv("./save/history_Dividend_data.csv", encoding="gbk",index=False)

    #### 登出系统 ####
    bs.logout()
    return rsList


def query_history_k_data_plus(code, startDate, endDate,, freq, ajustFlag):
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取沪深A股估值指标(日频)数据 ####
    # peTTM    滚动市盈率
    # psTTM    滚动市销率
    # pcfNcfTTM    滚动市现率
    # pbMRQ    市净率
    rs = bs.query_history_k_data_plus("sh.600000",
        "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM",
        start_date='2015-01-01', end_date='2017-12-31', 
        frequency="d", adjustflag="3")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    result_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        result_list.append(rs.get_row_data())
    result = pd.DataFrame(result_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    result.to_csv("./save/history_A_stock_valuation_indicator_data.csv", encoding="gbk", index=False)
    print(result)

    #### 登出系统 ####
    bs.logout()



def query_stock_basic(code):
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)
    
    # 获取证券基本资料
    rs = bs.query_stock_basic(code="sh.600000")
    # rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
    print('query_stock_basic respond error_code:'+rs.error_code)
    print('query_stock_basic respond  error_msg:'+rs.error_msg)
    
    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("D:/stock_basic.csv", encoding="gbk", index=False)
    print(result)
    
    # 登出系统
    bs.logout()
