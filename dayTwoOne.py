def possible(red, green, blue):
    if red > 12:
        return False
    if green > 13:
        return False
    if blue > 14:
        return False
    return True

def game(line):
    gameLine = line.split(":")
##    print(gameLine)
    ## [Game 1, 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green] 
    gameNumber = gameLine[0].replace("Game ","")
##    print(gameNumber)
    ## 1
    sets = gameLine[1].split(";")
##    print(sets)
    ## [3 blue, 4 red][1 red, 2 green, 6 blue][ 2 green]
    for set in sets:
        colors = set.split(",")
##        print(colors)
        ## [3 blue][4 red]
        red = 0
        green = 0
        blue = 0
        for color in colors:
##            print(color)
            pair = color.strip().split(" ")
##            print(pair)
            if pair[1] == "red":
##                print("red " + pair[0])
                red += int(pair[0])                
            if pair[1] == "green":
##                print("green " + pair[0])
                green += int(pair[0])
            if pair[1] == "blue":
##                print("blue " + pair[0])
                blue += int(pair[0])

        if not possible(red, green, blue):
            return 0
    return int(gameNumber)
        
# Using readlines()
file1 = open('dayTwo.txt', 'r')
Lines = file1.readlines()
 
total = 0
for line in Lines:
    print(line)
    g = game(line)
    print(g)
    total += game(line)
##test = "Game 98: 18 green, 16 red, 1 blue; 3 red, 2 blue, 20 green; 1 blue, 20 green, 14 red; 14 red, 2 green"
##game(test)
##4241 is too high
