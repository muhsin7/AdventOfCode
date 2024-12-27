DEBUG = False

import re
def extractnumbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    return [int(num) for num in numbers]
A_COST = 3
B_COST = 1

# DFS solution that works fine for part 1, not good enough for part 2
def solution(puzzleinputlines):
    mem = {}
    def dfs(currX, currY, currcost, clawmoves):
        if (currX, currY, clawmoves) in mem:
            return mem[(currX, currY, clawmoves)]
        aX, aY, bX, bY = clawmoves
        if currX == 0 and currY == 0:
            return currcost
        elif currX < 0 or currY < 0:
            return float("inf")
        
        a_cost = dfs(currX-aX, currY-aY, currcost+A_COST, clawmoves)
        b_cost = dfs(currX-bX, currY-bY, currcost+B_COST, clawmoves)
        optimal = min(a_cost, b_cost)
        mem[(currX, currY, clawmoves)] = optimal
        return optimal
    totalcost = 0
    for prize in puzzleinputlines:
        aString, bString, rewString = prize.split('\n')
        aX, aY = extractnumbers(aString)
        bX, bY = extractnumbers(bString)
        rewX, rewY = extractnumbers(rewString)

        cost = dfs(rewX, rewY, 0, (aX, aY, bX, bY))
        if cost != float("inf"):
            totalcost += cost
            print("--")    
    
    print(f"Total cost to get prizes is: {totalcost}")
    print("----------------")

# [ aX + bY = c ] [ dX + eY = f ]
def solve_linear_equations(a, b, c, d, e, f):
    # This was chatGPTed
    # Calculate the determinant of the coefficient matrix
    det = a * e - b * d
    
    if det == 0:
        raise ValueError("The system of equations has no unique solution.")
    
    # Calculate the determinants for X and Y
    detX = c * e - b * f
    detY = a * f - c * d
    
    # Calculate the values of X and Y
    X = detX / det
    Y = detY / det
    
    return X, Y

def solutionsimultaneous(puzzleinputlines, addPart2Constant=0):
    totalcost = 0
    for prize in puzzleinputlines:
        aString, bString, rewString = prize.split('\n')
        aX, aY = extractnumbers(aString)
        bX, bY = extractnumbers(bString)
        rewX, rewY = extractnumbers(rewString)

        # The problem can be represented in 2 linear equations
        #       aX + bX = rewX
        #       aY + bY = rewY
        # They will only have 1 solution or no solution 
        # since they only intersect at 1 point. In our 
        # case, if either value is negative it is also
        # considered an invalid solution
        try:
            A, B = solve_linear_equations(aX, bX, rewX+addPart2Constant, aY, bY, rewY+addPart2Constant)
            if A >= 0 and B >= 0 and A.is_integer() and B.is_integer():
                totalcost += int((3*A) + B) 
        except ValueError:
            pass  
    
    print(f"Total cost to get prizes is: {totalcost}")
    print("----------------")

# BFS that takes up too much memory for part 2
# crashes WSL even at about 5-6k size queue
# DFS solution obviously exceeds recursion limit
# from collections import deque
# def solutionpart2(puzzleinputlines):
#     currmoves = None
#     # mem = {}
#     def bfs(X, Y, cost):
#         q_back = deque([(X, Y, cost)])
#         q_front = deque([(0, 0, cost)])

#         optimal = float("inf")
#         visited_back = {(X, Y): 0}
#         visited_front = {(0, 0): 0}
        
#         while q_back and q_front:
#             print(f"Q lengths {len(q_back)}, {len(q_front)}")
#             if q_back:
#                 currX, currY, currcost = q_back.popleft()
#                 if (currX, currY) in visited_front:
#                     optimal = min(optimal, currcost + visited_front[(currX, currY)])
#                 aX, aY, bX, bY = currmoves

#                 for nextX, nextY, cos in [(currX-aX, currY-aY, A_COST), (currX-bX, currY-bY, B_COST)]:
#                     if nextX >= 0 and nextY >= 0 and (nextX, nextY) not in visited_back:
#                         visited_back[(nextX, nextY)] = currcost+cos
#                         q_back.append((nextX, nextY, currcost+cos))
#             if q_front:
#                 currX, currY, currcost = q_front.popleft()
#                 if (currX, currY) in visited_back:
#                     optimal = min(optimal, currcost + visited_back[(currX, currY)])

#                 aX, aY, bX, bY = currmoves

#                 for nextX, nextY, cos in [(currX+aX, currY+aY, A_COST), (currX+bX, currY+bY, B_COST)]:
#                     if nextX >= 0 and nextY >= 0 and (nextX, nextY) not in visited_front:
#                         visited_front[(nextX, nextY)] = currcost+cos
#                         q_front.append((nextX, nextY, currcost+cos))
#         return optimal
#     totalcost = 0
#     for prize in puzzleinputlines:
#         aString, bString, rewString = prize.split('\n')
#         aX, aY = extractnumbers(aString)
#         bX, bY = extractnumbers(bString)
#         rewX, rewY = extractnumbers(rewString)
        
#         currmoves = (aX, aY, bX, bY)
#         cost = bfs(rewX+10000000000000, rewY+10000000000000, 0)
#         if cost != float("inf"):
#             totalcost += cost    
    
#     print(f"Total cost to get the unit conversion error prizes is: {totalcost}")

try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n\n')
except:
    print("input.txt file not found in current directory")

# print("Part 1 solution")
# solution(lines)
print("Part 1 solution solved wwith equations")
solutionsimultaneous(lines)
print("Part 2 solution solved wwith equations")
solutionsimultaneous(lines, 10000000000000)



