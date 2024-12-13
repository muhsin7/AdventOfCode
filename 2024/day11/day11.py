DEBUG = False
import math

def applyrule(num):
        digits = 1 if num == 0 else math.floor(math.log10(abs(num))) + 1
        if num == 0:
            return (False, 1)
        elif digits % 2 == 0:
            divider = 10**(digits//2)
            rhs = num % divider
            lhs = (num - rhs)//divider
            return (True, [lhs, rhs])
        else:
            return (False, num * 2024)
        
def solution(puzzleinputlines, ITERATIONS=25):
    rocks = list(map(int, puzzleinputlines.split()))
    for _ in range(ITERATIONS):
        buff = []
        for r in rocks:
            res = applyrule(r)
            if res[0]:
                buff.extend(res[1])
            else:
                buff.append(res[1])
        rocks = buff
    print(f"Number of stones after {ITERATIONS} blinks: {len(rocks)}")

# Thank you memoization
def solutionpart2(puzzleinputlines, ITERATIONS=75):
    rocks = list(map(int, puzzleinputlines.split()))
    memo = {}
    def findExpandedRockLength(num, its):
        if its == 0:
            return 1
        if (num, its) in memo:
            return memo[(num, its)]
        
        newrock = applyrule(num)
        if newrock[0]:
            result = findExpandedRockLength(newrock[1][0], its-1) + findExpandedRockLength(newrock[1][1], its-1)
        else:
            result = findExpandedRockLength(newrock[1], its-1)

        memo[(num, its)] = result
        return result

    totalStones = 0
    for rock in rocks:
        expandedRock = findExpandedRockLength(rock, ITERATIONS)
        if DEBUG: print(f"{rock} expands into {expandedRock} different rocks")
        totalStones += expandedRock

    print(f"Number of stones after {ITERATIONS} blinks: {totalStones}")

try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        lines = file.read()
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2(lines)
