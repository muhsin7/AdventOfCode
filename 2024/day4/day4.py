DEBUG = False
def solution(puzzleinputlines):
    xmasfreq = 0
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    nextcharneeded = {
        "": "X",
        "X": "M",
        "M": "A",
        "A": "S",
    }
    def dfs(x, y, lastchar, setdirection=None):
        nonlocal xmasfreq
        currchar = puzzleinputlines[x][y]
        neededchar = nextcharneeded[lastchar]
        if currchar != neededchar: 
            return
        # currchar == neededchar at this point
        if neededchar == "S":
            xmasfreq += 1
            return
        directionsToExplore = dirs

        # Directional DFS
        # Once X->M goes in a certain direction, only look
        # for ->A->S in the same direction of X->M
        if setdirection: directionsToExplore = [setdirection]

        for dx, dy in directionsToExplore:
            nextx, nexty = x+dx, y+dy
            if 0 <= nextx < n and 0 <= nexty < m:
                dfs(nextx, nexty, currchar, setdirection=(dx,dy))

    for i in range(n):
        for j in range(m):
            dfs(i, j, "")

    print(f"XMAS appears {xmasfreq} times")

def solutionpart2(puzzleinputlines):
    n, m = len(puzzleinputlines), len(puzzleinputlines[0])
    diagonal1, diagonal2 = [(-1, -1), (1, 1)], [(-1, 1), (1, -1)]
    def isMas(x, y, diagonal):
        diagonalneighbours = ""
        for dx, dy in diagonal:
            nextx, nexty = x+dx, y+dy
            if nextx < 0 or nextx >= n or nexty < 0 or nexty >= m:
                # Out of bounds -> no possible X-MAS
                return False
            diagonalneighbours += puzzleinputlines[nextx][nexty]
        return diagonalneighbours == "MS" or diagonalneighbours == "SM"

    x_masfreq = 0
    for i in range(n):
        for j in range(m):
            if puzzleinputlines[i][j] == "A":
                if isMas(i, j, diagonal1) and isMas(i, j, diagonal2):
                    x_masfreq += 1
    
    print(f"X-MAS appears {x_masfreq} times")


try:
    with open("input.txt", "r") as file:
        data = file.read()
        if DEBUG:
            # 18 XMAS's
            data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2(lines)