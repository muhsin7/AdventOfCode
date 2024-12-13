DEBUG = False
def solution(puzzleinputlines):
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    def dfs(posX, posY, currval, peaks):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if int(puzzleinputlines[posX][posY]) != currval:
            return 0
        
        if currval == 9 and not (posX, posY) in peaks:
            peaks.add((posX, posY))
            return 1
        peaksReachableFromLoc = 0
        for dx, dy in dirs:
            nextX, nextY = posX+dx, posY+dy
            if (0 <= nextX < n) and (0 <= nextY < m):
                peaksReachableFromLoc += dfs(nextX, nextY, currval+1, peaks)
        return peaksReachableFromLoc
    
    trailheadScoreSum = 0
    for i in range(n):
        for j in range(m):
            if puzzleinputlines[i][j] == "0":
                trailheadScoreSum += dfs(i, j, 0, set())
    print(f"Sum of all scores: {trailheadScoreSum}")

# Same implementation, now just counts duplicate peaks
def solutionpart2(puzzleinputlines):
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    def dfs(posX, posY, currval):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if int(puzzleinputlines[posX][posY]) != currval:
            return 0
        
        if currval == 9:
            return 1
        peaksReachableFromLoc = 0
        for dx, dy in dirs:
            nextX, nextY = posX+dx, posY+dy
            if (0 <= nextX < n) and (0 <= nextY < m):
                peaksReachableFromLoc += dfs(nextX, nextY, currval+1)
        return peaksReachableFromLoc
    
    trailheadScoreSum = 0
    for i in range(n):
        for j in range(m):
            if puzzleinputlines[i][j] == "0":
                trailheadScoreSum += dfs(i, j, 0)
    print(f"Sum of all ratings: {trailheadScoreSum}")

try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2(lines)