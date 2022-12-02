import csv
import os
import sys

def getData(fileName):
    strPath = os.path.join(sys.path[0], fileName)
    with open(strPath) as fileObject:
        data = fileObject.read().split('\n')

    retval = []
    for item in data:
        retval.append(item.split(" "))

    return retval

def calcScore(data):
    points_draw = 3
    points_loss = 0
    points_win = 6
    points_rock = 1
    points_paper = 2
    points_scissors = 3
    total_points = 0
    
    for item in data:
        if item[1] == 'X':
            item[1] = 'A'
        elif item[1] == 'Y':
            item[1] = 'B'
        elif item[1] == 'Z':
            item[1] = 'C'

        if item[0] == 'A' and item[1] == 'A':
            total_points += points_draw
            total_points += points_rock
        elif item[0] == 'A' and item[1] == 'B':
            total_points += points_win
            total_points += points_paper
        elif item[0] == 'A' and item[1] == 'C':
            total_points += points_loss
            total_points += points_scissors
        elif item[0] == 'B' and item[1] == 'A':
            total_points += points_loss
            total_points += points_rock
        elif item[0] == 'B' and item[1] == 'B':
            total_points += points_draw
            total_points += points_paper
        elif item[0] == 'B' and item[1] == 'C':
            total_points += points_win
            total_points += points_scissors
        elif item[0] == 'C' and item[1] == 'A':
            total_points += points_win
            total_points += points_rock
        elif item[0] == 'C' and item[1] == 'B':
            total_points += points_loss
            total_points += points_paper
        elif item[0] == 'C' and item[1] == 'C':
            total_points += points_draw
            total_points += points_scissors

    return total_points


def calcScorePartTwo(data):
    points_draw = 3
    points_loss = 0
    points_win = 6
    points_rock = 1
    points_paper = 2
    points_scissors = 3
    total_points = 0
    
    for item in data:
        if item[1] == 'X':
            total_points += points_loss
            if item[0] == 'A':
                total_points += points_scissors
            elif item[0] == 'B':
                total_points += points_rock
            elif item[0] == 'C':
                total_points += points_paper
        elif item[1] == 'Y':
            total_points += points_draw
            if item[0] == 'A':
                total_points += points_rock
            elif item[0] == 'B':
                total_points += points_paper
            elif item[0] == 'C':
                total_points += points_scissors    
        elif item[1] == 'Z':
            total_points += points_win
            if item[0] == 'A':
                total_points += points_paper
            elif item[0] == 'B':
                total_points += points_scissors
            elif item[0] == 'C':
                total_points += points_rock

    return total_points

def main():
    data_example = getData("inputExample.csv")
    print("Example: " + str(calcScore(data_example)))

    data_part_one = getData("input.csv")
    print("Part 1: " + str(calcScore(data_part_one)))

    data_part_two = getData("input.csv")
    print("Part 2: " + str(calcScorePartTwo(data_part_two)))

if __name__ == "__main__":
    main()