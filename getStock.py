#!/usr/bin/python3
import baostock as bs
import pandas as pd

def test():
    print("in get Stock")

def getStockCode(date, creerFlag):
    #### 登陆系统 ####
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


    ## data_list format: ['sz.399682', '1', '医药行业']
    ## print(data_list)
    #result = pd.DataFrame(data_list, columns=rs.fields)
    ## 结果集输出到csv文件 ####
    #result.to_csv("D:\\all_stock.csv", encoding="gbk", index=False)
    #print(result)

    #### 登出系统 ####
    bs.logout()
    return code
#date = '2020-10-21'
#getStockCode(date)
