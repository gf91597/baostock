#!/usr/bin/python3


import baoStockOps as bso

if __name__ == "__main__":
    ''' Test all api '''
    #bso.get_all_stock_inderstry()
    #bso.get_sz50_stock()
    rsList = []
    bso.get_forecast_report("sz.600000", "2022-03-02", "2022-09-03")
