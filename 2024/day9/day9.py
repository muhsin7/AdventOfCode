DEBUG = False

def constructBlocks(puzzleinput):
    blocks = []
    for i in range(len(puzzleinput)):
        # empty space block
        blockVal = -1
        if i%2==0:
            # file block ID
            blockVal = i//2
        for _ in range(int(puzzleinput[i])):
            blocks.append(blockVal)
    return blocks

def printReadableBlocks(tupblocks):
    res = ""
    for blockID, freq in tupblocks:
        blockVal = "." if blockID == -1 else str(blockID)
        res += blockVal*freq
    print(res)

# (ID, contiguous_block_size) tuples
def constructOptimisedBlocks(puzzleinput):
    blocks = []
    for i in range(len(puzzleinput)):
        # empty space block
        blockVal = -1
        if i%2==0:
            # file block ID
            blockVal = i//2
        blocks.append((blockVal, int(puzzleinput[i])))
    return blocks
# Space optimisation: instead of storing the file blocks as is,
# store them as (ID, contiguous_block_size) tuples
def solution(puzzleinput):
    blocks = constructBlocks(puzzleinput)
    i, j = 0, len(blocks)-1
    while i < j:
        if blocks[i] != -1:
            # non-empty block in left-side
            i += 1
            continue
        if blocks[j] == -1:
            # empty block in right-side
            j -= 1
            continue
        blocks[i], blocks[j] = blocks[j], blocks[i]
        i += 1
        j -= 1

    checksum = 0
    index = 0
    while blocks[index] != -1:
        checksum += index * blocks[index]
        index += 1

    print(f"Final checksum value: {checksum}")        

def solutionpart2(puzzleinput):
    blocks = constructOptimisedBlocks(puzzleinput)
    j = len(blocks)-1
    while j >= 0:
        tup = blocks[j]
        if tup[0] == -1:
            # empty block
            j -= 1
            continue
        for i in range(j+1):
            searchtup = blocks[i]
            if searchtup[0] == -1 and searchtup[1] >= tup[1]:
                # empty space with more space than
                spacediff = searchtup[1] - tup[1]
                if spacediff == 0:
                    # empty space = block space -> swap blocks
                    blocks[i], blocks[j] = blocks[j], blocks[i]
                else:
                    fileblock = tup
                    extraspaceblock = (-1, spacediff)
                    actualspaceblock = (-1, tup[1])
                    blocks[i] = fileblock
                    blocks[j] = actualspaceblock
                    # push remaining portion of empty block that was not swapped
                    blocks.insert(i+1, extraspaceblock)
                if DEBUG: printReadableBlocks(blocks)
                break
        j -= 1

    if DEBUG: printReadableBlocks(blocks)

    checksum = 0
    index = 0
    for tup in blocks:
        if tup[0] == -1:
            index += tup[1]
        else:
            for _ in range(tup[1]):
                checksum += index * tup[0]
                index += 1
    print(f"Final checksum value with new method: {checksum}")        


try:
    filename = "debuginput.txt" if DEBUG else "input.txt" 
    with open(filename, "r") as file:
        lines = file.read()
except:
    print("input.txt file not found in current directory")

solution(lines)
solutionpart2(lines)