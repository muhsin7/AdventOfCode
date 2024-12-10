from collections import defaultdict

DEBUG = False
def constructPagesToOnlyBePrintedAfter(orderingRules):
    pagesToOnlyBePrintedAfter = defaultdict(set)
    # X|Y -> if both X and Y exist, X must be printed before Y
    #     ~>            ...       , Y must be printed after X
    for rule in orderingRules:
        X, Y = rule.split("|")
        pagesToOnlyBePrintedAfter[Y].add(X)
    return pagesToOnlyBePrintedAfter

def isValidPageUpdates(pages, pagesToOnlyBePrintedAfter):
    # once pages[i] is reached, for the update to be valid,
    # no page from pagesToOnlyBePrintedAfter[pages[i]] should be in the list
    invalidpages = set()
    for page in pages:
        if page in invalidpages:
            return False
        # invalid pages = union of current inv. pages 
        #                 and inv. pages of current page
        invalidpages = invalidpages | pagesToOnlyBePrintedAfter[page]
    return True

def solution(puzzleinputlines):
    splittingIndex = puzzleinputlines.index("")
    orderingRules, updatePages = puzzleinputlines[:splittingIndex], puzzleinputlines[splittingIndex+1:]

    pagesToOnlyBePrintedAfter = constructPagesToOnlyBePrintedAfter(orderingRules)

    middlePageNumberSum = 0
    for pagestring in updatePages:
        pages = pagestring.split(",")
        validUpdate = isValidPageUpdates(pages, pagesToOnlyBePrintedAfter)
        if validUpdate:
            middlePage = pages[len(pages)//2]
            middlePageNumberSum += int(middlePage)
    
    print(f"Sum of middle page numbers from valid updates is: {middlePageNumberSum}")


# Uses backtracking to find the reordered version of the invalid page order
# Most likely can be optimized, currently takes ~3 mins to run the given input
def reorderInvalidUpdate(pages, pagesToOnlyBePrintedAfter):
    TOTAL_PAGES_LENGTH = len(pages)
    reorderedPages = None
    def findReorder(currentpages, remainingpages, currentinvalidpages):
        nonlocal reorderedPages
        if len(currentpages) == TOTAL_PAGES_LENGTH:
            # Stops backtracking when we reach full length
            reorderedPages = currentpages
            return
        for pagechoiceindex in range(len(remainingpages)):
            # Try each page that has yet to be placed in the order
            currentpagescopy = currentpages.copy()
            pagechoice = remainingpages[pagechoiceindex]

            # See if the page cannot be after any of the pages that has come before it
            if pagechoice not in currentinvalidpages:
                updatedremainingpages = remainingpages[:pagechoiceindex] + remainingpages[pagechoiceindex+1:]
                updatedinvalidpages = currentinvalidpages | pagesToOnlyBePrintedAfter[pagechoice]
                currentpagescopy.append(pagechoice)
                findReorder(currentpagescopy, updatedremainingpages, updatedinvalidpages)
        return
    
    findReorder([], pages, set())
    return reorderedPages


def solutionpart2(puzzleinputlines):
    splittingIndex = puzzleinputlines.index("")
    orderingRules, updatePages = puzzleinputlines[:splittingIndex], puzzleinputlines[splittingIndex+1:]

    pagesToOnlyBePrintedAfter = constructPagesToOnlyBePrintedAfter(orderingRules)
    middlePageNumberSum = 0
    i = 0
    for pagestring in updatePages:
        print(f"Processing page order #{i}")
        pages = pagestring.split(",")
        validUpdate = isValidPageUpdates(pages, pagesToOnlyBePrintedAfter)
        if not validUpdate:
            # Reorder the pages
            reorderedpages = reorderInvalidUpdate(pages, pagesToOnlyBePrintedAfter)
            if DEBUG: print(f"Reordered {pages} to {reorderedpages}")
            middlePage = reorderedpages[len(reorderedpages)//2]
            middlePageNumberSum += int(middlePage)
        i += 1

    print(f"Sum of middle page numbers from corrected updates is: {middlePageNumberSum}")


try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2(lines)