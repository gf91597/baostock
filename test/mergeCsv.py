#!/usr/bin/python3


def merge_csv_file(bak, cur):
    print("merge csv file")
    print(bak)
    print(cur)
    curF = open(cur, "r+")
    bakF = open(bak, "a+")

    lines = curF.readlines()

    cnt = len(lines) - 1

    for i in range(cnt):
        bakF.write(lines[i+1])

    curF.close()
    bakF.close()

