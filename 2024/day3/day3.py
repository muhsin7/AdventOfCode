import re

def solution(puzzleinputlines):
    validcommands = re.findall("(mul\(\d+,\d+\))", puzzleinputlines)
    multsum = 0

    for command in validcommands:
        values = re.findall("\d+", command)
        multsum += int(values[0]) * int(values[1])
    
    print(f"Sum of mults: {multsum}")

def solutionpart2(puzzleinputlines):
    validcommands = re.findall("(mul\(\d*,\d*\))|(don't\(\))|(do\(\))", puzzleinputlines)
    multsum = 0
    enabled = True
    for command in validcommands:
        if command[1] == "don't()":
            enabled = False
            continue
        elif command[2] == "do()":
            enabled = True
            continue
        
        if enabled:
            values = re.findall("\d+", command[0])
            multsum += int(values[0]) * int(values[1])
    
    print(f"Sum of enabled mults: {multsum}")



try:
    with open("input.txt", "r") as file:
        data = file.read()
        lines = data
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2(lines)