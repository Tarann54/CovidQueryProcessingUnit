# File: Project3.py
# Student: Taran Nudurumati
# UT EID: tn8369
# Course Name: CS303E
# 
# Date Created: 5/1/21
# Date Last Modified: 5/2/21
# Description of Program: This program takes in the covid data file and creates
#a search query that provides data on cases and deaths based on user input for
# a certain county or for all of Texas. 

import os.path


class CovidData():
    def __init__(self):
        self.totalConfirmedCases = 0
        self.totalConfirmedDeaths = 0
        self.countyNames = []
        self.dictionary = {}
    
    def getCounties(self):
        return self.countyNames
    """            countiesString = ", "
            countiesString.join(self.countyNames)"""
        
    
    def getCountyCases(self, countyName):
        if countyName.lower().title() not in self.countyNames:
            return "oopsy"
        else:
            return (countyName.lower().title(), self.dictionary[countyName.title().strip()][0]) 
    
    def getCountyDeaths(self, countyName):
        return (countyName.lower().title(), self.dictionary[countyName.title().strip()][1])
    
    def getTexasCases(self):
        return self.totalConfirmedCases
    
    def getTexasDeaths(self):
        return self.totalConfirmedDeaths
    
    def initialize(self):
        
        dataFile = open("county-covid-data.txt", "r")
        #line = dataFile.readline().split(",")# to skip the heading line in the census file
    
        line = dataFile.readline().split(",")
        line[-1] = line[-1].strip()
    
        while line:
            if "#" in line[0]: #skip lines that start with #
                line = dataFile.readline().split(",")
                line[-1] = line[-1].strip()
                continue
            if line == [""]:
                break
            self.totalConfirmedCases += int(line[1])
            self.totalConfirmedDeaths += int(line[-1])
            self.countyNames.append(line[0])
        
            self.dictionary[line[0]] = (int(line[1]), int(line[-1]))
            line = dataFile.readline().split(",") #go to next line in file
            line[-1] = line[-1].strip()
        self.dictionary["Texas"] = (self.totalConfirmedCases, self.totalConfirmedDeaths)    
        #print(dictionary)
        #return (self.dictionary, self.countyNames)
        dataFile.close()

def printHelp():
    print("Enter any of the following commands: \
                     \nHelp - list available commands; \
                     \nQuit - exit this dashboard; \
                     \nCounties - list all Texas counties; \
                     \nCases <countyName>/Texas - confirmed Covid cases in specified county or statewide; \
                     \nDeaths <countyName>/Texas - Covid deaths in specified county or statewide.")
    return 

def getCommand():
    commandInput = input("Please enter a command: ")
    return commandInput

def main(): #the Query Processing Functionality itself
    data = CovidData()
    data.initialize()
    if not os.path.isfile("county-covid-data.txt"): #checking if file exists in same directory as this python file
        print("File county-covid-data.txt not found")
        return
    print()
    print("Welcome to the Texas Covid Database Dashboard.")
    print("This provides Covid data in Texas as of 1/26/21.")
    print("Creating dictionary from file: county-covid-data.txt \n")
    commandInput = printHelp()

    
    while True:
        commandInput = getCommand()
        if commandInput == "":
            continue
        # Parse the command into a list of words (assuming there's no punctuation).
        commWords = commandInput.split()
        # Extract the first word in the command (which is always a one-word command):
        comm = commWords[0]
        # Extract the rest of the words and re-assemble them into a single string, 
        # separated by spaces. 
        args = commWords[1:]
        arg = " ".join(args)

        if comm.lower() == "help":
            commandInput = printHelp()
        elif comm.lower() == "counties":
            output = data.getCounties()
            for i in range(len(output)):
                if i%10 == 0:
                    print("\r")
                print(output[i], end = ", ")
            print()
        elif comm.lower() == "cases":
            if str(arg).lower() == "texas":
                output = data.getTexasCases()
                print("Texas total confirmed Covid cases:", output)
            elif str(arg).lower() != "texas":
                output = data.getCountyCases(str(arg))
                if output != "oopsy":
                    print(output[0], "county has", output[1], "confirmed Covid cases.")
                else:
                    print("County", str(arg), "is not recognized.")
            else:
                print(output[0], "county has", output[1], "confirmed Covid cases.")
        elif comm.lower() == "deaths":
            if str(arg).lower() == "texas":
                output = data.getTexasDeaths()
                print("Texas total confirmed Covid deaths:", output)
            elif str(arg).lower() != "texas":
                output = data.getCountyDeaths(str(arg))
                if output != "oopsy":
                    print(output[0], "county has", output[1], "fatalaties.")
                else:
                    print("County", str(arg), "is not recognized.")
            
        elif comm.lower() == "quit":
            print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!")
            break
        else:
            print("Command is not recognized.  Try again!")
        
    
main()