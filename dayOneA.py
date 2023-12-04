from AdventMod import AdventSearch, ValueMap
## 54418

class Trebuchet():
    def __init__(self):
        self.digits = ["1","2","3","4","5","6","7","8","9"]
        self.words = ["one","two","three","four","five","six","seven","eight","nine"]
        self.allObjects = []
        for x in self.digits:
            self.allObjects.append(x)
        for x in self.words:
            self.allObjects.append(x)
        self.valueMapping = []
        for x in range(len(self.digits)):
            v = ValueMap(x + 1, [self.digits[x],self.words[x]])
            self.valueMapping.append(v)
                     
    def lineValue(self, line):             
        firstDigit = "-1"
        lastDigit = "-1"

        firstObject = AdventSearch.SearchFromFront(line, self.allObjects)
        print(firstObject)
        for x in self.valueMapping:
            val = x.myValue(firstObject)
            if val != 0:
                firstDigit = str(val)
                break

        secondObject = AdventSearch.SearchFromEnd(line, self.allObjects)
        print(secondObject)
        for x in self.valueMapping:
            val = x.myValue(secondObject)
            if val != 0:
                lastDigit = str(val)
                break
                    
        full = firstDigit + lastDigit
        return int(full)
        

T = Trebuchet()
file1 = open('dayOne.txt', 'r')
lines = file1.readlines()
total = 0
for x in lines:
    print(x)
    val = T.lineValue(x)
##    print(x + " , " + str(val))
    total = total + val
print(total)
## 54418
