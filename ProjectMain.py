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
            print("Step 1: Creating Output Directory")
            createAllDirectories()
            print("Step 1: Complete")
        if 2 == wStepID:
            print("Step 2: Parsing State Information")
            StateInfo.parseAbbreviationCSV(getStateAbbreviationCSV())
            StateInfo.parseLocationCSV(getStateLocationCSV())
            StateInfo.parseAreaCSV(getStateAreaCSV())
            print("Step 2: Complete")
        if 3 == wStepID:
            print("Step 3: Sort and Purge Missing Abbreviations")
            StateInfo.sortAndPurgeMissingAbbreviation()
            print("Step 3: Complete")
        if 4 == wStepID:
            print("Step 4: Saving Summarized State Geography Data to Output")
            StateInfo.saveSummarizedStateGeographyDataData(getOutputStateGeographyInfoCSV())
            print("Step 4: Complete")
        if 5 == wStepID:
            print("Step 5: Extracting Population data from data set")
            StateInfo.extractPopulationTable(getNameByStateCSVDirectory())
            print("Step 5: Complete")
        if 6 == wStepID:
            print("Step 6: Saving State Population data to Output Directory")
            StateInfo.saveStatePopulationData(getOutputStatePopulationDirectory(), getOutputUSAPopulationSummaryCSV())
            print("Step 6: Complete")
        if 7 == wStepID:
            print("Step 7: Saving Name Population data to Output Directory")
            StateInfo.saveNamePopulationData(getOutputNamePopulationDirectory(), getOutputHistoricalNameCountCSV())
            print("Step 7: Complete")

if __name__ == "__main__":
    main()