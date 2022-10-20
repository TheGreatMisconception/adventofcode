def Day1Part1(textFilename):
    with open(textFilename, "r") as File:
        textFileinput = File.read().split("\n")
    textFilevalues = [int(i) for i in textFileinput]
    lastValue = None
    increaseCount = 0
    for depth in textFilevalues:
        if lastValue and lastValue < depth:
            increaseCount += 1
        lastValue = depth
    return increaseCount

if __name__ == "__main__":
    defaultTextfilename = "input.txt"
    Day1Part1(defaultTextfilename)
