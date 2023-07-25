print("enter a string",end = '-')
inputString = input()
print("enter a integer",end = '-')
N = int(input())
listOut = []
shortestIndex = len(inputString)
for i in range(0, (len(inputString) -N +1)):
    searchChar = inputString[i]
    startSearchIndex = i + N - 1
    findIndex = inputString.find(searchChar, startSearchIndex)
    if (findIndex >= 0):
        if(findIndex - startSearchIndex) < shortestIndex:
            listOut = []
            shortestIndex = (findIndex - startSearchIndex)
            listOut.append(inputString[i:findIndex + 1])
        elif((findIndex-startSearchIndex) == shortestIndex):
            listOut.append(inputString[i:findIndex+1])
if(listOut == []):
    print("not-found")
else:
    print(*listOut)
