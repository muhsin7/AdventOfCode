from collections import defaultdict
DEBUG = True

def printmap(puzzleinputlines, n, m, visited=set()):
    debugmap = []
    for i in range(n):
        maprow = ""
        for j in range(m):
            if (i, j) not in visited:
                maprow += "."
            else:
                maprow += puzzleinputlines[i][j]
        debugmap.append(maprow)
    print("\n".join(debugmap))

def printposition(puzzleinputlines, n, m, position):
    debugmap = []
    for i in range(n):
        maprow = ""
        for j in range(m):
            if (i, j) == position:
                maprow += f"[{puzzleinputlines[i][j]}]"
            else:
                maprow += f" {puzzleinputlines[i][j]} "
        debugmap.append(maprow)
    print("\n".join(debugmap))

def printsubshape(puzzleinputlines, n, m, sidesetH, sidesetV):
    posset = set([x[0] for x in sidesetH | sidesetV])
    debugmap = []
    for i in range(n):
        maprow = ""
        for j in range(m):
            if (i, j) in posset:
                maprow += f"[{puzzleinputlines[i][j]}]"
            else:
                maprow += f" {puzzleinputlines[i][j]} "
        debugmap.append(maprow)
    print("\n".join(debugmap))

def solution(puzzleinputlines):
    visited = set()
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    # square plot
    n = m = len(puzzleinputlines)
    def dfs(posX, posY, plant):
        if ((posX < 0 or posY < 0
                or posX >= n or posY >= m)
                or puzzleinputlines[posX][posY] != plant):
            # boundary found -> increment perimeter
            return 0, 1
        if (posX, posY) in visited:
            # pre-visited nodes don't add to either 
            return 0, 0
        visited.add((posX, posY))
        # incremented area for successful case
        area, perimeter = 1, 0
        for dx, dy in dirs:
            nextX, nextY = posX+dx, posY+dy
            subArea, subPerim = dfs(nextX, nextY, plant)
            area += subArea
            perimeter += subPerim
        if DEBUG: print(f"{plant} -> {(area, perimeter)}")
        return area, perimeter
    totalPrice = 0
    for i in range(n):
        for j in range(m):
            if not (i, j) in visited:
                a, p = dfs(i, j, puzzleinputlines[i][j])
                totalPrice += a*p
    
    print(f"Total price of fencing: {totalPrice}")


try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

# solution(lines)
solutionpart2(lines)