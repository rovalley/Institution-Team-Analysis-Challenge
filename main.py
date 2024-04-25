institutions = dict()

with open ("2015.csv", "r") as readFile:
    lines = readFile.readlines()
    for i in range(1,len(lines)):
        line = lines[i].strip()
        while '"' in line:
            firstQuote = line.index('"')
            secondQuote = line[firstQuote + 1:].index('"') + firstQuote + 1
            line = line[:firstQuote] + line[firstQuote + 1:secondQuote].replace(",","") + line[secondQuote + 1:]
        lineData = line.split(",")
        institutionName = lineData[0]
        city = lineData[2]
        stateProv = lineData[3]
        country = lineData[4]
        institution = (institutionName, city, stateProv, country)
        if institution not in institutions:
            institutions[institution] = list()
        teamNumber = lineData[2]
        advisor = lineData[5]
        problem = lineData[6]
        ranking = lineData[7]
        team = (teamNumber, advisor, problem, ranking)
        institutions[institution].append(team)

numberOfInstitutions = len(institutions)
numberOfTeams = 0
for institution in institutions:
    teamsList = institutions[institution]
    numberOfTeams += len(teamsList)
avgNumTeams = numberOfTeams / numberOfInstitutions
with open ("AverageNumberOfTeams.txt", "w") as file:
    file.write(str(avgNumTeams))
    file.write("\n")

listOfInstitutionsOrderedByNumTeams = list()
for institution in institutions:
    institutionName = institution[0]
    teamsList = institutions[institution]
    listOfInstitutionsOrderedByNumTeams.append((len(teamsList), institutionName))
listOfInstitutionsOrderedByNumTeams.sort(reverse=True)
with open("ListOfInstitutionsOrderedByNumTeams.txt", "w") as file:

    for institution in listOfInstitutionsOrderedByNumTeams:
        file.write(institution[1])
        file.write(",")
        file.write(str(institution[0]))
        file.write("\n")


listOfOutstandingInstitutions = list()
for institution in institutions:
    institutionName = institution[0]
    teamsList = institutions[institution]
    for team in teamsList:
        ranking = team[3]
        if ranking == "Outstanding Winner":
            if institutionName not in listOfOutstandingInstitutions:
                listOfOutstandingInstitutions.append(institutionName)

listOfOutstandingInstitutions.sort()
with open("ListOfOutstandingInstitutions.txt", "w") as file:
    for institutionName in listOfOutstandingInstitutions:
        file.write(institutionName)
        file.write("\n")

listOfMeritoriousUSATeams = list()
for institution in institutions:
    country = institution[3]
    if country == "USA":
        teamsList = institutions[institution]
        for team in teamsList:
            ranking = team[3]
            if ranking == "Meritorious" or ranking == "Finalist" or ranking =="Outstanding Winner":
                institutionName = institution[0]
                if institutionName not in listOfMeritoriousUSATeams:
                    listOfMeritoriousUSATeams.append(institutionName)
with open("MeritoriousUSATeams.txt", "w") as file:
    for institutionName in listOfMeritoriousUSATeams:
        file.write(institutionName)
        file.write("\n")
