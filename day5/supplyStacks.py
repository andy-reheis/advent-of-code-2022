import csv
import os
import sys
from string import ascii_lowercase as alc
from string import ascii_uppercase as auc


def getData(fileName):
    strPath = os.path.join(sys.path[0], fileName)
    with open(strPath) as fileObject:
        data = fileObject.read().split('\n')

    stacks = dict()
    instructions = []
    number_stacks = int(max(data[data.index("") - 1]))
    for i in range(0, number_stacks):
        stacks[i + 1] = []

    for i in range(0, data.index("") - 1):
        for j in range(0, number_stacks):
            if data[i][1 + j * 4] != " ":
                stacks[j + 1].append(data[i][1 + j * 4])

    for i in range(0, number_stacks):
        stacks[i + 1].reverse()

    for i in range(data.index("") + 1, len(data)):
        temp = data[i].split(" ")
        instructions.append([temp[1], temp[3], temp[5]])

    return stacks, instructions


def calc_one(stacks, instructions):
    for item in instructions:
        for i in range(0, int(item[0])):
            stacks[int(item[2])].append(stacks[int(item[1])].pop())

    result = ""
    for stack in stacks:
        result += stacks[stack][len(stacks[stack]) - 1]

    return result


def calc_two(stacks, instructions):
    for item in instructions:
        temp = []
        for i in range(0, int(item[0])):
            temp.append(stacks[int(item[1])].pop())
        temp.reverse()
        for elem in temp:
            stacks[int(item[2])].append(elem)

    result = ""
    for stack in stacks:
        result += stacks[stack][len(stacks[stack]) - 1]

    return result


def main():
    stacks, instructions = getData("input.csv")
    result = calc_one(stacks, instructions)
    print("Part one: " + str(result))

    stacks_two, instructions_two = getData("input.csv")
    result = calc_two(stacks_two, instructions_two)
    print("Part two: " + str(result))

if __name__ == "__main__":
    main()