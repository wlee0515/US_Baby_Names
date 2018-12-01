import os
from pathlib import Path

from CEBD1160FP import NameInfoParser


# The folder name with the original data
def getInputDirectory():
    return "db_original"


# The folder name with the generated data
def getOutputDirectory():
    return "db_generated"


# Location to save the state population info
def getOutputStatePopulationDirectory():
    return os.path.join(getOutputDirectory(),"statepopulation")


# Location to save the name population info
def getOutputNamePopulationDirectory():
    return os.path.join(getOutputDirectory(),"namepopulation")


# Location  to find the state abbreviation data
def getStateAbbreviationCSV():
    return os.path.join(getInputDirectory(), "stateinfo/stateabbreviations.csv")


# Location  to find the state geocoordinate data
def getStateLocationCSV():
    return os.path.join(getInputDirectory(), "stateinfo/statelocation.csv")

# Location  to find the state Area data
def getStateAreaCSV():
    return os.path.join(getInputDirectory(), "stateinfo/statearea.csv")

# Location to find the name per state data
def getNameByStateCSVDirectory():
    return os.path.join(getInputDirectory(), "namesbystate")


# Output file name of the aggregation of the geographic data
def getOutputStateGeographyInfoCSV():
    return os.path.join(getOutputDirectory(), "stategeographyinfo.csv")


# Output file name of the USA population summary data
def getOutputUSAPopulationSummaryCSV():
    return os.path.join(getOutputDirectory(), "USAPopulationSummary.csv")


# Output file name of the Historical USA name count summary data
def getOutputHistoricalNameCountCSV():
    return os.path.join(getOutputDirectory(), "historicalnamecount.csv")


# Output file name of the working name list
def getOutputNameListCSV():
    return os.path.join(getOutputDirectory(), "namelist.csv")

# create directory function
def createAllDirectories():
    # check if output folder exits
    if False == os.path.exists(getOutputDirectory()):
        # if not exist, create
        os.makedirs(getOutputDirectory())
    # check if output folder exits
    if False == os.path.exists(getOutputStatePopulationDirectory()):
        # if not exist, create
        os.makedirs(getOutputStatePopulationDirectory())
    # check if output folder exits
    if False == os.path.exists(getOutputNamePopulationDirectory()):
        # if not exist, create
        os.makedirs(getOutputNamePopulationDirectory())

def main():

    # Object to parse Name information
    wNameInfoParser = NameInfoParser()

    # Initial step count
    wStepID = 0
    # Ending step count
    wExitStep = 10

    # loop though all steps
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
            wNameInfoParser.parseAbbreviationCSV(getStateAbbreviationCSV())
            wNameInfoParser.parseLocationCSV(getStateLocationCSV())
            wNameInfoParser.parseAreaCSV(getStateAreaCSV())
            print("Step {0}: Complete".format(wStepID))
        if 3 == wStepID:
            print("Step {0}: Sort and Purge Missing Abbreviations".format(wStepID))
            wNameInfoParser.purgeMissingAbbreviation()
            print("Step {0}: Complete".format(wStepID))
        if 4 == wStepID:
            print("Step {0}: Saving Summarized State Geography Data to Output".format(wStepID))
            wNameInfoParser.saveSummarizedStateGeographyDataData(getOutputStateGeographyInfoCSV())
            print("Step {0}: Complete".format(wStepID))
        if 5 == wStepID:
            print("Step {0}: Extracting Population data from data set".format(wStepID))
            wNameInfoParser.extractPopulationTable(getNameByStateCSVDirectory())
            print("Step {0}: Complete".format(wStepID))
        if 6 == wStepID:
            print("Step {0}: Saving Name List to Output Directory".format(wStepID))
            wNameInfoParser.saveNameList(getOutputNameListCSV())
            print("Step {0}: Complete".format(wStepID))
        if 7 == wStepID:
            print("Step {0}: Saving State Population data to Output Directory".format(wStepID))
            wNameInfoParser.saveStatePopulationData(getOutputStatePopulationDirectory(), getOutputUSAPopulationSummaryCSV())
            print("Step {0}: Complete".format(wStepID))
        if 8 == wStepID:
            print("Step {0}: Saving Name Population data to Output Directory".format(wStepID))
            wNameInfoParser.saveNamePopulationData(getOutputNamePopulationDirectory(), getOutputHistoricalNameCountCSV())
            print("Step {0}: Complete".format(wStepID))

if __name__ == "__main__":
    main()
