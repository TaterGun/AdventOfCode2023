#file1 = open('dayThreeTest.txt', 'r')
file1 = open('dayThree.txt', 'r')
lines = file1.readlines()
total = 0


nullS = [".","\n"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
symbs = []
for x in lines:
    for y in x:
        if not y in nullS and not y in digits and not y in symbs:
            symbs.append(y)

print(symbs)

valList = []
dictCoords = {}
## each coordinate has a value
## {(1,2): 323} (not a real value here)
x = 0
y = 0
tempStr = ""
cList = []
head = (-1,-1)
for line in lines:
    x = 0
    y = y + 1
    tempStr = ""
    cList = []
    for char in line:
        x = x + 1
        if char in digits:
            if head == (-1,-1):
                head = (x,y)
            cList.append((x,y))
            tempStr = tempStr + char
        else:
            if tempStr != "":
                val = int(tempStr)
                #print(val)
                valList.append(val)
                for xy in cList:
                    dictCoords[(xy[0],xy[1])] = (val,head)
                tempStr = ""
                cList = []
            head = (-1,-1)
partNumsUsed = []
totalGearRations = []
tempGearRations = []
def addNumFromCoordValue(x,y):
    xy = (x,y)
    #print(dictCoords.keys())
    #print(xy)
    if xy in dictCoords.keys():
        #print(dictCoords[xy])
        if not dictCoords[xy] in tempGearRations:
            tempGearRations.append(dictCoords[xy])
            
x = 0
y = 0            
for line in lines:
    x = 0
    y = y + 1
    for char in line:
        x = x + 1
        if char == "*":
            ## check ball around symbol
            tempGearRations = []
            addNumFromCoordValue(x - 1, y - 1)        
            addNumFromCoordValue(x - 1, y)
            addNumFromCoordValue(x - 1, y + 1)
            addNumFromCoordValue(x, y - 1)
            ## (x, y) ## do not bother
            addNumFromCoordValue(x, y + 1)
            addNumFromCoordValue(x + 1, y - 1)
            addNumFromCoordValue(x + 1, y)
            addNumFromCoordValue(x + 1, y + 1)
            if len(tempGearRations) == 2:
                totalGearRations.append(tempGearRations[0][0] * tempGearRations[1][0])

print(partNumsUsed)
total = 0
for n in totalGearRations:
    total += n
print(total)

