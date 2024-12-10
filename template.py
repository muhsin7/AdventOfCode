DEBUG = False
def solution(puzzleinputlines):
    # Implement here
    pass

def solutionpart2(puzzleinputlines):
    # Implement part 2 here
    pass

try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

solution(lines)
