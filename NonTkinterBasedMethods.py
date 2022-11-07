import random
from tkinter import messagebox

# the only reason I have this file is so that there's less clutter than there already is in the main window file
# I don't like too much clutter because then my ADHD causes me to space out when reading walls of text
# What's not visible on GitHub is the metric-fuck-ton of collapsed regions I have on PyCharm.

floorKey = {
    0: "General Works",
    1: "History",
    2: "Technology",
    3: "Literature",
    4: "Art",
    5: "Natural Sciences",
    6: "Language",
    7: "Social Sciences",
    8: "Philosophy",
    9: "Religion"
}


def setArrayValues(floorList):
    for i in range(len(floorList)):
        if floorList[i] == '':
            floorList[i] = 0


def validateInformation(floorList):
    failedFloors = []
    for i in range(len(floorList)):

        try:
            int(floorList[i])

        except ValueError:
            failedFloors.append(i)
            floorList[i] = 0

    errorThrowingFloors = failedFloors

    errorString = '\n'

    for errors in errorThrowingFloors:
        errorString += str(floorKey[errors] + "\n")

    if len(errorThrowingFloors) > 0:
        messagebox.showerror("Error", message=f"One or more values has been entered incorrectly, you can view the "
                                              f"incorrect floors below:\n{errorString}")


def checkNuggetNumber(floorList):
    failedFloors = []
    for i in range(len(floorList)):
        floor = int(floorList[i])

        if floor < 0 or floor > 5:
            failedFloors.append(i)
            floorList[i] = 0
    errorThrowingFloors = failedFloors

    errorString = '\n'

    for errors in errorThrowingFloors:
        errorString += str(floorKey[errors] + "\n")

    if len(errorThrowingFloors) > 0:
        messagebox.showerror("Error", message=f"One or more floors has an incorrect number of nuggets provided, "
                                              f"you can view the floors throwing the error below:\n{errorString}")


def validateActInformation(actNumber):
    convertedNumber = int(actNumber)
    try:
        int(actNumber)
    except ValueError:
        return 0
    if convertedNumber <= 0 or convertedNumber > 10:
        return 0


def randomizeList(floorList, actNumber):
    numberOfActs = actNumber
    numberOfFloors = 0
    drawPool = []
    randomizedList = []

    for i in range(len(floorList)):
        if floorList[i] != 0:
            numberOfFloors += 1

    if numberOfFloors < numberOfActs:
        messagebox.showerror("Error",
                             message="The number of available floors you have provided is larger than the "
                                     "number of floors you have checked off.")
        numberOfActs = 0

    for i in range(len(floorList)):
        numberOfNuggets = int(floorList[i])
        floorType = floorKey[i]
        for n in range(numberOfNuggets):
            drawPool.append(floorType)
    while len(randomizedList) != numberOfActs:
        drawnFloor = random.choice(drawPool)
        if drawnFloor not in randomizedList:
            randomizedList.append(drawnFloor)

    return randomizedList
