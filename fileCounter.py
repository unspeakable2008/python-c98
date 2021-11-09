def fileCounter():
    fileName = input("enter the file name")
    numberofwords = 0
    file = open(fileName,"r")
    for line in file :
        words = line.split()
        numberofwords = numberofwords+len(words)
    print(numberofwords)
fileCounter()                