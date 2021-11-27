def SwapFileData():
    fileOnedata=input("Enter your file name :  ")
    fileTwodata=input("Enter your file name :  ")

    with open(fileOnedata,'r') as sampleA:
        data_sampleA=sampleA.read()

    with open(fileTwodata, 'r') as sampleB:
        data_sampleB=sampleB.read()

    with open(fileOnedata, 'w') as sampleA:
        data_sampleA.write(fileTwodata)

    with open(fileTwodata, 'w') as sampleB:
        data_sampleB.write(fileOnedata)

SwapFileData()

