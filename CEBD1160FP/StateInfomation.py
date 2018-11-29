from os import walk
from os import path


class NameData:
    def __init__(self):
        self.Sex = {}
        self.Count = 0

class Population:
    def __init__(self):
        self.Total = 0
        self.Male = 0
        self.Female = 0
        self.NameSet = {}

class StateInformation:
    def __init__(self, name):
        self.Name = name
        self.Abbreviation = ""
        self.Latitude = 0.0
        self.Longitude = 0.0
        self.Area = 0.0
        self.PopulationTable = {}

gNameList = {}
gTotalUSPopulation = {}
gStateInformationDictionary = {}


class StateInfo:

    def getStateInformationDictionary():
        return gStateInformationDictionary;

    def getStateInfomationByName(name):
        if name in gStateInformationDictionary:
            return gStateInformationDictionary[name]
        return None

    def getStateInfomationByAbbreviation(abbreviation):
        for wName, wState in gStateInformationDictionary.items():
            if abbreviation == gStateInformationDictionary[wName].Abbreviation:
                return gStateInformationDictionary[wName]
        return None

    def addStateName(name):
        if name not in gStateInformationDictionary:
            gStateInformationDictionary[name] = StateInformation(name)

    def setStateAbbreviation(name, abbreviation):
        StateInfo.addStateName(name)
        gStateInformationDictionary[name].Abbreviation = abbreviation

    def setStateLocation(name, latitude, longitude):
        StateInfo.addStateName(name)
        wState = gStateInformationDictionary[name]
        wState.Latitude = latitude
        wState.Longitude = longitude

    def setStateArea(name, area):
        StateInfo.addStateName(name)
        gStateInformationDictionary[name].Area = area

    def setNameList(name, sex, count):
        wNameData = gNameList[name] = NameData()
        wNameData.Count = count
        wNameData.Sex[sex] = 1
            
    def addToNameList(name, sex, count):
        if name not in gNameList:
            wNameData = gNameList[name] = NameData()
            wNameData.Count = count
            wNameData.Sex[sex] = 1
        else:
            wNameData = gNameList[name]
            wNameData.Count = count
            wNameData.Sex[sex] = 1
            
    def setTotalPopulation(year, population, malecount, femalecount, name=""):
        if year not in gTotalUSPopulation:
            gTotalUSPopulation[year] = Population()
        wPopulation = gTotalUSPopulation[year]
        wPopulation.Total = population
        wPopulation.Male = malecount
        wPopulation.Female = femalecount
        if "" != name:
            wPopulation.NameSet[name] = population

    def addToTotalPopulation(year, population, malecount, femalecount, name=""):
        if year not in gTotalUSPopulation:
            gTotalUSPopulation[year] = Population()
        wPopulation = gTotalUSPopulation[year]
        wPopulation.Total += population
        wPopulation.Male += malecount
        wPopulation.Female += femalecount
        if "" != name:
            if name not in wPopulation.NameSet:
                wPopulation.NameSet[name] = 0
            wPopulation.NameSet[name] += population

    def setStatePopulation(stateAbbr, year, population, malecount, femalecount, name=""):
        StateInfo.addStateName(stateAbbr)
        wState = gStateInformationDictionary[stateAbbr]
        if year not in wState.PopulationTable:
            wState.PopulationTable[year] = Population()
        wPopulation = wState.PopulationTable[year]
        wPopulation.Total = population
        wPopulation.Male = malecount
        wPopulation.Female = femalecount
        if "" != name:
            wPopulation.NameSet[name] = population

    def addStatePopulation(stateAbbr, year, population, malecount, femalecount, name=""):
        StateInfo.addStateName(stateAbbr)
        wState = gStateInformationDictionary[stateAbbr]
        if year not in wState.PopulationTable:
            wState.PopulationTable[year] = Population()
        wPopulation = wState.PopulationTable[year]
        wPopulation.Total += population
        wPopulation.Male += malecount
        wPopulation.Female += femalecount
        if "" != name:
            if name not in wPopulation.NameSet:
                wPopulation.NameSet[name] = 0
            wPopulation.NameSet[name] += population

    def parseAbbreviationCSV(filename):
        wFileHandler = open(filename, 'r')
        if 'r' == wFileHandler.mode:
            print("Parsing file : {0}".format(filename))
            wFileData = wFileHandler.readlines()
            for wLine in wFileData:
                wLine = wLine.strip("\n")
                wData = wLine.split(",")
                if 4 <= len(wData):
                    StateInfo.addStateName(wData[0])
                    StateInfo.setStateAbbreviation(wData[0], wData[3])
        wFileHandler.close()

    def parseLocationCSV(filename):
        wFileHandler = open(filename, 'r')
        if 'r' == wFileHandler.mode:
            print("Parsing file : {0}".format(filename))
            wFileData = wFileHandler.readlines()
            for wLine in wFileData:
                wLine = wLine.strip("\n")
                wData = wLine.split(",")
                if 3 <= len(wData):
                    StateInfo.addStateName(wData[0])
                    StateInfo.setStateLocation(wData[0], float(wData[1]), float(wData[2]))
        wFileHandler.close()

    def parseAreaCSV(filename):
        wFileHandler = open(filename, 'r')
        if 'r' == wFileHandler.mode:
            print("Parsing file : {0}".format(filename))
            wFileData = wFileHandler.readlines()
            for wLine in wFileData:
                wLine = wLine.strip("\n")
                wData = wLine.split(",")
                if 4 <= len(wData):
                    StateInfo.addStateName(wData[0])
                    StateInfo.setStateArea(wData[0], float(wData[3]))
        wFileHandler.close()

    def sortAndPurgeMissingAbbreviation():
        wListToDelete=[]
        for wName, wState in gStateInformationDictionary.items():
            if "" == wState.Abbreviation:
                wListToDelete.append(wName)
        for wName in wListToDelete:
            gStateInformationDictionary.pop(wName)

    def extractPopulationTable(inputDirectory):
        # List of files to process
        wFileList = []
        # walk through all sub folders and files in the provided path
        for (wPath, wDirectories, wFileNames) in walk(inputDirectory):
            # Loop through all file names
            for wFile in wFileNames:
                #  Add the direct path to the file list
                wFileList.append(path.join(wPath, wFile))
            # break after first iteration to only get the list of files in the provided directory
            break
        # if the file list is 0, return
        if 0 == len(wFileList):
            return
        for wFilename in wFileList:
            wFileHandler = open(wFilename, 'r')
            wState = None
            if 'r' == wFileHandler.mode:
                print("Parsing file : {0}".format(wFilename))
                wFileData = wFileHandler.readlines()
                for wLine in wFileData:
                    wLine = wLine.strip("\n")
                    wData = wLine.split(",")
                    if 4 <= len(wData):
                        if None == wState:
                            wState = StateInfo.getStateInfomationByAbbreviation(wData[0])
                        elif wState.Abbreviation != wData[0]:
                            wState = StateInfo.getStateInfomationByAbbreviation(wData[0])
                        if None != wState:
                            wMaleCount = 0
                            wFemaleCount = 0
                            if "M" == wData[1]:
                                wMaleCount = int(wData[4])
                            if "F" == wData[1]:
                                wFemaleCount = int(wData[4])
                            StateInfo.addStatePopulation(wState.Name, int(wData[2]), int(wData[4]), wMaleCount, wFemaleCount, wData[3])
                            StateInfo.addToTotalPopulation( int(wData[2]), int(wData[4]), wMaleCount, wFemaleCount,  wData[3])
                            StateInfo.addToNameList(wData[3], wData[1], int(wData[4]))
                wFileHandler.close()

    def saveNameList(outputfilename):
        print("Saving Name List")
        wFileHandler = open(outputfilename, 'w')
        if 'w' == wFileHandler.mode:
            wDataLine = ""
            wDataLine += "{0}".format("Name")
            wDataLine += ",{0}".format("Sex")
            wDataLine += ",{0}".format("Count")
            wFileHandler.write("{0}\n".format(wDataLine))
            for wName in sorted(gNameList.keys()):
                wData = gNameList[wName]
                wDataLine = ""
                wDataLine += "{0}".format(wName)
                if "M" in wData.Sex:
                    if "F" in wData.Sex:
                        wDataLine += ",{0}".format("U")
                    else:
                        wDataLine += ",{0}".format("M")
                else:
                    if "F" in wData.Sex:
                        wDataLine += ",{0}".format("F")
                    else:
                        wDataLine += ",{0}".format("NA")
                wDataLine += ",{0}".format(wData.Count)
                wFileHandler.write("{0}\n".format(wDataLine))
        wFileHandler.close()
    
    
    def saveSummarizedStateGeographyDataData(outputfilename):
        print("Saving USA state geography data")
        wFileHandler = open(outputfilename, 'w')
        if 'w' == wFileHandler.mode:
            wDataLine = ""
            wDataLine += "{0}".format("State")
            wDataLine += ",{0}".format("Abbreviation")
            wDataLine += ",{0}".format("Latitude_deg")
            wDataLine += ",{0}".format("Longitude_deg")
            wDataLine += ",{0}".format("Area_sq-Km")
            wFileHandler.write("{0}\n".format(wDataLine))
            for wName, wState in gStateInformationDictionary.items():
                wDataLine = ""
                wDataLine += "{0}".format(wState.Name)
                wDataLine += ",{0}".format(wState.Abbreviation)
                wDataLine += ",{0}".format(wState.Latitude)
                wDataLine += ",{0}".format(wState.Longitude)
                wDataLine += ",{0}".format(wState.Area)
                wFileHandler.write("{0}\n".format(wDataLine))
        wFileHandler.close()

    def saveStatePopulationData(outputDirectory, outputUSAPopulationFileName):
        for wName, wState in gStateInformationDictionary.items():
            print("Saving State population summary of {0}".format(wName))
            wFilename = outputDirectory + "/" + wState.Abbreviation + ".csv"
            wFileHandler = open(wFilename, 'w')
            if 'w' == wFileHandler.mode:
                wDataLine = ""
                wDataLine += "{0}".format("state")
                wDataLine += ",{0}".format("year")
                wDataLine += ",{0}".format("totalPopulation")
                wDataLine += ",{0}".format("malePopulation")
                wDataLine += ",{0}".format("femalePopulation")
                wDataLine += ",{0}".format("uniqueNames")
                wFileHandler.write("{0}\n".format(wDataLine))
                for wYear, wPopulation in wState.PopulationTable.items():
                    wDataLine = ""
                    wDataLine += "{0}".format(wState.Abbreviation)
                    wDataLine += ",{0}".format(wYear)
                    wDataLine += ",{0}".format(wPopulation.Total)
                    wDataLine += ",{0}".format(wPopulation.Male)
                    wDataLine += ",{0}".format(wPopulation.Female)
                    wDataLine += ",{0}".format(len(wPopulation.NameSet))
                    wFileHandler.write("{0}\n".format(wDataLine))
            wFileHandler.close()

        print("Saving USA population summary")
        wFileHandler = open(outputUSAPopulationFileName, 'w')
        if 'w' == wFileHandler.mode:
            wDataLine = ""
            wDataLine += "{0}".format("state")
            wDataLine += ",{0}".format("year")
            wDataLine += ",{0}".format("totalPopulation")
            wDataLine += ",{0}".format("malePopulation")
            wDataLine += ",{0}".format("femalePopulation")
            wDataLine += ",{0}".format("uniqueNames")
            wFileHandler.write("{0}\n".format(wDataLine))
            for wYear, wPopulation in gTotalUSPopulation.items():
                wDataLine = ""
                wDataLine += "{0}".format("USA")
                wDataLine += ",{0}".format(wYear)
                wDataLine += ",{0}".format(wPopulation.Total)
                wDataLine += ",{0}".format(wPopulation.Male)
                wDataLine += ",{0}".format(wPopulation.Female)
                wDataLine += ",{0}".format(len(wPopulation.NameSet))
                wFileHandler.write("{0}\n".format(wDataLine))
        wFileHandler.close()


    def saveNamePopulationData(outputDirectory, outputHistoricalCountFileName):
        wProcessedNameList = {}
        for wYear_Top, wPopulation_Top in gTotalUSPopulation.items():
            print("Saving Data of Year {0}".format(wYear_Top))
            for wName, wCount in wPopulation_Top.NameSet.items():
                if wName in wProcessedNameList:
                    continue
                wHistoricalCount = wProcessedNameList[wName] = {}
                wFilename = outputDirectory + "/" + wName.lower() + ".csv"
                wFileHandler = open(wFilename, 'w')
                if 'w' == wFileHandler.mode:
                    wHistoricalCount["USA"] = 0
                    for wStateName, wStateInfo in gStateInformationDictionary.items():
                        wHistoricalCount[wStateInfo.Abbreviation] = 0

                    wDataLine = ""
                    wDataLine += "{0}".format("Name")
                    wDataLine += ",{0}".format("Year")
                    wDataLine += ",{0}".format("USA")
                    for wStateName, wStateInfo in gStateInformationDictionary.items():
                        wDataLine += ",{0}".format(wStateInfo.Abbreviation)
                    wFileHandler.write("{0}\n".format(wDataLine))

                    for wYear, wPopulation_USA in gTotalUSPopulation.items():
                        wUSANameCount = 0
                        if wName in wPopulation_USA.NameSet:
                            wUSANameCount = wPopulation_USA.NameSet[wName]
                        wHistoricalCount["USA"] += wUSANameCount

                        wDataLine = ""
                        wDataLine += "{0}".format(wName)
                        wDataLine += ",{0}".format(wYear)
                        wDataLine += ",{0}".format(wUSANameCount)
                        for wStateName, wStateInfo in gStateInformationDictionary.items():
                            wNameCountAtYearAtState = 0
                            if wYear in wStateInfo.PopulationTable:
                                wStatPopulationAtYear = wStateInfo.PopulationTable[wYear]
                                if wName in wStatPopulationAtYear.NameSet:
                                    wNameCountAtYearAtState = wStatPopulationAtYear.NameSet[wName]
                            wHistoricalCount[wStateInfo.Abbreviation] += wNameCountAtYearAtState

                            wDataLine += ",{0}".format(wNameCountAtYearAtState)
                        wFileHandler.write("{0}\n".format(wDataLine))
                wFileHandler.close()


        wSortedList = {}
        for wName in sorted(wProcessedNameList.keys()):
            wSortedList[wName] = wProcessedNameList[wName]

        wProcessedNameList = wSortedList

        print("Saving Historical Count Summary File")
        wFileHandler = open(outputHistoricalCountFileName, 'w')
        if 'w' == wFileHandler.mode:
            wDataLine = ""
            wDataLine += "{0}".format("Name")
            wDataLine += ",{0}".format("USA")
            for wStateName, wStateInfo in gStateInformationDictionary.items():
                wDataLine += ",{0}".format(wStateInfo.Abbreviation)
            wFileHandler.write("{0}\n".format(wDataLine))

            for wName, wHistoricalCount in wProcessedNameList.items():
                wDataLine = ""
                wDataLine += "{0}".format(wName)
                wDataLine += ",{0}".format(wHistoricalCount["USA"])
                for wStateName, wStateInfo in gStateInformationDictionary.items():
                    wDataLine += ",{0}".format(wHistoricalCount[wStateInfo.Abbreviation])
                wFileHandler.write("{0}\n".format(wDataLine))
        wFileHandler.close()


