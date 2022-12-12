import csv
import os
import sys
from string import ascii_lowercase as alc
from string import ascii_uppercase as auc


def getData(fileName):
    strPath = os.path.join(sys.path[0], fileName)
    with open(strPath) as fileObject:
        data = fileObject.read().split('\n')

    return data


def all_distinct(list):
    return len(set(list)) == len(list)


def calc(data, range):
    start = 0
    end = range
    item = data[start:end]
    indicator = all_distinct(item)
    while not indicator:
        start += 1
        end += 1
        item = data[start:end]
        indicator = all_distinct(item)

    print(end)



def main():
    data = getData("input.csv")
    calc(data[0], 4)
    calc(data[0], 14)


if __name__ == "__main__":
    main()