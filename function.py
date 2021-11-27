def countWords():
    fileName=input("enter the file path:-")
    numberOfWords=0
    file=open(fileName,'r')
    for f in file:
        words=f.split()
        numberOfWords=numberOfWords+len(words)
    print("number of words in a file")    
    print(numberOfWords)

countWords()    
