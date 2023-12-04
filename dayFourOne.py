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
        if score == 0:
            score = 1
        else:
            score = score * 2
    return score
        
# Using readlines()
file1 = open('dayFour.txt', 'r')
Lines = file1.readlines()
 
total = 0
for line in Lines:
    total += cardScore(line)

print(total)
