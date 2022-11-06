import NotWindow

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.geometry('450x400')
window.title("LoR Floor Randomizer")
tabControl = ttk.Notebook(window)

# randomizer tab
randomizerTab = ttk.Frame(tabControl)
tabControl.add(randomizerTab, text="Floor Randomizer")


# methods
def getFloorInformation():
    generalWorksCount = generalEntry.get()
    historyCount = historyEntry.get()
    technologyCount = technologyEntry.get()
    literatureCount = litEntry.get()
    artCount = artEntry.get()
    natSciCount = natSciEntry.get()
    languageCount = languageEntry.get()
    socSciCount = socSciEntry.get()
    philosophyCount = philosophyEntry.get()
    religionCount = religionEntry.get()

    floorList = [generalWorksCount, historyCount, technologyCount, literatureCount, artCount,
                 natSciCount, languageCount, socSciCount,
                 philosophyCount, religionCount]
    NotWindow.setArrayValues(floorList)

    return floorList


def getActInformation():
    numberOfActs = actsNumber.get()

    if NotWindow.validateActInformation(numberOfActs) == 0:
        messagebox.showerror("Error",
                             message="You have provided an invalid input for the number of acts, please try again")
        actsNumber.delete(0, END)

    return int(numberOfActs)


def generateRandomFloorList():
    # check floor information
    acquiredFloorValues = getFloorInformation()
    NotWindow.validateInformation(acquiredFloorValues)
    NotWindow.checkNuggetNumber(acquiredFloorValues)

    # get number of acts
    numberOfActs = getActInformation()

    # randomize information

    randomizedList = NotWindow.randomizeList(acquiredFloorValues, numberOfActs)
    randomizedFloorList.delete(0, END)
    for i in range(len(randomizedList)):
        randomizedFloorList.insert(i, randomizedList[i])


def updatePage():
    if generalCheckVar.get() == 0:
        generalEntry.config(state=DISABLED)
    else:
        generalEntry.config(state=NORMAL)

    if historyCheckVar.get() == 0:
        historyEntry.config(state=DISABLED)
    else:
        historyEntry.config(state=NORMAL)

    if technologyCheckVar.get() == 0:
        technologyEntry.config(state=DISABLED)
    else:
        technologyEntry.config(state=NORMAL)

    if litCheckVar.get() == 0:
        litEntry.config(state=DISABLED)
    else:
        litEntry.config(state=NORMAL)

    if artCheckVar.get() == 0:
        artEntry.config(state=DISABLED)
    else:
        artEntry.config(state=NORMAL)

    if natSciCheckVar.get() == 0:
        natSciEntry.config(state=DISABLED)
    else:
        natSciEntry.config(state=NORMAL)

    if languageCheckVar.get() == 0:
        languageEntry.config(state=DISABLED)
    else:
        languageEntry.config(state=NORMAL)

    if socSciCheckVar.get() == 0:
        socSciEntry.config(state=DISABLED)
    else:
        socSciEntry.config(state=NORMAL)

    if philosophyCheckVar.get() == 0:
        philosophyEntry.config(state=DISABLED)
    else:
        philosophyEntry.config(state=NORMAL)

    if religionCheckVar.get() == 0:
        religionEntry.config(state=DISABLED)
    else:
        religionEntry.config(state=NORMAL)


def checkAll():
    generalCheck.select()
    historyCheck.select()
    technologyCheck.select()
    litCheck.select()
    artCheck.select()
    natSciCheck.select()
    languageCheck.select()
    socSciCheck.select()
    philosophyCheck.select()
    religionCheck.select()
    updatePage()


def unCheckAll():
    historyCheck.deselect()
    technologyCheck.deselect()
    litCheck.deselect()
    artCheck.deselect()
    natSciCheck.deselect()
    languageCheck.deselect()
    socSciCheck.deselect()
    philosophyCheck.deselect()
    religionCheck.deselect()
    updatePage()


def resetTextBoxes():
    generalEntry.delete(0, END)
    historyEntry.delete(0, END)
    technologyEntry.delete(0, END)
    litEntry.delete(0, END)
    artEntry.delete(0, END)
    natSciEntry.delete(0, END)
    languageEntry.delete(0, END)
    socSciEntry.delete(0, END)
    philosophyEntry.delete(0, END)
    religionEntry.delete(0, END)


def resetConfig():
    resetTextBoxes()
    unCheckAll()
    actsNumber.delete(0, END)
    randomizedFloorList.delete(0, END)


# frames

informationFrame = Frame(window)
selectDeselectFrame = Frame(window)
updateFrame = Frame(window)
randomizedFloorsFrame = Frame(window)
numberOfActsFrame = Frame(randomizedFloorsFrame)
# titles

floorLabel = Label(informationFrame, text="Floor:", padx=5, font="Arial 10 underline")
floorLabel.grid(row=0, column=0)
nuggetNumberLabel = Label(informationFrame, text="# of Nuggets:", padx=5, font="Arial 10 underline")
nuggetNumberLabel.grid(row=0, column=2)

# general works

generalCheckVar = IntVar(informationFrame)

generalLabel = Label(informationFrame, text="General Works: ")
generalLabel.grid(row=1, column=0)

generalCheck = Checkbutton(informationFrame, variable=generalCheckVar, onvalue=1, offvalue=0)
generalCheck.grid(row=1, column=1)
generalCheck.select()

generalEntry = Entry(informationFrame, width=10)
generalEntry.grid(row=1, column=2)

# history

historyCheckVar = IntVar(informationFrame)

historyLabel = Label(informationFrame, text="History:")
historyLabel.grid(row=2, column=0)

historyCheck = Checkbutton(informationFrame, variable=historyCheckVar, onvalue=1, offvalue=0)
historyCheck.grid(row=2, column=1)

historyEntry = Entry(informationFrame, width=10)
historyEntry.grid(row=2, column=2)
historyEntry.config(state=DISABLED)

# technological sciences

technologyCheckVar = IntVar(informationFrame)

technologyLabel = Label(informationFrame, text="Technological Sciences: ")
technologyLabel.grid(row=3, column=0)

technologyCheck = Checkbutton(informationFrame, variable=technologyCheckVar, onvalue=1, offvalue=0)
technologyCheck.grid(row=3, column=1)

technologyEntry = Entry(informationFrame, width=10)
technologyEntry.grid(row=3, column=2)
technologyEntry.config(state=DISABLED)

# literature

litCheckVar = IntVar(informationFrame)

litLabel = Label(informationFrame, text="Literature:")
litLabel.grid(row=4, column=0)

litCheck = Checkbutton(informationFrame, variable=litCheckVar, onvalue=1, offvalue=0)
litCheck.grid(row=4, column=1)

litEntry = Entry(informationFrame, width=10)
litEntry.grid(row=4, column=2)
litEntry.config(state=DISABLED)

# art

artCheckVar = IntVar(informationFrame)

artLabel = Label(informationFrame, text="Art:")
artLabel.grid(row=5, column=0)

artCheck = Checkbutton(informationFrame, variable=artCheckVar, onvalue=1, offvalue=0)
artCheck.grid(row=5, column=1)

artEntry = Entry(informationFrame, width=10)
artEntry.grid(row=5, column=2)
artEntry.config(state=DISABLED)

# natural sciences

natSciCheckVar = IntVar(informationFrame)

natSciLabel = Label(informationFrame, text="Natural Sciences:")
natSciLabel.grid(row=6, column=0)

natSciCheck = Checkbutton(informationFrame, variable=natSciCheckVar, onvalue=1, offvalue=0)
natSciCheck.grid(row=6, column=1)

natSciEntry = Entry(informationFrame, width=10)
natSciEntry.grid(row=6, column=2)
natSciEntry.config(state=DISABLED)

# language

languageCheckVar = IntVar(informationFrame)

languageLabel = Label(informationFrame, text="Language:")
languageLabel.grid(row=7, column=0)

languageCheck = Checkbutton(informationFrame, variable=languageCheckVar, onvalue=1, offvalue=0)
languageCheck.grid(row=7, column=1)

languageEntry = Entry(informationFrame, width=10)
languageEntry.grid(row=7, column=2)
languageEntry.config(state=DISABLED)

# social sciences

socSciCheckVar = IntVar(informationFrame)

socSciLabel = Label(informationFrame, text="Social Sciences:")
socSciLabel.grid(row=8, column=0)

socSciCheck = Checkbutton(informationFrame, variable=socSciCheckVar, onvalue=1, offvalue=0)
socSciCheck.grid(row=8, column=1)

socSciEntry = Entry(informationFrame, width=10)
socSciEntry.grid(row=8, column=2)
socSciEntry.config(state=DISABLED)

# philosophy

philosophyCheckVar = IntVar(informationFrame)

philosophyLabel = Label(informationFrame, text="Philosophy:")
philosophyLabel.grid(row=9, column=0)

philosophyCheck = Checkbutton(informationFrame, variable=philosophyCheckVar, onvalue=1, offvalue=0)
philosophyCheck.grid(row=9, column=1)

philosophyEntry = Entry(informationFrame, width=10)
philosophyEntry.grid(row=9, column=2)
philosophyEntry.config(state=DISABLED)

# religion

religionCheckVar = IntVar(informationFrame)

religionLabel = Label(informationFrame, text="Religion:")
religionLabel.grid(row=10, column=0)

religionCheck = Checkbutton(informationFrame, variable=religionCheckVar, onvalue=1, offvalue=0)
religionCheck.grid(row=10, column=1)

religionEntry = Entry(informationFrame, width=10)
religionEntry.grid(row=10, column=2)
religionEntry.config(state=DISABLED)

# numbers of acts frame


actsLabel = Label(numberOfActsFrame, text="Please provide the number \nof acts in the reception: ")
actsNumber = Entry(numberOfActsFrame)

actsLabel.grid(row=0, column=0)
actsNumber.grid(row=1, column=0)

# buttons

checkAllButton = Button(selectDeselectFrame, text="Check All Floors", command=checkAll)
checkAllButton.pack(side=LEFT, padx=3)

unCheckAllButton = Button(selectDeselectFrame, text="Uncheck All Floors", command=unCheckAll)
unCheckAllButton.pack(side=LEFT, padx=3)

refreshButton = Button(updateFrame, text="Update Floor \nAvailability", command=updatePage)
refreshButton.pack(side=LEFT, padx=3)

resetButton = Button(updateFrame, text="Reset \nConfigurations", command=resetConfig)
resetButton.pack(side=LEFT, padx=10)

getInformationButton = Button(randomizedFloorsFrame, text="Randomize Floors", command=generateRandomFloorList)
getInformationButton.grid(row=1, column=0, pady=(5, 0))

# listbox

randomizedFloorList = Listbox(randomizedFloorsFrame, width=25)
randomizedFloorList.grid(row=2, column=0, pady=5)

# pack stuff

# frames
informationFrame.grid(row=0, column=0, pady=5)
selectDeselectFrame.grid(row=1, column=0, pady=5)
updateFrame.grid(row=2, column=0, pady=5)
numberOfActsFrame.grid(row=0, column=0, pady=5)
randomizedFloorsFrame.grid(row=0, column=1, pady=5)

# tabs


# instructions tab


# start the application
window.mainloop()
