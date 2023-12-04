class ValueMap(object):   
    def __init__(self, value, mappedObjects, nullValue = 0):
        self.value = value
        self.objects = mappedObjects
        self.nullValue = nullValue
    def myValue(self, mappedObject):
        if mappedObject in self.objects:
            return self.value
        else:
            return self.nullValue

def ValueInString(searchString, values):
    ## Iterates through values and returns the first iteration fround in the string
    for i in range(len(values)):
        if values[i] in searchString:
            return values[i]
    return ""

class AdventSearch:

    def SearchFromFront(searchString, values):
        tempString = ""
        for c in searchString:
            tempString = tempString + c
            val = ValueInString(tempString, values)
            if val != "":
                return val
        return ""

    def backwards(line):
        return line[::-1]      
            
    def SearchFromEnd(searchString, values):
        tempString = ""
        for c in AdventSearch.backwards(searchString):
            tempString = c + tempString
            val = ValueInString(tempString, values)
            if val != "":
                return val
        return ""
