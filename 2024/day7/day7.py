DEBUG = False
def solution(puzzleinputlines):
    def dfs(remainingnums, target, currval=0, nextop=""):
        if len(remainingnums) == 0:
            return currval == target
        
        nextval = remainingnums[0]
        if DEBUG: print(f"{currval} {nextop} {nextval}")
        if nextop == "":
            currval = nextval
        elif nextop == "+":
            currval += nextval
        elif nextop == "*":
            currval *= nextval
        
        # evalWith+asNextOp OR evalWith*asNextOp
        return dfs(remainingnums[1:], target, currval,"*") or dfs(remainingnums[1:], target, currval,"+")
    
    totalCalibration = 0
    for calibration in puzzleinputlines:
        testValue, equationString = calibration.split(": ")
        equationValues = list(map(int, equationString.split()))
        if dfs(equationValues, int(testValue)):
            totalCalibration += int(testValue)
    
    print(f"Total calibration value: {totalCalibration}")

def solutionpart2(puzzleinputlines):
    def dfs(remainingnums, target, currval=0, nextop=""):
        if len(remainingnums) == 0:
            return currval == target
        
        nextval = remainingnums[0]
        if DEBUG: print(f"{currval} {nextop} {nextval}")
        if nextop == "":
            currval = nextval
        elif nextop == "+":
            currval += nextval
        elif nextop == "*":
            currval *= nextval
        elif nextop == "||":
            currval = int(str(currval)+str(nextval))
        
        # evalWith+asNextOp OR evalWith*asNextOp OR evalWith||asNextOp
        return dfs(remainingnums[1:], target, currval,"*") or dfs(remainingnums[1:], target, currval,"+") or dfs(remainingnums[1:], target, currval,"||")
    
    totalCalibration = 0
    for calibration in puzzleinputlines:
        testValue, equationString = calibration.split(": ")
        equationValues = list(map(int, equationString.split()))
        if dfs(equationValues, int(testValue)):
            totalCalibration += int(testValue)
    
    print(f"Total calibration value: {totalCalibration}")

try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2(lines)