def cardScore(line):
    numbers = line.split(":")[1]
    myNums = numbers.split("|")[0]
    winNums = numbers.split("|")[1]
    def trimSplit(nums):
        stripped = []
        for x in nums.split(" "):
            if x != "":
                stripped.append(x.strip())
        return stripped
        
    myNums = trimSplit(myNums)
    winNums = trimSplit(winNums)

    score = 0
    myWinNums = []
    for x in myNums:
        for y in winNums:
            if x == y:
                myWinNums.append(x)
    for x in myWinNums:
        score += 1
    #print(score)
    return score
        
# Using readlines()
file1 = open('dayFour.txt', 'r')
Lines = file1.readlines()


dictLineScore = {} 
totalInitCards = 0
for line in Lines:
    #print(line)
    lineId = int(line.split(":")[0].replace("Card","").strip())
    score = cardScore(line)
    dictLineScore[lineId] = [1,score]
    totalInitCards += 1

winningCards = dictLineScore.keys()

for x in range(1, totalInitCards + 1):
    #print(x)
    if x in winningCards:
        instances = dictLineScore[x][0]
        score = dictLineScore[x][1]
        for y in range(x + 1, x + score + 1):
            dictLineScore[y][0] = dictLineScore[y][0] + instances

total = 0
for x in range(1, totalInitCards + 1):
    total += dictLineScore[x][0]

print(total)   
