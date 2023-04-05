#Caitlin Farley, HW7, program lists names from Pioneers.txt and takes input
#of name from user and outputs the persons accomplishment
    
#create loop condition for repeition
inputNewName = ('y','Y','Yes','yes')
goAgain = 'y'
while goAgain in inputNewName:
    
    def main ():
    
        
        def getList(textFile):
            inputFile = open(textFile, "r") #function will separate the textfile
            lineByLine = inputFile.readlines()    #line by line 
    
    
            allData=[]
    
            for currentLine in lineByLine:            #and put into a list separated by comma, names[0] accomplishments[1]
                currentList = currentLine.split(',')
                allData.append(currentList)    #[[Charles Babbage,is called the father of the computer],[Augusta Ada Byron,was the first computer programmer]]
        
            return allData

        def giveNames(allData):
            nameList = []
    
            for singleData in allData :    #function will take the names and put them into a different list and return them for user to see 

                nameList.append(singleData[0]) 
        
            return  nameList

        def getAccomp(inputedName,allData):
            
            for currentList in allData:
                if inputedName == currentList[0]:  #function will take the name inputed and return the corresponding accomplishment
                    return currentList[1]
            
            return "No match found. Please enter valid name!"

        List = getList("Pioneers.txt")

        names = giveNames(List)
        for name in names :
            print(name)

        inputedName = str(input("\nEnter a name from above list : "))
        inputedName = inputedName.title()
    
        accomp= getAccomp(inputedName,List)
    
        print(accomp)
    
    
    main()
#user is able to input another name if desired
    goAgain = input('Want to know about another person? Press Y ')
    
            
