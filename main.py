import common_def
import getStock
import spider_cur
import create_cal
import get_stock_inderstry
import datetime
import sys

def cal_creer_stock(codeDate, creerFlag):
    common_def.zTing = 19.30
    common_def.zMiddle = 18.0
    common_def.dMiddle = -11.0
    create_cal.create_cal_main(codeDate, creerFlag)

def cal_A_stock(codeDate, creerFlag):
    common_def.zTing = 9.30
    common_def.zMiddle = 8.0
    common_def.dMiddle = -5.0
    create_cal.create_cal_main(codeDate, creerFlag)

if __name__ == "__main__":
    spider = 0
    creerFlag = 0
    cal = 0

    if len(sys.argv) == 0:
        pass
    elif len(sys.argv) == 2:
        spider = int(sys.argv[1])
    elif len(sys.argv) == 3:
        spider = int(sys.argv[1])
    elif len(sys.argv) == 4:
        spider = int(sys.argv[1])
    else :
        print('Usage: ' + sys.argv[0] + ' [spider] ' + '[creerFlag]')
        print('spider: 0 do not get data, 1 get stock data')
        print('creerFlag: 0 A, 1 creer, 2 all, others do nothing')
        exit(1)

#get inderstry may not be used
#    get_stock_inderstry.get_all_stock_inderstry()

    today = datetime.datetime.today()
    delta = datetime.timedelta(days=5)
    before_20_days = today - delta
    # 将日期转换为指定格式的字符串
    startDate = before_20_days.strftime("%Y-%m-%d")
    endDate = today.strftime("%Y-%m-%d")
    codeDate = startDate

    print(startDate)
    print(endDate)


    if (spider):
        print("need to spider\n")
        spider_cur.spider_cur(codeDate, startDate, endDate)
    else:
        print("no need spider\n")

#    if cal == 1:
#        if (creerFlag == 0):
#            cal_A_stock(codeDate, creerFlag)
#        elif (creerFlag == 1):
#            cal_creer_stock(codeDate, creerFlag)
#        else:
#            print("do nothing, please set creerFlag as 0, 1, 2")
#    else:
#        print("do not cal anything\n")
#        pass

