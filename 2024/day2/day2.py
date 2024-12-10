DEBUG = False
def solution(puzzleinputlines):
    safereports = 0
    for reporti in range(len(puzzleinputlines)-1):
        report = puzzleinputlines[reporti].split(" ")
        safe = safeReport(report)
        if DEBUG: print(f"{puzzleinputlines[reporti]} -> {safe}")
        if safe:
            safereports += 1
    
    print(f"Total safe reports: {safereports}")

def safeReport(report):
    increasing = int(report[0]) < int(report[1])

    for i in range(0, len(report)-1):
        if not validJump(report[i], report[i+1], increasing):
            return False
    return True

# Returns if the jump is safe
def validJump(num1, num2, increasing):
    diff = int(num1) - int(num2)
    if not (1 <= abs(diff) <= 3):
        return False
    if (increasing and diff > 0) or (not increasing and diff < 0):
        return False

    # Safe so far...
    return True


def solutionpart2(puzzleinputlines):
    safereports = 0
    for reporti in range(len(puzzleinputlines)-1):
        report = puzzleinputlines[reporti].split(" ")
        safeWithoutDampener = safeReport(report)
        if safeWithoutDampener:
            safereports += 1
            continue

        safeWithDampener = False
        for i in range(len(report)):
            modifiedReport = report[:i] + report[i + 1:]  # Remove i-th level
            if safeReport(modifiedReport):
                safeWithDampener = True
                break
        if safeWithDampener:
            safereports += 1
    
    print(f"Total safe reports with dampener: {safereports}")


############################################################ 
# Attempted 2-pointer solution to potentially re-try later
#
# Problem was that it does not re-evaluate `increasing`
# when it dampens the 1st or 2nd element (i think)
############################################################

# def solutionpart2pointers(puzzleinputlines):
#     safereports = 0
#     for reporti in range(len(puzzleinputlines)-1):
#         report = puzzleinputlines[reporti].split(" ")
#         increasing = int(report[0]) < int(report[1])
#         safe = True
#         dampenerUsed = False
#         dampenedindex = None
#         i, j = 0, 1
#         while j < len(report):
#             if not validJump(report[i], report[j], increasing):
#                 if dampenerUsed:
#                     safe = False
#                     break
#                 # Skip the current level using the dampener
#                 dampenerUsed = True
#                 j += 1
#                 continue
            
#             # Move the pointers forward
#             i = j
#             j += 1
#         if DEBUG:
#             print(f"{puzzleinputlines[reporti]} -> {safe}")
#             print("---------------------")
#         if safe:
#             safereports += 1
    
#     print(f"Total safe reports with dampener: {safereports}")
#     print("---------------------")


try:
    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")
if not DEBUG:
    solution(lines)
    solutionpart2(lines)
if DEBUG:
    print("-----DEBUG INPUT PART 1-----")
    solution(['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1', '1 3 2 4 5', '8 6 4 4 1', '1 3 6 7 9', '1 3 6 7 9'])
    print("-----DEBUG INPUT PART 2-----")
    solutionpart2(['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1', '1 3 2 4 5', '8 6 4 4 1', '1 3 6 7 9', '1 3 6 7 9'])

