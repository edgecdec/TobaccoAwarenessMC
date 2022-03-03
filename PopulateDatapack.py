from Team import Team
from CreateHelmetsFunction import createHelmetsFunction
import csv
import os
import zipfile

basePath = 'APICAT/data/apicat/functions/team_setup/'
callPath = 'apicat:team_setup/'

def zipDir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

teams = []

teamLeaders = []

#Read the team leaders from file and put them in list to be used later
with open("TeamLeaders.txt", "r") as infile:
    for line in infile.readlines():
        teamLeaders.append(line.replace('\n', ''))

# print(teamLeaders)


teamDataDict = csv.DictReader(open("TeamData.csv"))

#Create Team Objects for ease
i = 0
for teamData in teamDataDict:
    teams.append(Team(teamData['Team Color Name'], teamData['Hex Code'], teamData['Block'], teamData['Team Number'], teamLeaders[i]))
    i += 1

# Create Teams and add leader to them
with open(f"{basePath}create_teams.mcfunction", "w") as outfile:
    for team in teams:
        curTeamNum = team.getNumber()
        outfile.write(f'#Create Team {curTeamNum} and add leader\n')
        outfile.write(f'team add team{curTeamNum} "Team {curTeamNum}"\n')
        outfile.write(f'team modify team{curTeamNum} color {team.getTeamColorName()}\n')
        outfile.write(f'team join team{curTeamNum} {team.getLeader()}\n\n')

# with open("TeamData.csv", "w") as outfile:
#     outfile.write(f"Team Number,Team Color Name,Hex Code,Block\n")
#     for team in teams:
#         outfile.write(f"{team.number},{team.teamColorName},{team.hexCode},{team.block}\n")

# Create Team Helmets
createHelmetsFunction(teams, f"{basePath}put_helmets_on.mcfunction")

#Turn whole datapack into .zip file
zipf = zipfile.ZipFile('APICAT.zip', 'w', zipfile.ZIP_DEFLATED)
zipDir('APICAT/', zipf)
zipf.close()