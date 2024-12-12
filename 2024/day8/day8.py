from collections import defaultdict
DEBUG = False

def printmap(puzzleinputlines, n, m, antinode=set()):
    debugmap = []
    for i in range(n):
        maprow = ""
        for j in range(m):
            if (i, j) in antinode:
                maprow += "#"
            else:
                maprow += puzzleinputlines[i][j]
        debugmap.append(maprow)
    print("\n".join(debugmap))

def dist(pos1, pos2):
    return (pos1[0]-pos2[0], pos1[1]-pos2[1])

def addDelta(pos, delta):
    return (pos[0]+delta[0], pos[1]+delta[1])

def multDelta(delta, mult):
    return (delta[0]*mult, delta[1]*mult)

def inBounds(pos, n, m):
    return 0 <= pos[0] < m and 0 <= pos[1] < n

def solution(puzzleinputlines):
    antennasByFreq = defaultdict(list)
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    for i in range(n):
        for j in range(m):
            freq = puzzleinputlines[i][j]
            if freq.isalnum():
                antennasByFreq[freq].append((i, j))
    
    antinodes = set()
    for freq, antennaPositions in antennasByFreq.items():
        antennaCount = len(antennaPositions)
        for p in range(antennaCount):
            for q in range(antennaCount):
                if p != q:
                    posDelta = dist(antennaPositions[p], antennaPositions[q])
                    antinode = addDelta(antennaPositions[p], posDelta)
                    if inBounds(antinode, n, m):
                        antinodes.add(antinode)
    
                if DEBUG:
                    printmap(puzzleinputlines, n, m, antinodes)
                    print("------------------")

    print(f"Unique locations with an antinode: {len(antinodes)}")

def solutionpart2(puzzleinputlines):
    antennasByFreq = defaultdict(list)
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    for i in range(n):
        for j in range(m):
            freq = puzzleinputlines[i][j]
            if freq.isalnum():
                antennasByFreq[freq].append((i, j))
    
    antinodes = set()
    for freq, antennaPositions in antennasByFreq.items():
        antennaCount = len(antennaPositions)
        for p in range(antennaCount):
            for q in range(antennaCount):
                if p != q:
                    posDelta = dist(antennaPositions[p], antennaPositions[q])
                    deltaMultiplier = 0
                    while inBounds(addDelta(antennaPositions[p], multDelta(posDelta, deltaMultiplier)), n, m):
                        antinode = addDelta(antennaPositions[p], multDelta(posDelta, deltaMultiplier))
                        antinodes.add(antinode)
                        antinode = addDelta(antinode, posDelta)
                        deltaMultiplier += 1
    
                if DEBUG:
                    printmap(puzzleinputlines, n, m, antinodes)
                    print("------------------")

    print(f"Unique locations with an antinode with extended resonant harmonics: {len(antinodes)}")

try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2(lines)