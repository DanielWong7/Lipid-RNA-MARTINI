## Meant to create an gromacs ndx file for specific beads ##

## Edit these parameters to control how the new ndx file is made
fileName = "System_md.gro"
ndxName = "chargedBeadsIndex.ndx"
startLine = 3
endLine = 1000
groupNames = ["charged_lipid", "chargedRNA"]
targetBeads = ["CRG", "BB1"]
foundBeads = [[],[]]

## Get to start line
print("Scanning gro file...")
file = open(fileName,"r")
for i in range(1,startLine):
    file.readline()

## Parse lines and add coordinate number to index list if it is a target bead
for i in range(startLine,endLine+1):
    line = file.readline().split()
    for j in range(len(targetBeads)):
        if line[1] == targetBeads[j]:
            foundBeads[j].append(line[2])           
file.close()
print("Completed scan")
for i in range(len(foundBeads)):
    print("Found " + str(len(foundBeads[i])) + " " + targetBeads[i] + " beads")

## Write new ndx file
print("Writing ndx file...")
file = open(ndxName,"w")
for i in range(len(groupNames)):
    file.write("[ " + groupNames[i] + " ]\n")
    for j in range(len(foundBeads[i])):
        file.write(foundBeads[i][j] + " ")
        if (j+1)%15==0:
            file.write("\n")
    file.write("\n")
file.close()
print("Completed writing ndx file")
