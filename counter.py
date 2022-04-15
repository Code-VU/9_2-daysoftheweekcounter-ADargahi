
def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    openFile = open(file_name)
    file = openFile.readlines()
    fromDict = {}

    for line in file:
        if line.startswith("From "):
            line = line.strip()
            line = line.split(' ')
            if line[2] in fromDict:
                fromDict[line[2]] += 1
            else:
                fromDict[line[1]] = 1
    print(fromDict)


            

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countDayOfTheWeek()