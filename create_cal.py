#!/usr/bin/python3

import pandas as pd
import getStock
import common_def
import os

#@N: need to calculate num days.
#@F: front day
#@T: today
#@R: rear day
#@D10: down to stop
#@U10: up to stop
#@G: green
#@R: red
#@C: continue
#
#Example: N4C_TU10_RG:

#第一天涨幅在20个点的股票
code_1d20 = []
inder_1d20 = []

#前一天涨停，今天未涨停，今天是绿色的
code_2d_r20_tgreen = []
inder_2d_r20_tgreen = []

#前一天涨停，今天未涨停，今天是红色的
code_2d_r20_tred = []
inder_2d_r20_tred = []

#计算三天，第三天涨停，前一天红色，今天绿色
code_3d_20_rreg_tgreen = []
inder_3d_20_rreg_tgreen = []

#计算4天，连续4天红色
code_4d_con_red = []
inder_4d_con_red = []

#计算5天 连续4天绿色， 第5天红色
code_5d_4green_1red = []
inder_5d_4green_1red = []

#计算连续6天， 2天红色， 两天绿色， 两天红色

def get_inderstry(codeList, newL):
    inder = open('./save/stock_industry.csv', 'r', encoding='gbk')
    lines = inder.readlines()

    for code in codeList:
        for line in lines:
            if code in line:
                newL.append(line[14:])


def output_data(name, code):
    sko.write(str(name), str(code))

def get_stock_list(getDate):
    clist = getStock.getStockCode(getDate)
    return clist

def get_stock_content(code):
    data = pd.read_csv("./curday/" + code + ".csv", encoding="gbk")
    #Ten days maybe enough to calculate.
    #get ten days data,
    sk = []
    for i in range(0, len(data)):
        tmp = tuple(data.loc[i])
        sk.append(list(tmp))
    if sk:
        return sk

#计算第一天涨停的股票
def _alg_cal_1d20_point(sk):
    if sk is None:
        return
    cnt = len(sk)
    if (cnt >= 2):
        if (sk[cnt-2][12] < common_def.zMiddle):
            if (sk[cnt-1][12] > common_def.zTing):
                code_1d20.append(sk[0][1])

def alg_cal_1d20_point(sko):
    sko.write("begin: 计算1天， 第一天涨停，根据行业选择是否购买\n")
    get_inderstry(code_1d20, inder_1d20)
    for i in range(len(inder_1d20)):
        sko.write(inder_1d20[i])

#计算前一天涨停，今天是绿色的
#code_2d_r20_tgreen = []
def _alg_cal_2d_r20_tgreen(sk):
    if sk is None:
        return
    cnt = len(sk)
    if(cnt >= 7):
        if (sk[cnt-7][2] > sk[cnt-7][5]):
            if (sk[cnt - 6][2] > sk[cnt - 6][5]):
                if (sk[cnt - 5][2] > sk[cnt - 5][5]):
                    if (sk[cnt - 4][2] > sk[cnt - 4][5]):
                        if (sk[cnt - 3][2] > sk[cnt - 3][5]):
                            if (sk[cnt - 2][2] > sk[cnt - 2][5]):
                                if (sk[cnt - 1][2] > sk[cnt - 1][5]):
                                    code_2d_r20_tgreen.append(sk[0][1])

def alg_cal_2d_r20_tgreen(sko):
    sko.write("\nbegin: 计算7天， 全是绿色的\n")
    get_inderstry(code_2d_r20_tgreen, inder_2d_r20_tgreen)
    for i in range(len(inder_2d_r20_tgreen)):
        sko.write(inder_2d_r20_tgreen[i])

#计算前一天涨停，今天是红色的
#code_2d_r20_tred = []
def _alg_cal_2d_r20_tred(sk):
    if sk is None:
        return
    cnt = len(sk)
    if (cnt >= 2):
       if (sk[cnt-2][2] < sk[cnt-2][5]):
           if (sk[cnt-1][2] > sk[cnt-1][5]):
               if (sk[cnt-1][5] > sk[cnt-2][5]):
                   code_2d_r20_tred.append(sk[0][1])

def alg_cal_2d_r20_tred(sko):
    sko.write("\nbegin: 计算2天， 前一天>9.5，今天高开，收盘绿，并且收盘价格大于昨天收盘价格\n")
    get_inderstry(code_2d_r20_tred, inder_2d_r20_tred)
    for i in range(len(inder_2d_r20_tred)):
        sko.write(inder_2d_r20_tred[i])



#计算三天，第三天涨停，前一天红色，今天绿色
#code_3d_20_rreg_tgreen = []
def _alg_cal_3d_20_rred_tgreen(sk):
    if sk is None:
        return
    cnt = len(sk)
    if (cnt >= 7):
        if (sk[cnt-7][2] < sk[cnt-7][5]):
            if (sk[cnt-6][2] > sk[cnt-6][5]):
                if (sk[cnt-5][2] > sk[cnt-5][5]):
                    if (sk[cnt-4][2] < sk[cnt-4][5]):
                        if (sk[cnt-3][2] > sk[cnt-3][5]):
                            if(sk[cnt-2][2] < sk[cnt-2][5]):
                                if (sk[cnt-1][2] > sk[cnt-1][5]):
                                    code_3d_20_rreg_tgreen.append(sk[0][1])


def alg_cal_3d_20_rred_tgreen(sko):
    sko.write("\nbegin: 计算6天，>7 G G R G R G\n")
    get_inderstry(code_3d_20_rreg_tgreen, inder_3d_20_rreg_tgreen)
    for i in range(len(inder_3d_20_rreg_tgreen)):
        sko.write(inder_3d_20_rreg_tgreen[i])

#计算4天，连续4天红色
#code_4d_con_red = []
def _alg_cal_4d_con_red(sk):
    if sk is None:
        return
    cnt = len(sk)
    if (cnt >= 3):
        if (sk[cnt-2][12] > 8.0):
            if (sk[cnt-1][2] < sk[cnt-3][5]):
                if (sk[cnt-0][2] < sk[cnt-2][5]):
                        code_4d_con_red.append(sk[0][1])

def alg_cal_4d_con_red(sko):
    sko.write("\nbegin: 计算3天， >8 R R\n")
    get_inderstry(code_4d_con_red, inder_4d_con_red)
    for i in range(len(inder_4d_con_red)):
        sko.write(inder_4d_con_red[i])

#计算5天，前四天绿色， 今天红色
#code_5d_4green_1red = []
def _alg_cal_5d_4green_1red(sk):
    if sk is None:
        return
    cnt = len(sk)
    if (cnt >= 5):
        if (sk[cnt-5][2] > sk[cnt-5][5]):
            if (sk[cnt-4][2] > sk[cnt-4][5]):
                if (sk[cnt-3][2] > sk[cnt-3][5]):
                    if (sk[cnt-2][2] > sk[cnt-2][5]):
                        if(sk[cnt-1][2] > sk[cnt-1][5]):
                            code_5d_4green_1red.append(sk[0][1])

def alg_cal_5d_4green_1red(sko):
    sko.write("\nbegin: 计算5天， 前4天绿色，今天红色\n")
    get_inderstry(code_5d_4green_1red, inder_5d_4green_1red)
    for i in range(len(inder_5d_4green_1red)):
        sko.write(inder_5d_4green_1red[i])



def alg_cal_call_func(clist):
    for c in clist:
        if c[3:6] == "300":
            filePath = "./curday/"+c+".csv"
            if os.path.exists(filePath):
                sk = get_stock_content(c)
                _alg_cal_4d_con_red(sk)

def alg_cal_output(creerFlag):
    if (creerFlag == 0):
        sko = open("./save/sksaveA.txt", "w", encoding='utf-8')
    if (creerFlag == 1):
        sko = open("./save/sksave.txt", "w", encoding='utf-8')
    alg_cal_4d_con_red(sko)
    alg_cal_5d_4green_1red(sko)
    alg_cal_2d_r20_tred(sko)

    sko.close()


def create_cal_main(getDate, creerFlag):
    clist = get_stock_list(getDate)
    alg_cal_call_func(clist)
    alg_cal_output(creerFlag)

