from os import walk
from os import path

# This Class is to parse the data provided into a JSON object

# Class to Record the count of the Name
class NameData:
    # Constructor
    def __init__(self):
        self.MaleCount = 0       # The total number of Males using this name
        self.FemaleCount = 0     # The total number of Females using this name


# Class to record the Population of a given year
class Population:
    # Constructor
    def __init__(self):
        self.Total = 0           # Total number of people
        self.Male = 0            # Total number of Males
        self.Female = 0          # Total number of Females
        self.NameSet = {}        # Dictionary of Names and occurance in the population count: key=Name, value=NameData()


# Class to record the geographical information of a state and it's population information
class StateInformation:
    # Constructor
    def __init__(self, name):
        self.Name = name             # Name of State
        self.Abbreviation = ""       # Abbreviation of State
        self.Latitude = 0.0          # Geographical Latitude of state (degrees)
        self.Longitude = 0.0         # Geographical Longitude of state (degrees)
        self.Area = 0.0              # Geographical Area of state (sq-km)
        self.PopulationTable = {}    # Population Information of state : key=Year, value=Population()


# Master class to Parse Data into object
class NameInfoParser:

    # Constructor
    def __init__(self):
        self.NameList = {}                    # Name List : key = "Name, value = NameData()
        self.TotalUSPopulation = {}           # Total Population Count of USA : key = Year, value = Population()
        self.StateInformationDictionary = {}  # Information of each State : key = State, value = StateInformation()

    # getter for state information dictionary
    def getStateInformationDictionary(self):
        return self.StateInformationDictionary;

    # getter for state information by name
    def getStateInfomationByName(self, name):
        # If state is in state information dictionary
        if name in self.StateInformationDictionary:
            # return instance
            return self.StateInformationDictionary[name]
        # re-tune None if not found
        return None

    # getter for state information by abbreviation
    def getStateInfomationByAbbreviation(self, abbreviation):
        # loop through all available states
        for wName, wState in self.StateInformationDictionary.items():
            # if abbreviation is equal to requested abbreviation
            if abbreviation == self.StateInformationDictionary[wName].Abbreviation:
                # return object if found
                return self.StateInformationDictionary[wName]
        # return null if not found
        return None

    # function to add State name to Dictionary
    def addStateName(self, name):
        # if name is not in Dictionary
        if name not in self.StateInformationDictionary:
            # create new instance
            self.StateInformationDictionary[name] = StateInformation(name)

    # setter for State abbreviation
    def setStateAbbreviation(self, name, abbreviation):
        # add new state name to dictionary
        self.addStateName(name)
        # set object Abbreviation to input argument, abbreviation
        self.StateInformationDictionary[name].Abbreviation = abbreviation

    # setter for state location
    def setStateLocation(self, name, latitude, longitude):
        # add new state name to dictionary
        self.addStateName(name)
        # get reference
        wState = self.StateInformationDictionary[name]
        # set Latitude and Longitude value
        wState.Latitude = latitude
        wState.Longitude = longitude

    # setter for state area
    def setStateArea(self, name, area):
        # add new state name to dictionary
        self.addStateName(name)
        # set object area value
        self.StateInformationDictionary[name].Area = area

    # setter for name list data
    def setNameList(self, name, sex, count):
        # get instance of resporter
        wNameData = self.NameList[name] = NameData()
        # if sex is male
        if "M" == sex:
            # set male count value
            wNameData.MaleCount = count
        # if sex is female
        if "F" == sex:
            # set female count value
            wNameData.FemaleCount = count

    # adding for name list data
    def addToNameList(self, name, sex, count):
        # name is not in list
        if name not in self.NameList:
            # call set population problem
            self.setNameList(name, sex, count)
        # else
        else:
            # get current name from data
            wNameData = self.NameList[name]
            # if sec is male
            if "M" == sex:
                # Add to Male count if Mals
                wNameData.MaleCount += count
            if "F" == sex:
                # Add to Male count if Mals
                wNameData.FemaleCount += count

    # set Total Population
    def setTotalPopulation(self, year, population, malecount, femalecount, name=""):
        if year not in self.TotalUSPopulation:
            self.TotalUSPopulation[year] = Population()
        # get the instance of the object
        wPopulation = self.TotalUSPopulation[year]
        # set wPopulation data
        wPopulation.Total = population
        wPopulation.Male = malecount
        wPopulation.Female = femalecount
        # if not null string
        if "" != name:
            # set Population name set
            wPopulation.NameSet[name] = population

    # Add count to Total Population
    def addToTotalPopulation(self, year, population, malecount, femalecount, name=""):
        # Is year already in TotalUSPopulation
        if year not in self.TotalUSPopulation:
            # if year not found, create new account
            self.TotalUSPopulation[year] = Population()
        # get instance of the opject
        wPopulation = self.TotalUSPopulation[year]
        # add value to existing object
        wPopulation.Total += population
        wPopulation.Male += malecount
        wPopulation.Female += femalecount
        # if not null string
        if "" != name:
            # if name is not in name set
            if name not in wPopulation.NameSet:
                # set name count to 0
                wPopulation.NameSet[name] = 0
            # add population to NameSet
            wPopulation.NameSet[name] += population

    # set State population
    def setStatePopulation(self, statename, year, population, malecount, femalecount, name=""):
        # add new state name to dictionary
        self.addStateName(statename)
        # get state information object
        wState = self.StateInformationDictionary[statename]
        # if requested year is not in the PopulationTable
        if year not in wState.PopulationTable:
            # Add year and assign new Population() object
            wState.PopulationTable[year] = Population()
        # get Population to save in
        wPopulation = wState.PopulationTable[year]
        # Set Population values
        wPopulation.Total = population
        wPopulation.Male = malecount
        wPopulation.Female = femalecount
        # if name is not null
        if "" != name:
            # add population to wPopulation name set
            wPopulation.NameSet[name] = population

    # add requested population to database
    def addStatePopulation(self, statename, year, population, malecount, femalecount, name=""):
        # add new state name to dictionary
        self.addStateName(statename)
        # get state information object
        wState = self.StateInformationDictionary[statename]
        # if requested year is not in the PopulationTable
        if year not in wState.PopulationTable:
            # Add year and assign new Population() object
            wState.PopulationTable[year] = Population()
        # get Population to save in
        wPopulation = wState.PopulationTable[year]
        # Set Population values
        wPopulation.Total += population
        wPopulation.Male += malecount
        wPopulation.Female += femalecount
        # if name is not null
        if "" != name:
            # if name is not in Name Set
            if name not in wPopulation.NameSet:
                # Initiallize name to 0
                wPopulation.NameSet[name] = 0
            # Add requested population
            wPopulation.NameSet[name] += population

    # function to parse Abbreviation CSV
    def parseAbbreviationCSV(self, filename):
        # open provided file in read mode
        wFileHandler = open(filename, 'r')
        # if file is properly open
        if 'r' == wFileHandler.mode:
            # print log
            print("Parsing file : {0}".format(filename))
            # read file lines
            wFileData = wFileHandler.readlines()
            # loop through lines
            for wLine in wFileData:
                # remove the newline character
                wLine = wLine.strip("\n")
                # split words by comma
                wData = wLine.split(",")
                # if Entry list is greater than 4, Abbreviations are on the 4th column
                if 4 <= len(wData):
                    # add abbreviation to the class
                    self.setStateAbbreviation(wData[0], wData[3])
        # close file
        wFileHandler.close()

    # parse function to parse coordinate data
    def parseLocationCSV(self, filename):
        # open provided file in read mode
        wFileHandler = open(filename, 'r')
        # if file is properly open
        if 'r' == wFileHandler.mode:
            # print log
            print("Parsing file : {0}".format(filename))
            # read file lines
            wFileData = wFileHandler.readlines()
            # loop through lines
            for wLine in wFileData:
                # remove the newline character
                wLine = wLine.strip("\n")
                # split words by comma
                wData = wLine.split(",")
                # check word list size
                if 3 <= len(wData):
                    # Add coordinate location to the class
                    self.setStateLocation(wData[0], float(wData[1]), float(wData[2]))
        # close file
        wFileHandler.close()

    # parse function to parse area data
    def parseAreaCSV(self, filename):
        # open provided file in read mode
        wFileHandler = open(filename, 'r')
        # if file is properly open
        if 'r' == wFileHandler.mode:
            # print log
            print("Parsing file : {0}".format(filename))
            # read file lines
            wFileData = wFileHandler.readlines()
            # loop through lines
            for wLine in wFileData:
                # remove the newline character
                wLine = wLine.strip("\n")
                # split words by comma
                wData = wLine.split(",")
                # check word list size
                if 4 <= len(wData):
                    # Add coordinate area to the class
                    self.setStateArea(wData[0], float(wData[3]))
        # close file
        wFileHandler.close()

    # purge missing state information, minimum requirement is to have a state abbreviation
    def purgeMissingAbbreviation(self):
        # new container to store elements to delete
        wListToDelete=[]
        # loop through state information dictionary
        for wName, wState in self.StateInformationDictionary.items():
            # if the Abbreviation is not set
            if "" == wState.Abbreviation:
                # add name to list to delete
                wListToDelete.append(wName)
        # loop through list of items to delete
        for wName in wListToDelete:
            # delete the list from dictionary
            self.StateInformationDictionary.pop(wName)

    # extract the provided database.
    def extractPopulationTable(self, inputDirectory):
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
        # loop through file list
        for wFilename in wFileList:
            # open file in read mode
            wFileHandler = open(wFilename, 'r')
            # initialize wStat info reference
            wState = None
            # if file is open properly
            if 'r' == wFileHandler.mode:
                # log  message
                print("Parsing file : {0}".format(wFilename))
                # read file lines
                wFileData = wFileHandler.readlines()
                # loop through lines
                for wLine in wFileData:
                    # remove newline character
                    wLine = wLine.strip("\n")
                    # split string into word array
                    wData = wLine.split(",")
                    # check length of array
                    if 4 <= len(wData):
                        # if state was not previously found
                        if None == wState:
                            # get new state information
                            wState = self.getStateInfomationByAbbreviation(wData[0])
                        # if privouse state's abbriviation is not equal to line abbreviation
                        elif wState.Abbreviation != wData[0]:
                            # get new state information
                            wState = self.getStateInfomationByAbbreviation(wData[0])
                        # if wState is defined
                        if None != wState:
                            # Count the number of Male in the current data entry
                            wMaleCount = 0
                            if "M" == wData[1]:
                                wMaleCount = int(wData[4])
                            # Count the number of Female in the current data entry
                            wFemaleCount = 0
                            if "F" == wData[1]:
                                wFemaleCount = int(wData[4])
                            # add data to class
                            self.addStatePopulation(wState.Name, int(wData[2]), int(wData[4]), wMaleCount, wFemaleCount, wData[3])
                            self.addToTotalPopulation( int(wData[2]), int(wData[4]), wMaleCount, wFemaleCount,  wData[3])
                            self.addToNameList(wData[3], wData[1], int(wData[4]))
                # close file
                wFileHandler.close()

    # this function saves the  name list
    def saveNameList(self, outputfilename):
        print("Saving Name List")
        # open provided file in write mode
        wFileHandler = open(outputfilename, 'w')
        # if file is in write mode
        if 'w' == wFileHandler.mode:
            # Enter Header in first file line
            wDataLine = ""
            wDataLine += "{0}".format("Name")
            wDataLine += ",{0}".format("Sex")
            wDataLine += ",{0}".format("Count")
            wDataLine += ",{0}".format("MaleCount")
            wDataLine += ",{0}".format("FemaleCount")
            wFileHandler.write("{0}\n".format(wDataLine))
            # Loop through sorted name list
            for wName in sorted(self.NameList.keys()):
                # get Name count refence
                wData = self.NameList[wName]
                # start write data into csv
                wDataLine = ""
                # write Name
                wDataLine += "{0}".format(wName)
                # write gender
                # if Male count is 0
                if 0 == wData.MaleCount:
                    # Name is a female name
                    wDataLine += ",{0}".format("F")
                else:
                    # get the ratio of female to male using the name
                    wTest = wData.FemaleCount/wData.MaleCount;
                    # if the ratio is within the middle 40%
                    if (wTest > 0.3) & (wTest < 0.7):
                        # the name is consider a unisex name
                        wDataLine += ",{0}".format("U")
                    # if ratio is in the lesser 50%
                    elif wTest < 0.5:
                        # the name is a conseder a male name
                        wDataLine += ",{0}".format("M")
                    # the name is in the higher 50%
                    else:
                        # the name is consder a female name
                        wDataLine += ",{0}".format("F")
                # add total count to csv
                wDataLine += ",{0}".format(wData.MaleCount+wData.FemaleCount)
                # add male count to csv
                wDataLine += ",{0}".format(wData.MaleCount)
                # add female count to csv
                wDataLine += ",{0}".format(wData.FemaleCount)
                # write line value
                wFileHandler.write("{0}\n".format(wDataLine))
        # close file
        wFileHandler.close()
    
    # save summarized state geographic data
    def saveSummarizedStateGeographyDataData(self, outputfilename):
        # print log message
        print("Saving USA state geography data")
        # open file for writing mode
        wFileHandler = open(outputfilename, 'w')
        # if file is properly open
        if 'w' == wFileHandler.mode:
            # Enter Header in first file line
            wDataLine = ""
            wDataLine += "{0}".format("State")
            wDataLine += ",{0}".format("Abbreviation")
            wDataLine += ",{0}".format("Latitude_deg")
            wDataLine += ",{0}".format("Longitude_deg")
            wDataLine += ",{0}".format("Area_sq-Km")
            wFileHandler.write("{0}\n".format(wDataLine))
            # loop through state info object
            for wName, wState in self.StateInformationDictionary.items():
                wDataLine = ""
                # name of the state
                wDataLine += "{0}".format(wState.Name)
                # abbreviation of the state
                wDataLine += ",{0}".format(wState.Abbreviation)
                # latitude of the state
                wDataLine += ",{0}".format(wState.Latitude)
                # longitude of the state
                wDataLine += ",{0}".format(wState.Longitude)
                # area of the state
                wDataLine += ",{0}".format(wState.Area)
                # Write Data into file
                wFileHandler.write("{0}\n".format(wDataLine))
        # close file
        wFileHandler.close()

    # save state population data
    def saveStatePopulationData(self, outputDirectory, outputUSAPopulationFileName):
        # loop thorugh all state objects in dictionary
        for wName, wState in self.StateInformationDictionary.items():
            # Print Log
            print("Saving State population summary of {0}".format(wName))
            # get new file name  {state_abbreviation}.csv
            wFilename = outputDirectory + "/" + wState.Abbreviation + ".csv"
            # open the file in write mode
            wFileHandler = open(wFilename, 'w')
            # if file is open properly
            if 'w' == wFileHandler.mode:
                # print header
                wDataLine = ""
                wDataLine += "{0}".format("state")
                wDataLine += ",{0}".format("year")
                wDataLine += ",{0}".format("totalPopulation")
                wDataLine += ",{0}".format("malePopulation")
                wDataLine += ",{0}".format("femalePopulation")
                wDataLine += ",{0}".format("uniqueNames")
                wFileHandler.write("{0}\n".format(wDataLine))
                # loop through population table
                for wYear, wPopulation in wState.PopulationTable.items():
                    wDataLine = ""
                    # record the state abbreviation
                    wDataLine += "{0}".format(wState.Abbreviation)
                    # record the year
                    wDataLine += ",{0}".format(wYear)
                    # Total population with that name during the year
                    wDataLine += ",{0}".format(wPopulation.Total)
                    # Male population with that name during the year
                    wDataLine += ",{0}".format(wPopulation.Male)
                    # Female population with that name during the year
                    wDataLine += ",{0}".format(wPopulation.Female)
                    # Print the number of unique names that year
                    wDataLine += ",{0}".format(len(wPopulation.NameSet))
                    # save data to file
                    wFileHandler.write("{0}\n".format(wDataLine))
            # close file
            wFileHandler.close()

        # Print Log
        print("Saving USA population summary")
        # open requested file path for writing
        wFileHandler = open(outputUSAPopulationFileName, 'w')
        # if file is proper opened
        if 'w' == wFileHandler.mode:
            wDataLine = ""
            wDataLine += "{0}".format("state")
            wDataLine += ",{0}".format("year")
            wDataLine += ",{0}".format("totalPopulation")
            wDataLine += ",{0}".format("malePopulation")
            wDataLine += ",{0}".format("femalePopulation")
            wDataLine += ",{0}".format("uniqueNames")
            wFileHandler.write("{0}\n".format(wDataLine))
            # loop through population table
            for wYear, wPopulation in self.TotalUSPopulation.items():
                wDataLine = ""
                # record the state abbreviation
                wDataLine += "{0}".format("USA")
                # record the year
                wDataLine += ",{0}".format(wYear)
                # Male population with that name during the year
                wDataLine += ",{0}".format(wPopulation.Total)
                # Female population with that name during the year
                wDataLine += ",{0}".format(wPopulation.Male)
                # Female population with that name during the year
                wDataLine += ",{0}".format(wPopulation.Female)
                # Print the number of unique names that year
                wDataLine += ",{0}".format(len(wPopulation.NameSet))
                 # save data to file
                wFileHandler.write("{0}\n".format(wDataLine))
        # close file
        wFileHandler.close()

    # save individual name population data
    def saveNamePopulationData(self, outputDirectory, outputHistoricalCountFileName):
        # List of names that have already processed
        wProcessedNameList = {}
        # Loop though total use population history to get the names required to process
        for wYear_Top, wPopulation_Top in self.TotalUSPopulation.items():
            # Log year to process
            print("Saving Data of Year {0}".format(wYear_Top))
            # Loop through the names in the current year population
            for wName, wCount in wPopulation_Top.NameSet.items():
                # if name is already processed
                if wName in wProcessedNameList:
                    # skip current name
                    continue
                # create wProcessedName List entry and save reference
                wHistoricalCount = wProcessedNameList[wName] = {}
                # Create file name with the current entry name
                wFilename = outputDirectory + "/" + wName.lower() + ".csv"
                # Open file for the name in write mode
                wFileHandler = open(wFilename, 'w')
                # if file opened successfully
                if 'w' == wFileHandler.mode:
                    # set Historical count of "USA" is set to 0;
                    wHistoricalCount["USA"] = 0
                    # loop through all states
                    for wStateName, wStateInfo in self.StateInformationDictionary.items():
                        # Initialize all initial value to 0
                        wHistoricalCount[wStateInfo.Abbreviation] = 0

                    # Save file header
                    wDataLine = ""
                    wDataLine += "{0}".format("Name")
                    wDataLine += ",{0}".format("Year")
                    wDataLine += ",{0}".format("USA")
                    # for every state
                    for wStateName, wStateInfo in self.StateInformationDictionary.items():
                        # print the state abbreviation as header
                        wDataLine += ",{0}".format(wStateInfo.Abbreviation)
                    # save header
                    wFileHandler.write("{0}\n".format(wDataLine))

                    # Loop through TotalUSPopulation to know which year to use
                    for wYear, wPopulation_USA in self.TotalUSPopulation.items():
                        # initialize US count to 0
                        wUSANameCount = 0
                        # if the name is in the current population NameSet
                        if wName in wPopulation_USA.NameSet:
                            # record actual name count
                            wUSANameCount = wPopulation_USA.NameSet[wName]
                        # add data to HistoricalCount Data
                        wHistoricalCount["USA"] += wUSANameCount

                        # Start printing data into CSV
                        wDataLine = ""
                        # The current working name
                        wDataLine += "{0}".format(wName)
                        # The year the data is captured from
                        wDataLine += ",{0}".format(wYear)
                        # The overall US population with the name
                        wDataLine += ",{0}".format(wUSANameCount)
                        # Loop though all the states
                        for wStateName, wStateInfo in self.StateInformationDictionary.items():
                            # Initialize state count to 0
                            wNameCountAtYearAtState = 0
                            # if year is in the current population table
                            if wYear in wStateInfo.PopulationTable:
                                # Get State population object of the year
                                wStatPopulationAtYear = wStateInfo.PopulationTable[wYear]
                                # if the Name is in the NameSet of the year
                                if wName in wStatPopulationAtYear.NameSet:
                                    # save the current count of the name in the state
                                    wNameCountAtYearAtState = wStatPopulationAtYear.NameSet[wName]
                            # Add the current state count to HistoricalCount
                            wHistoricalCount[wStateInfo.Abbreviation] += wNameCountAtYearAtState
                            # The Count of the Name for the specified state at the specified year
                            wDataLine += ",{0}".format(wNameCountAtYearAtState)
                        # Save data to file
                        wFileHandler.write("{0}\n".format(wDataLine))
                # close file
                wFileHandler.close()

        # Sort the process name list in alphabetical order
        wSortedList = {}
        for wName in sorted(wProcessedNameList.keys()):
            wSortedList[wName] = wProcessedNameList[wName]
        wProcessedNameList = wSortedList

        # print log
        print("Saving Historical Count Summary File")
        # open filename to save historical name count data in wirte mode
        wFileHandler = open(outputHistoricalCountFileName, 'w')
        # if the file is open correctly
        if 'w' == wFileHandler.mode:
            # Added the associated headers
            wDataLine = ""
            # Current working name
            wDataLine += "{0}".format("Name")
            # The USA Gran total column
            wDataLine += ",{0}".format("USA")
            # All state Abbreviation
            for wStateName, wStateInfo in gStateInformationDictionary.items():
                wDataLine += ",{0}".format(wStateInfo.Abbreviation)
            # Save data to file
            wFileHandler.write("{0}\n".format(wDataLine))

            # loop through wProccedNameList
            for wName, wHistoricalCount in wProcessedNameList.items():
                wDataLine = ""
                # print current name
                wDataLine += "{0}".format(wName)
                # print USA historical count
                wDataLine += ",{0}".format(wHistoricalCount["USA"])
                # print state historical count
                for wStateName, wStateInfo in gStateInformationDictionary.items():
                    wDataLine += ",{0}".format(wHistoricalCount[wStateInfo.Abbreviation])
                # save data to file
                wFileHandler.write("{0}\n".format(wDataLine))
        # close file
        wFileHandler.close()


