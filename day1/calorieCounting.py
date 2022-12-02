import csv
import os
import sys

def getData(fileName):
    strPath = os.path.join(sys.path[0], fileName)
    with open(strPath) as fileObject:
        data = fileObject.read().split('\n')

    return data


def findMostCalories(data):
    most_calories = 0
    temp_sum = 0
    for item in data:
        if item == "":
            if temp_sum > most_calories:
                most_calories = temp_sum
            temp_sum = 0
        else:
            temp_sum += int(item)
    
    return most_calories


def findTopThreeCalories(data):
    most_calories = [0, 0, 0]
    temp_sum = 0
    for item in data:
        if item == "":
            if temp_sum > most_calories[0]:
                most_calories[0] = temp_sum
                most_calories.sort()
            temp_sum = 0
        else:
            temp_sum += int(item)

    if temp_sum > most_calories[0]:
        most_calories[0] = temp_sum

    return sum(most_calories)

def main():
    data_example = getData("inputExample.csv")
    print("Example: " + str(findMostCalories(data_example)))

    data_part_one = getData("input.csv")
    print("Part 1: " + str(findMostCalories(data_part_one)))

    data_part_two = getData("input.csv")
    print("Part 2: " + str(findTopThreeCalories(data_part_two)))

if __name__ == "__main__":
    main()