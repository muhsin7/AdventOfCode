DEBUG = False

def findGuard(puzzleinput):
    guardPosition = None
    for i in range(len(puzzleinput)):
        for j in range(len(puzzleinput[i])):
            if puzzleinput[i][j] == "^":
                guardPosition = (i, j)
                break
        if guardPosition:
            break
    return guardPosition

rightTurn = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N"
}    

deltas = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1)
}

def nextPos(posX, posY, direction):
    delta = deltas[direction]
    return (posX+delta[0], posY+delta[1])

def solution(puzzleinputlines):
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    if DEBUG:
        printmap(puzzleinputlines, n, m)
    guardPosition = findGuard(puzzleinputlines)
    guardDirection = "N"
    outOfBounds = False
    visited = {guardPosition}
    guardX, guardY = guardPosition
    while not outOfBounds:
        aheadOfGuard = nextPos(guardX, guardY, guardDirection)
        if 0 > aheadOfGuard[0] or 0 > aheadOfGuard[1] or aheadOfGuard[0] >= n or aheadOfGuard[1] >= m:
            outOfBounds = True
            continue
        if puzzleinputlines[aheadOfGuard[0]][aheadOfGuard[1]] == "#":
            guardDirection = rightTurn[guardDirection]
            continue

        # Move forward
        guardX, guardY = aheadOfGuard
        visited.add(aheadOfGuard)
    
    if DEBUG: printmap(puzzleinputlines, n, m, visited)
    print(f"The guard visited {len(visited)} distinct positions")           

def printmap(puzzleinputlines, n, m, visited=set()):
    debugmap = []
    for i in range(n):
        maprow = ""
        for j in range(m):
            if (i, j) in visited:
                maprow += "X"
            else:
                maprow += puzzleinputlines[i][j]
        debugmap.append(maprow)
    print("\n".join(debugmap))

def solutionpart2(puzzleinputlines):
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    originalGuardPosition = findGuard(puzzleinputlines)
    originalGuardDirection = "N"
    loopingObstacles = 0

    maxPermittedOverlaps = sum(s.count('.') for s in puzzleinputlines)
    for innerI in range(n):
        for innerJ in range(m):
            permittedOverlaps = maxPermittedOverlaps
            guardPosition, guardDirection = originalGuardPosition, originalGuardDirection
            if puzzleinputlines[innerI][innerJ] != "#" and puzzleinputlines[innerI][innerJ] != "^":
                puzzlemap = puzzleinputlines.copy()
                puzzlemap[innerI] = "".join(["O" if p==innerJ else puzzlemap[innerI][p] for p in range(len(puzzlemap[innerI]))])
                if DEBUG:
                    printmap(puzzlemap, n, m)
                outOfBounds = False
                visited = {guardPosition}
                guardX, guardY = guardPosition
                while not outOfBounds:
                    aheadOfGuard = nextPos(guardX, guardY, guardDirection)
                    if 0 > aheadOfGuard[0] or 0 > aheadOfGuard[1] or aheadOfGuard[0] >= n or aheadOfGuard[1] >= m:
                        outOfBounds = True
                        continue
                    if puzzlemap[aheadOfGuard[0]][aheadOfGuard[1]] == "#" or puzzlemap[aheadOfGuard[0]][aheadOfGuard[1]] == "O":
                        guardDirection = rightTurn[guardDirection]
                        continue
                    if aheadOfGuard in visited:
                        permittedOverlaps -= 1
                        if DEBUG: print(f"Overlapping, {permittedOverlaps} remaining")
                        if permittedOverlaps <= 0:
                            loopingObstacles += 1
                            break
                    # Move forward
                    guardX, guardY = aheadOfGuard
                    visited.add(aheadOfGuard)
                
                if DEBUG: printmap(puzzlemap, n, m, visited)
    
    print(f"There are {loopingObstacles} possible positions you can choose") 
       
def solutionpart2optimised(puzzleinputlines):
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    ogGuardX, ogGuardY = findGuard(puzzleinputlines)
    originalGuardDirection = "N"
    
    loopingObstacles = 0
    for innerI in range(n):
        for innerJ in range(m):
            gX, gY, guardDirection = ogGuardX, ogGuardY, originalGuardDirection
            if puzzleinputlines[innerI][innerJ] != "#" and puzzleinputlines[innerI][innerJ] != "^":
                puzzlemap = puzzleinputlines.copy()
                puzzlemap[innerI] = "".join(["O" if p==innerJ else puzzlemap[innerI][p] for p in range(len(puzzlemap[innerI]))])
                if DEBUG:
                    printmap(puzzlemap, n, m)
                outOfBounds = False
                visited = {(gX, gY, guardDirection)}
                guardX, guardY = gX, gY
                while not outOfBounds:
                    aheadOfGuard = nextPos(guardX, guardY, guardDirection)
                    if 0 > aheadOfGuard[0] or 0 > aheadOfGuard[1] or aheadOfGuard[0] >= n or aheadOfGuard[1] >= m:
                        outOfBounds = True
                        continue
                    if puzzlemap[aheadOfGuard[0]][aheadOfGuard[1]] == "#" or puzzlemap[aheadOfGuard[0]][aheadOfGuard[1]] == "O":
                        guardDirection = rightTurn[guardDirection]
                        continue
                    if (aheadOfGuard[0], aheadOfGuard[1], guardDirection) in visited:
                        loopingObstacles += 1
                        break
                    # Move forward
                    guardX, guardY = aheadOfGuard
                    visited.add((aheadOfGuard[0], aheadOfGuard[1], guardDirection)) 
                if DEBUG: printmap(puzzlemap, n, m, visited)
    
    print(f"There are {loopingObstacles} possible positions you can choose") 
       



try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2optimised(lines)
