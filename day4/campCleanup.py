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


def find_same_prioities(first, second):#
    for item_first in first:
        for item_second in second:
            if item_first == item_second:
                return item_first


def calc(data):
    counter = 0
    counter_two = 0
    for item in data:
        pairs = item.split(",")
        start_low = start_high = end_low = end_high = 0

        first = pairs[0].split("-")
        second = pairs[1].split("-")

        first[0] = int(first[0])
        first[1] = int(first[1])
        second[0] = int(second[0])
        second[1] = int(second[1])

        if first[1] - first[0] < second[1] - second[0]:
            temp = first
            first = second
            second = temp
        
        #part one
        if first[0] == first[1]:
            if first[0] >= second[0] and first[0] <= second[1]:
                counter += 1

        elif second[0] == second[1]:
            if second[0] >= first[0] and second[0] <= first[1]:
                counter += 1

        elif first[0] <= second[0] and first[1] >= second[1]:
            counter += 1

        if first[0] >= second[0] and first[0] <= second[1]:
            counter_two += 1
        elif second[0] >= first[0] and second[0] <= first[1]:
            counter_two += 1
        #part two
        # if first[0] == first[1] and (first[0] >= second[0] and first[1] <= second[1]):
        #     counter_two += 1
        # elif second[0] == second[1] and (second[0] >= first[0] and second[1] <= first[1]):
        #     counter_two += 1
        # elif (first[0] >= second[0] and first[0] >= second[1]) or (second[0] >= first[0] and second[0] >= first[1]):
        #     counter_two += 1

    print("Part one: " + str(counter))
    print("Part two: " + str(counter_two))

def main():
    data = getData("input.csv")
    calc(data)


if __name__ == "__main__":
    main()