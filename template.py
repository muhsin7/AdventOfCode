def solution(puzzleinputlines):
    # Implement here
    pass


try:
    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.split('\n')
except:
    print("input.txt file not found in current directory")

solution(lines)
