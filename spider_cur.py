#!/usr/bin/python3

import getStock
import K_line
#import time
#import os
#import pandas as pd

#爬取数据
def spider_cur(codeDate, startDate, endDate, creerFlag):
    start = startDate
    end = endDate

    code = getStock.getStockCode(codeDate, creerFlag)
    K_line.get_K_Line(code, start, end)


if __name__ == '__main__':
    print("This is for only spider\n")
    codeDate = "2022-03-15"
    startDate = "2022-03-01"
    endDate = "2020-03-16"
    creerFlag = 2
    spider_cur(codeDate, startDate, endDate, creerFlag)

