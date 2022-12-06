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


def part_one(data):
    sum = 0
    for backpack in data:
        common = find_same_prioities(backpack[0:int(len(backpack) / 2)], backpack[int(len(backpack) / 2):])
        sum += alc.index(common) + 1 if common in alc else auc.index(common) + 27
    
    return sum


def find_part_two(content):
    for item in content[0]:
        if item in content[1] and item in content[2]:
            return item

def part_two(data):
    sum = 0
    for i in range(int(len(data) / 3)):
        common = find_part_two([data[i * 3], data[i * 3 + 1], data[i * 3 + 2]])
        sum += alc.index(common) + 1 if common in alc else auc.index(common) + 27

    return sum

def main():
    data_example = getData("inputExample.csv")
    print("Example: " + str(part_one(data_example)))
    
    data_part_one = getData("input.csv")
    print("Part one: " + str(part_one(data_part_one)))
    
    data_part_two = getData("input.csv")
    print("Part two: " + str(part_two(data_part_two)))

if __name__ == "__main__":
    main()