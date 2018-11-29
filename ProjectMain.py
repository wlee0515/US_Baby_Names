import os
from pathlib import Path

from CEBD1160FP import StateInfo


def getInputDirectory():
    return "db_original"


def getOutputDirectory():
    return "db_generated"


def getOutputStatePopulationDirectory():
    return os.path.join(getOutputDirectory(),"statepopulation")


def getOutputNamePopulationDirectory():
    return os.path.join(getOutputDirectory(),"namepopulation")


def getStateAbbreviationCSV():
    return os.path.join(getInputDirectory(), "stateinfo/stateabbreviations.csv")


def getStateLocationCSV():
    return os.path.join(getInputDirectory(), "stateinfo/statelocation.csv")


def getStateAreaCSV():
    return os.path.join(getInputDirectory(), "stateinfo/statearea.csv")


def getNameByStateCSVDirectory():
    return os.path.join(getInputDirectory(), "namesbystate")


def getOutputStateGeographyInfoCSV():
    return os.path.join(getOutputDirectory(), "stategeographyinfo.csv")


def getOutputUSAPopulationSummaryCSV():
    return os.path.join(getOutputDirectory(), "USAPopulationSummary.csv")


def getOutputHistoricalNameCountCSV():
    return os.path.join(getOutputDirectory(), "historicalnamecount.csv")


def getOutputNameListCSV():
    return os.path.join(getOutputDirectory(), "namelist.csv")

def createAllDirectories():
    # check if temporary folder exits
    if False == os.path.exists(getOutputDirectory()):
        # if not exist, create
        os.makedirs(getOutputDirectory())
    # check if temporary folder exits
    if False == os.path.exists(getOutputStatePopulationDirectory()):
        # if not exist, create
        os.makedirs(getOutputStatePopulationDirectory())
    # check if temporary folder exits
    if False == os.path.exists(getOutputNamePopulationDirectory()):
        # if not exist, create
        os.makedirs(getOutputNamePopulationDirectory())

def main():

    wStepID = 0
    wExitStep = 10
    for wCount in range(0,10):
        if wExitStep == wStepID:
            break
        wStepID += 1

        if 1 == wStepID:
            print("Step {0}: Creating Output Directory".format(wStepID))
            createAllDirectories()
            print("Step {0}: Complete".format(wStepID))
        if 2 == wStepID:
            print("Step {0}: Parsing State Information".format(wStepID))
            StateInfo.parseAbbreviationCSV(getStateAbbreviationCSV())
            StateInfo.parseLocationCSV(getStateLocationCSV())
            StateInfo.parseAreaCSV(getStateAreaCSV())
            print("Step {0}: Complete".format(wStepID))
        if 3 == wStepID:
            print("Step {0}: Sort and Purge Missing Abbreviations".format(wStepID))
            StateInfo.sortAndPurgeMissingAbbreviation()
            print("Step {0}: Complete".format(wStepID))
        if 4 == wStepID:
            print("Step {0}: Saving Summarized State Geography Data to Output".format(wStepID))
            StateInfo.saveSummarizedStateGeographyDataData(getOutputStateGeographyInfoCSV())
            print("Step {0}: Complete".format(wStepID))
        if 5 == wStepID:
            print("Step {0}: Extracting Population data from data set".format(wStepID))
            StateInfo.extractPopulationTable(getNameByStateCSVDirectory())
            print("Step {0}: Complete".format(wStepID))
        if 6 == wStepID:
            print("Step {0}: Saving Name List to Output Directory".format(wStepID))
            StateInfo.saveNameList(getOutputStatePopulationDirectory(), getOutputNameListCSV())
            print("Step {0}: Complete".format(wStepID))
        if 7 == wStepID:
            print("Step {0}: Saving State Population data to Output Directory".format(wStepID))
            StateInfo.saveStatePopulationData(getOutputStatePopulationDirectory(), getOutputUSAPopulationSummaryCSV())
            print("Step {0}: Complete".format(wStepID))
        if 8 == wStepID:
            print("Step {0}: Saving Name Population data to Output Directory".format(wStepID))
            StateInfo.saveNamePopulationData(getOutputNamePopulationDirectory(), getOutputHistoricalNameCountCSV())
            print("Step {0}: Complete".format(wStepID))

if __name__ == "__main__":
    main()
